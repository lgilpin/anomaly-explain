# File: rules.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Rule file for conceptual primitives and reasonableness monitor code.
#      Based on the MIT 6.034 Lab 1: Rule-Based Systems 

from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from production import PASS, FAIL, match, populate, simplify, variables
from data import *
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

# Uncomment this to test out your backward chainer
#pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules,
#                                        'opus is a penguin'))
#pprint.pprint(zookeeper_rules)

driving_rules_two_objs =  (
    IF( AND( '(?x) driving at velocity (?v) during (?y) and (?z)',
             'NO threats between (?y) and (?z)'),
        THEN( 'passenger is (?x) at velocity (?v) between (?y) and (?z)')),
    IF ( AND('moving (?v) at state (?y)', '(?z) succeeds (?y)',
             'moving (?v) at state (?z)'),
         THEN('safe driving at velocity (?v) during (?y) and (?z)')),
    
    IF (OR('(?y) is not moving', '(?y) is not located near',
           ('(?y) is not a large object')),
        THEN('(?y) not a threat at (?x)')),
    
    IF (AND('(?x) not a threat at (?y)', '(?x) not a threat at (?z)'),
        THEN('(?x) is not a threat between (?y) and (?z)')),
    
    IF (AND('input_data[1] is not a threat between (?y) and (?z)',
            'input_data[2] is not a threat between (?y) and (?z)'),
        THEN('NO threats between (?y) and (?z)')),
    )

def generate_arbitrary_rules(num):
    """"
    Returns a list of the number of data detections:
    """
    threat_text = "is not a threat between (?y) and (?z)"
    for i in range(num):
        rules.append("input_data[%d]"+threat_text %i)
    return rules

# Need to add velocity.  
driving_rules_one_obj =  (
    IF( AND( '(?x) driving at velocity (?v) during (?y) and (?z)',
             'obj is not a threat between (?y) and (?z)'),
        THEN( 'passenger is (?x) at velocity (?v) between (?y) and (?z)')),
    IF ( AND('moving (?v) at state (?y)', '(?z) succeeds (?y)',
             'moving (?v) at state (?z)'),
         THEN('safe driving at velocity (?v) during (?y) and (?z)')),
    IF (OR('obj is not moving',
           'obj is not located near',
           'obj is not a large object'),
        THEN('obj not a threat at (?x)')),
    IF (AND('obj not a threat at (?y)',
            'obj not a threat at (?z)',
            '(?z) succeeds (?z)',
        THEN('obj is not a threat between (?y) and (?z)'))
    )

short_rules_for_demo = (
    IF( AND( '(?x) driving at (?v) during (?y) and (?z)',
             'obj is not a threat between (?y) and (?z)'),
        THEN( 'passenger is (?x) at (?v) between (?y) and (?z)')),
    IF ( AND('moving (?v) at state (?y)',
             '(?z) succeeds (?y)',
             'moving (?v) at state (?z)'),
         THEN('safe driving at (?v) during (?y) and (?z)')),
    IF (OR('obj is not moving', 'obj is not located near',
           ('obj is not a large object')),
        THEN('obj not a threat at (?x)')),
    IF (AND('obj not a threat at (?y)', 'obj not a threat at (?z)'),
        THEN('obj is not a threat between (?y) and (?z)'))
    )

driving_rules_in_progress = (
    IF( AND( "(?x) safe driving",
             NOT("(?x) is a large moving object")),
        THEN( "(?x) is safe" )),
    
    IF( AND( "(?x) is moving",
             "(?x) is large" ),
        THEN( "(?x) is a large moving object"))
)

pretty_goal_tree(
    backchain_to_goal_tree(driving_rules_two_objs,
                           'passenger is safe at velocity V between s and t'))

pretty_goal_tree(
    backchain_to_goal_tree(driving_rules_one_obj,
                           'passenger is safe at velocity V between s and t'))

pretty_goal_tree(
    backchain_to_goal_tree(short_rules_for_demo,
                           'passenger is safe at V between s and t'))

reasonable_rule =(
    IF( AND('(?x) is moving'
        '(?x) hasProperty animate',
        THEN('(?x) is reasonable.'))))
        
