# File: synthesize.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Explanation Synthesizer code

#from priority import *

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

def diagnose(explanations):
    """
    Diagnoses the root cause of a set of explanations against a given
    priority hierarchy

    """
    return 
# High Level rules 
