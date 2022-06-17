# File: rules.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Rule file for conceptual primitives and reasonableness monitor code.
#      Based on the MIT 6.034 Lab 1: Rule-Based Systems 

from .production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from .production import PASS, FAIL, match, populate, simplify, variables
from .data import *
import pprint

CHAR_OFFSET = 97

# RULES FOR FORWARD CHAINING 
same_IsA_rule = IF('(?x) IsA (?y)', THEN('self (?x) (?x)'))
same_location_rule = IF('(?x) AtLocation (?y)', THEN('self (?x) (?x)'))
consistent_anchor_rule = IF(AND("(?x) IsA (?y)", "(?z) IsA (?y)",
                           NOT("self (?x) (?z)")),
                       THEN("(?x) consistent (?z)"))
consistent_location_rule = IF(AND("(?x) AtLocation (?y)", "(?z) AtLocation (?y)",
                                  NOT("self (?x) (?z)")), #NOT("(?z) sameLocation (?y)")),
                       THEN("(?x) sameLocation (?z)"))

anchor_rules = [same_IsA_rule, consistent_anchor_rule]
location_rules = [same_location_rule, consistent_location_rule]


# make consistent rules?

# make size rules

def same_anchor_rule(num=2):
    statements = []
    consequent = "consistent"
    for i in range(0,num):
        binding = "(?%c)"%chr(i+CHAR_OFFSET)
        statements.append( "IsA(%s, (?x))"%binding)
        consequent += " %s"%binding
    return IF (AND (statements), THEN(consequent))

def isReasonable(labels, commonsense_data):
    """
    Checks the data for certain reasonability checks:
    (1) are they the same anchor point
    (2) are they located at the same location
    (3) are they at the same size
    (4) are they moving (or not)
    If any of these are not met, then it's unreasonable
    """
    explanation = []
    reasonable = True # True unless proven false 
    # check same object

    if not same_anchor(labels):
        explanation.append("labels are different anchors: %s"%anchor_summary())
        reasonable = False

    # check same location
    if not same_location(labels):
        explanation.append("labels are not at the same location")
        reasonable = False
    else:
        explanation.append("located at the same location")

    # check same size
    if not same_size(labels):
        explanation.append("labels are of different size: %s"%size_summary())
        reasonable = False
    else:
        explanation.append("")

    return (reasonable, explanation)

#### Backward Chaining #########################################

def backchain_to_goal_tree(rules, hypothesis):            
    """
    LHG Code from 6.034, modified for the ADE system.

    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """
    top_level = [hypothesis]
    
    for rule in rules:
        matching = match(rule.consequent(), hypothesis)
        
        if matching is not None:
            tree = []
            next = populate(rule.antecedent(), matching)
            ant_stuff = type(rule.antecedent())
            
            if ant_stuff is str: # leaf
                tree.append(backchain_to_goal_tree(rules, next))
            else: 
                for hyp in next:
                    tree.append(backchain_to_goal_tree(rules, hyp))
                    
            if ant_stuff == OR:
                top_level.append(OR(tree))
            else: top_level.append(AND(tree))
    return simplify(OR(top_level))

# Uncomment this to test out your backward chainer:
#pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules, 'opus is a penguin'))
#pprint.pprint(zookeeper_rules)

driving_rules = (
    IF( AND( "(?x) safe driving",
             NOT("(?x) is a large moving object")),
        THEN( "(?x) is safe" )),
    
    IF( AND( "(?x) is moving",
             "(?x) is large" ),
        THEN( "(?x) is a large moving object"))
)

#pretty_goal_tree(backchain_to_goal_tree(driving_rules, 'passenger is safe'))
