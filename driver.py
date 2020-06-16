# File: driver.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: High-level reasoner code.   

import argparse
import requests
import sys
import logging

import nltk
from sympy import *  # python symbolic package
from sympy.logic import SOPform
import itertools
from time import process_time

# TODO we may want to do some data science stuff 
import pandas as pd
import numpy as np
import csv

import commonsense.conceptnet as kb
import synthesizer.synthesize as synthesize

import monitor.reasonableness_monitor as monitor

# We may not want to use a priority queue
from queue import PriorityQueue
needs = PriorityQueue() #we initialise the PQ class instead of using a
                        #function to operate upon a list.
domain = None
anchors = ['animal', 'object', 'place', 'plant']
relations = ['AtLocation', 'LocatedNear'] # technically these are vehicle relations for now

class Reason:
    def __init__(self, rdf, reason):
        self.rdf = rdf
        self.ind = 1   # for referencing
        self.reason = reason

    def add_reason(self, reason):
        self.reason = reason

class Synthesizer:
    """Started setting this out

    But really, the synthesizer just has (1) a set of candidate
    explanations and (2) a priority hierarchy 

    """
    def __init__(self, relations, anchors, data, rules):
        self.relations = relations
        self.anchors = anchors
        self.data = data
        self.rules = rules
        
"""
Section on data tables
"""

def initialize(relationFile, anchorFile):
    """" Lists the relations for the semantic database
    Should also have domains attached to the some of the relations

    TODO: Check format of the file, etc 
    """
    relations = make_data_frame(relationFile)
    anchors = make_data_frame(anchorFile)

def make_data_frame(fileName):
    """ Makes a dataframe from the specified file

    CSV files are assumed to have a heading with a:
    header
    info....
    """
    try:
        raw_relation_data = pd.read_csv(fileName)
        logging.debug("%s is parsed as a csv file" %fileName)
        logging.debug(raw_relation_data.head())
    except pd.errors.ParserError:
        raw_relation_data = pd.DataFrame()
        with open(fileName, 'r') as f:
            for line in f:
                raw_relation_data = pd.concat( [df,
                                 pd.DataFrame([tuple(line.strip().split('\s+'))])],
                                ignore_index=True )
    return raw_relation_data

def clean_relations(raw_data):
    """
    Cleans relation raw data from a file 
    """
    for element in raw_data:
        print(element)
    return raw_data

# Takes symbolic reasons and turns it into a natural language explanation 
def make_explanation(reasons):
    return reasons

# This will "imagine the future and generate a few candidate plans
# How does one do this?  * Or do we assume the planner?
def generate_candiates(state):
    return ["continue-forward", "stop", "veer-slow-down"]

# TODO - How will this be defined?
# Define an API for this. 
def make_needs_hierachy():
    needs.put(1, symbols('passenger-safety'))
    needs.put(2, symbols('passenger-perceived-safety'))
    needs.put(3, symbols('passenger-comfort'))
    needs.put(4, symbols('route-efficiency'))
    # safety of the person in the vehicle (1)
    # safety of the people around
    # safety of moving things (animals)
    return 

def check_hierarchy():    
    return

# Takes in an arbitrary number of explanations (tested for up to...)
# Returns an explanation and the correct intended action
# If actions are not provided by the underlying algorithm, ...TODO
# Group Explanations / explanation alignement 
def synthesize_explanations(*explanations, actions):
    """
    Step 1 - alignment
    Step 2 - provenance 
    """
    for (is_reasonable, explanation) in explanations:
        logging.debug(is_reasonable)
        logging.debug(explanation)
    action = synthesize.diagnose(explanations)
    return explanations

# Return a list of symbolic triples supporting the explanation 
def get_explanation_uber(symbol_list, case):
    if case=='vision':
        for exp in symbol_list:
            add_common_sense(exp)
        if similar(symbol_list):
            logging.debug("They're similar")
        else:
            logging.debug("They're not similar")
        return (False, symbol_list)
    elif case=='lidar':
        for exp in symbol_list:
            print(exp)
            symbol_list = []
        return (True, symbol_list)
    else: # Then it's the case for actions
        for exp in symbol_list:
            print(exp)
            symbol_list = []
        return (True, symbol_list)
    
def run_uber_example():
    """
    Iniatives the uber example
    1.  Vision reports an unknown object, a vehicle, and then a bicycle
    2.  Lidar reports interpretted information
    3.  State is moving forward quickly has been going straight, etc 
    """
    start_time = process_time() # starting time

    # From the Uber report: The vision system reports, "unknown
    # object, as a vehicle, and then as a bicycle with varying
    # expectations of future travel path."
    vision = symbols('unknown_object vehicle bicycle')
    visionExplain = monitor.snapshot_monitor(vision, anchors,relations, True)

    lidar = symbols('object_moving 5_ft_tall top_left_quadrant')
    lidarExplain = (symbols('reasonable'), lidar)

    state = symbols('moving_quickly proceed_straight has_been_straight')
    stateExplain = (symbols('reasonable'), state)

    actions = symbols('forward stop veer-slow')

    explanation = synthesize_explanations(visionExplain, lidarExplain,
                                          stateExplain, actions=actions)    
    
    #expr = SOPform(sm, minterms) # find the expression
    end_time = process_time() # end time
    print('explanation :', explanation)
    print('\nprocessing time (in seconds):', end_time-start_time)

def main():
    """
    Right now, this tests the Uber example

    REQUIREMENT: The anchors and commonsense files need to be .csv
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', 
                        help='This is the same as debug right now')
    parser.add_argument("-d", "--domain", action='store_true', 
                        help='Enter the particular domain', default='vehicle')
    parser.add_argument("-r", "--relations", action='store_true',
                        help='The datafile with descriptions of the relations',
                        default='commonsense/relations.csv')
    parser.add_argument("-a", "--anchors", action='store_true',
                        help='The datafile with descriptions of the anchors/ontology',
                        default='commonsense/anchors.csv')
    
    args = parser.parse_args()
    domain = args.domain

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(message)s')

    # Logging info for verbose and other debugging
    logging.info("Verbose output.")
    logging.info("Explaining behavior in the %s domain\n" %args.domain)

    initialize(args.relations, args.anchors)

    run_uber_example()

if __name__ == "__main__":
    main()

