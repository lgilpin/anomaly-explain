# File: priority.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Priority file for the explanation synthesizer

import sys
import os
#sys.path.append(os.path.abspath('../'))

from reasoning.production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from reasoning.production import PASS, FAIL, match, populate, simplify, variables
from reasoning.data import *
import pprint

PRIORITIES = []
OPTIONS = ['continue', 'stop', 'veer and slow down']

def get_priorities():
    return ['safety', 'perceived_safety', '', 'efficiency']

def set_priorities_from_file(fileName):
    """
    Read a file line by line with the prioriites
    """
    f = open(fileName, "r")
    for x in f:
        PRIORITIES.append(x)
    return PRIORITIES


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
        THEN('obj is not a threat between (?y) and (?z)'))))

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

reasonable_rule =(
    IF( AND('(?x) is moving'
        '(?x) hasProperty animate',
        THEN('(?x) is reasonable.'))))


