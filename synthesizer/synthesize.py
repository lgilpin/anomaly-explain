# File: synthesize.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Explanation Synthesizer code

import sys
import os
sys.path.append(os.path.abspath('../'))

#from priority import *
from reasoning.production import *
from reasoning.data import *
from .priority import *

DISAGREE = 'unreasonable'

class Synthesizer:
    """Started setting this out

    The synthesizer just has (1) a set of candidate
    explanations and (2) a priority hierarchy 

    """
    def __init__(self, relations, anchors, data, rules):
        self.relations = relations
        self.anchors = anchors
        self.data = data
        self.rules = rules

    def set_priorities(self):
        # Check it is not null 
        self.priorities = get_priorities()

    def set_rules(self):
        return

#class Priorities:

def full_text(explanations):
    """
    Puts it into full text
    """
    output = ''
    for (reasonable, explanation) in explanations:
        output += str(reasonable)
        output += str(explanation)
    return output

def disagree(explanations):
    """
    Placeholder function for synthesizer
    Checks for key disagreement words 
    TODO Needs more careful parsing
    """
    reasons = full_text(explanations)
    if 'unreasonable' in reasons:
        return True
    else: return False 

def diagnose(explanations, options=OPTIONS):
    """
    Diagnoses the root cause of a set of explanations against a given
    priority hierarchy

    """
    if disagree(explanations):
        best = OPTIONS[-1]
    else: best = 'continue'
    diagnosis_text = "The best option is to %s." %best
    return diagnosis_text

def parse_reason(explanation):
    """
    The input explanation should be a triple.
    """
    (subject,_,_) = explanation
    return "The "+str(subject)

def synthesize(explanations):
    for (reason, explanation) in explanations:
        if is_threat(explanation):
            return parse_reason(explanation)+\
                "Is a threatening object that should be avoided." 
    return "default"

def is_threat(reason):
    text=''
    for item in reason:
        text+=str(item)
    if 'tall' and 'moving' in text:
        return True
    else: return False

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

def align(reasons):
    return True

def uber_synthesize(explanations=None):
    """
    Runs the uber example for the synthesizer 
    """
    print("synthesizing the uber example")
    print("Using default driving priorities.  Goal tree as follows")
    goals = backchain_to_goal_tree(short_rules_for_demo,
                           'passenger is safe at V between s and t')
    pretty_goal_tree(goals) # this is a type OR tree

    print('monitoring outputs:', explanations)
    if explanations and align(explanations):
        judgement = diagnose(explanations)
        summary = synthesize(explanations)
        print("SYNTHESIZER OUTPUT:", judgement, summary)
    else:
        print("Explanations cannot align")

def main():
    uber_synthesize()

if __name__ == '__main__':
    main()
