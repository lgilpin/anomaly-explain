# File: rule_reasoner.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Rule file for conceptual primitives and reasonableness monitor code.
#      Based on the MIT 6.034 Lab 1: Rule-Based Systems 

from .production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from .data import *
import pprint

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

# Fill this in with your rule 
transitive_rule = IF( AND('(?x) beats (?y)','(?y) beats (?z)'),
                           THEN('(?x) beats (?z)'))

transitive_IsA_rule = IF( AND ('IsA((?x), (?y))', 'IsA((?y), (?z)'),
                          THEN('IsA((?x), (?z))'))

# You can test your rule by uncommenting these pretty print statements
#  and observing the results printed to your screen after executing lab1.py
# pprint(forward_chain([transitive_rule], abc_data))
# pprint(forward_chain([transitive_rule], poker_data))
# pprint(forward_chain([transitive_rule], minecraft_data))

CHAR_OFFSET = 97

def same_anchor_rule(num=2):
    statements = []
    consequent = "consistent"
    for i in range(0,num):
        binding = "(?%c)"%chr(i+CHAR_OFFSET)
        statements.append( "IsA(%s, (?x))"%binding)
        consequent += " %s"%binding
    return IF (AND (statements), THEN(consequent)) 

#### Part 3: Family Relations #########################################

# Define your rules here. We've given you an example rule whose lead you can follow:
friend_rule = IF( AND("person (?x)", "person (?y)"), THEN ("friend (?x) (?y)", "friend (?y) (?x)") )


child_rule = IF ("parent (?x) (?y)", THEN("child (?y) (?x)"))
same_rule = IF('person (?x)', THEN('self (?x) (?x)'))
sibling_rule = IF(AND ("parent (?x) (?y)", "parent (?x) (?z)", NOT("self (?y) (?z)")),
                  THEN ("sibling (?y) (?z)"))


#  x and y are cousins (a parent of x and a parent of y are siblings,
#  but x and y are not siblings)
cousin_rule =  IF ( AND ("parent (?a) (?x)", "parent (?b) (?y)", "sibling (?a) (?b)",
                         NOT("sibling (?x) (?y)"), NOT("self (?x) (?y)")),
                    THEN ("cousin (?x) (?y)"))
gradparent_rule = IF (AND ("parent (?z) (?y)", "parent (?y) (?x)"),
                      THEN ("grandparent (?z) (?x)"))

grandchild_rule = IF ("grandparent (?y) (?x)", THEN("grandchild (?x) (?y)"))


# Add your rules to this list:
family_rules = [same_rule, child_rule, sibling_rule, cousin_rule, gradparent_rule, grandchild_rule]


# These smaller datasets might be helpful for debugging:
# pprint(forward_chain(family_rules, sibling_test_data, verbose=True))
# pprint(forward_chain(family_rules, grandparent_test_data, verbose=True))

# The following should generate 14 cousin relationships, representing 7 pairs
# of people who are cousins:
black_family_cousins = [
     relation for relation in
     forward_chain(family_rules, black_data, verbose=False)
     if "cousin" in relation ]

# To see if you found them all, uncomment this line:
# pprint(black_family_cousins)

###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!
# print("(Doing forward chaining. This may take a minute.)")
# transitive_rule_poker = forward_chain([transitive_rule], poker_data)
# transitive_rule_abc = forward_chain([transitive_rule], abc_data)
# transitive_rule_minecraft = forward_chain([transitive_rule], minecraft_data)
# family_rules_simpsons = forward_chain(family_rules, simpsons_data)
# family_rules_black = forward_chain(family_rules, black_data)
# family_rules_sibling = forward_chain(family_rules, sibling_test_data)
# family_rules_grandparent = forward_chain(family_rules, grandparent_test_data)
# family_rules_anonymous_family = forward_chain(family_rules, anonymous_family_test_data)
