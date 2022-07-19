# File: monitor.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Local Reasonabeless monitors for the high-level synthesizer.
from typing import List

from dataclasses import dataclass, field
import logging
import pandas as pd

from commonsense.conceptnet import Fact, ConceptNet
from commonsense.kb import KB
from commonsense.logical_classes import to_data_frame, get_fact_query, Event
from reasoner import rules
from reasoner.production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from reasoner.chain import *

data_header = ['fact', 'reason'] # DATA HEADERS

# Map for my judgement, this can be changed
judgement = {True:'reasonable', False: 'unreasonable'}
confidence = {1: 'poor visibility', 2: 'fair visibility',
              3: 'good visibility', 4: 'great visibility'}
# safe vs unsafe -- user study.

DEFAULT_ANCHORS = ['person', 'animal', 'object', 'place', 'plant']
DEFAULT_RELATIONS = ['AtLocation', 'LocatedNear']

"""
TODO : Add in average size
"""
@dataclass
class SnapshotMonitor:
    """I started created this as an object, but in reality, it doesn't
    really use much of this """
    labels: List = field(default_factory=list)
    data: List = field(default_factory=list)
    rules: List = field(default_factory=list)  # This will have to be changed
    system_name: str = "default"

    reasonable: bool = True
    near_miss: bool = False
    anchors: List[str] = None  # This might not be necessary
    sym_exp: List = field(default_factory=list)  # Right now, this is separated into supports

    # Again, this isn't really used: and disputes
    support: List = None
    dispute: List = None

    reasons: List = field(default_factory=list)  # Not really used, but keeping it around in case.

    text_exp: str = ""
    kb: KB = ConceptNet()  # Companion()

    def kb_name(self) -> str:
        """
        This may want to be more verbose
        :return:
        :rtype:
        """
        if type(self.kb) == ConceptNet:
            return "ConceptNet"
        else: return "NextKB"
    # ^ Have this in the constructor
# kb = CompanionKB    
    # def __init__(self, labels, data, rules, system_name="vision perception"):
    #     """I started created this as an object, but in reality, it doesn't
    #     really use much of this """
    #     self.labels = labels
    #     self.data = data
    #     self.rules = rules
    #     self.system_name = system_name
    #
    #     self.reasonable = True
    #     self.near_miss = False
    #     self.anchors = [] # This might not be necessary
    #     self.sym_exp = [] # Right now, this is separated into supports
    #                       # and disputes
    #     self.support = None
    #     self.dispute = None
    #
    #     self.reasons = []  # Not really used, but keeping it around in case.
    #
    #     self.text_exp = ""
    #     self.kb = ConceptNet()  # Companion()

        #facts = add_commonsense(labels, anchors, relations, labels) #wtf are labels?
    def add_data(self, data_point):
        """

        :param data_point:
        :type data_point:
        :return:
        :rtype:
        """
        self.data = data_point # Change that

    def add_reason(self, reason):
        self.reasons.append(reason)

    def label_summary(self):
        """
        Returns a string summary of the labels in question
        """
        if self.labels:
            return ", ".join(str(x) for x in self.labels)
        else:
            return 

    def make_explanation(self, explanations):
        """
        Constructs the explanation for a SnapshotMonitor
        It is constructed from looking at the reasons, supports, and contradictions

        Essentially is an explanation translator 
        """
        summary = "This %s is %s.  "% (self.system_name, judgement[self.reasonable])

        if self.near_miss:
            summary += "There is commonsense supporting that this could be a %s" \
                %near_miss_summary()
        elif not self.reasonable: # Use to be an else 
            summary += "There is no commonsense supporting the similarity between %s" \
                %self.label_summary()
            if self.support:
                summary += " except that ", translate(self.support)

        #for explanation in explanations:
        #    summary+=explanation+".  "
        if not self.reasonable:
            summary+=".  This component should be ignored."
        else:
          summary+="There is commonsense supporting the same %s between %s"\
              %("location",self.label_summary())
        return (self.reasonable, summary)

    def get_fact_list(self):
        """
        Returns the set of facts (without the underlying reasons) for
        rule-based analysis.
        """
        return self.data['fact'].values.toList()

    def test_reasonable_snapshot(self, data, symbols, context=False):

        """
        Tests whether this is a reasonable point in time given a set of rules.
        """
        # Check that they are all the same anchor?
        facts = data['fact']
        logging.debug(facts)
    
        fact_data = facts.values.tolist()
        logging.debug(fact_data)

        # Checking the anchors 
        anchors = rules.anchor_rules
        data = supplement(anchors, data, 'Anchor rule fired')
        logging.debug("new data is %s"%data)

        locations = rules.location_rules
        data = supplement(locations, data, 'Location rule fired')
        logging.debug("new data is %s"%data)

        (judgement, explanations) = self.isReasonable(data, symbols, context)
        return self.make_explanation(explanations)
    
    def isReasonable(self, data, labels, context=False):
        """
        Checks the data for certain reasonability checks:
        (1) are they the same anchor point
        (2) are they located at the same location
        (3) are they at the same size
        (4) are they moving (or not)
        If any of these are not met, then it's unreasonable
        """
        explanation = []

        # how many labels:
        #print("Are we here in reasonable",labels)
        many_labels = True
        if labels:
            many_labels = True

        # check same object
        if not same_anchor(labels, data) and many_labels:
            explanation.append("labels are different anchors: %s"%anchor_summary())
            self.reasonable = False

        # check same location
        if not same_location(labels, data) and many_labels:
            if check_alternatives(labels, data):
                explanation.append("%s located at the same location")
                #            %s"%(label_summary(labels), location_summary()))
            else:
                explanation.append("labels are not at the same location")
                self.reasonable = False
        else:
            explanation.append("%s located at the same location of %s"
                               %(self.label_summary(), location_summary()))

        # check same size
        if not same_size(labels, data) and many_labels:
                explanation.append("labels are of different size: %s"\
                                   %size_summary(labels))
                self.reasonable = False
        else:
            explanation.append(size_summary(labels))
        if context:
            #self.reasonable = True
            self.reasonable = self.kb.connected(labels)
        return (self.reasonable, explanation)

    def add_commonsense(self, symbols, anchors, relations, labels=False):
        """
        TODO: eliminate this is a repeat method
        This method adds commonsense information for a particular concept

        TODO: find the base concept

        1.  Adds the anchor point information
        2.  Adds the important symbolic relations
        """
        reasons = []
        # if type(symbols) is not list:
        #     return add_single_commonsense(symbols, anchors, relations, labels=False)
        # 1: Anchoring
        for sym in symbols:
            concept = str(sym)
            anchor = self.kb.find_anchor(concept, anchors)
            reasons.append(anchor)
            # print("REASONS ARE %s" % reasons)

        # 2: Adding commonsense for the relations of interest
        if labels:
            # Then this is a sort of description
            for concept in symbols:
                logging.debug("Accessing KB for this concept: %s" % concept)
                reasons += self.kb.aggregate(concept, relations)
        else:
            if has_verb(symbols):
                # Represent in conceptual primitives
                return "Not implemented yet"

        print("REASONS ARE %s" % reasons)
        logging.debug(reasons)
        data = to_data_frame(reasons)
        print(data)
        # data = pd.DataFrame(reasons, columns=['fact', 'reason'])
        return data
        # else return []

    def explain_analogy(self, query: Fact):
        # make events from facts
        print("testing")
        
    def explain_fact(self, starter_fact: Fact):
        """
        TODO / Inprogress function to explain a "starter" fact or list of facts
        1.  Get all concepts from the starter fact
            - If it has a verb, use verb anchors
            - If it doesn't use a verb, look *only* for commonsense connections
        2.  Aggregate commonsense for each concept
        3.  Run reasoner to see if there are any contradictions.
        :param starter_fact: The fact to start with.
        :return: TODO
        """
        fact = self.kb.clean(starter_fact)

        if self.anchors is None:
            self.anchors = DEFAULT_ANCHORS
        # iterate through the fact...
        # for concept in starter_fact.all_concepts():
        #     # get all commonsense facts
        #     print(concept)
        #     symbols = labels
        # Add back in for a given set of relations.
        facts = self.kb.search(fact.subject, relation='IsA', reason=self.kb_name())
        facts += self.kb.search(fact.object, relation='IsA', reason=self.kb_name())
        logging.debug("Snapshot monitor made with the following data: %s" % facts)
        # monitor = SnapshotMonitor(symbols, facts, [], "vision system")
        return facts
        # return to_data_frame(facts)


    def explain(self, facts: List, add_facts: List = None, preference: Fact = None, to_df: bool = False):
        if len(facts) == 1:
            starter_facts = self.explain_fact(facts[0])
            if add_facts:
                all_facts = starter_facts + add_facts
                domain_specific_facts = to_data_frame(add_facts)
                #all_facts = \
                    #pd.concat([starter_facts, domain_specific_facts], ignore_index=True)
            else:
                all_facts = to_data_frame(starter_facts)
        else: # if we have more than one fact then we want to explain all the events
            self.explain_events(facts, add_facts)
        if preference:
            print("Preference is %s"%preference.to_string())
        explanation = chain_explanation(all_facts, preference)
        # for item in explanation:
        #     print("(%s)"%item.to_string())
        explanation = summarize(all_facts, explanation[-1].subject)
        return explanation


    def explain_all_events(self, facts: List, add_facts: List = None) -> None:
        df = to_data_frame(facts)
        events = df.groupby("subject")
        for event in events:
            (name, event_df) = event
            event_type = "looking" if name.startswith("looking") else "speaking"
            print("Explaining", name)
            observer = event_df[event_df['predicate'] == 'observedBy'][['object']].values[0][0]
            doer = event_df[event_df['predicate'] == 'observedBy'][['object']].values[0][0]
            print("  %s is observing a %s event"%(observer, event_type))

            # Check for alignment between additional facts
            if event_type == "looking":
                looker = event_df[event_df['predicate'] == 'looker'][['object']].values[0][0]
                direction = event_df[event_df['predicate'] == 'direction'][['object']]
                if not direction.empty:
                    direction_str = direction.values[0][0].lower()
                    print("  %s looking in %s direction"%(looker, direction_str))
                    if add_facts:
                        # check if the direction is in the additional facts
                        fact = get_fact_query(direction_str, add_facts)
                        if fact:
                            reason = fact.object
                            print("  Since %s is looking in %s direction, %s is %s"%(looker, direction_str, looker, reason))
            else:
                speaker = event_df[event_df['predicate'] == 'speaker'][['object']].values[0][0]
                utterance = event_df[event_df['predicate'] == 'utterance'][['object']].values[0][0]
                print("  %s spoke %s" % (speaker, utterance))
            print(event_df)

    def explain_event(self, event: Event, add_facts: List = None):
        name = event.event_type
        event_df = to_data_frame(event.facts)
        # type_name = event_df[event_df['predicate'] == 'isA'][['object']].values[0]
        # name = "looking" if type_name.startswith("looking") else "speaking"
        print("Explaining", name)
        observer = event_df[event_df['predicate'] == 'observedBy'][['object']].values[0][0]
        doer = event_df[event_df['predicate'] == 'observedBy'][['object']].values[0][0]
        print("  %s is observing a %s event" % (observer, name))

        # Check for alignment between additional facts
        if name == "looking":
            looker = event_df[event_df['predicate'] == 'looker'][['object']].values[0][0]
            direction = event_df[event_df['predicate'] == 'direction'][['object']]
            if not direction.empty:
                direction_str = direction.values[0][0].lower()
                print("  %s looking in %s direction" % (looker, direction_str))
                if add_facts:
                    # check if the direction is in the additional facts
                    fact = get_fact_query(direction_str, add_facts)
                    if fact:
                        reason = fact.object
                        print(
                            "  Since %s is looking in %s direction, %s is %s" % (looker, direction_str, looker, reason))
        else:
            speaker = event_df[event_df['predicate'] == 'speaker'][['object']].values[0][0]
            utterance = event_df[event_df['predicate'] == 'utterance'][['object']].values[0][0]
            print("  %s spoke %s" % (speaker, utterance))

    def explain_events(self, events: List, add_facts: List = None) -> None:
        last_direction = None
        last_direction_event = None
        user = "user"
        for event in events:
            self.explain_event(event, add_facts)
            for fact in event.facts:
                if fact.predicate == 'direction':
                    current_direction = fact.object
                    current_event = event
                    if last_direction != current_direction and last_direction is not None:
                        print("  %s THEN %s"%(last_direction, current_direction))
                    last_direction = current_direction
                    last_direction_event = event
                elif fact.predicate == 'utterance':
                    print("  %s speaks, so %s may want help."%(user, user))


    def toFact(self, facts_df: pd.DataFrame) -> List[Fact]:
        all_facts = []
        for fact in facts_df['fact']:
            if fact is not None:
                tokens = fact.split(" ")
                if len(tokens) == 3:
                    [start, relation, end] = fact.split(" ")
                else:
                    end = tokens[-1]
                    relation = tokens[-2]
                    start = tokens[0] # This will have to be changed eventually 
                real_fact = Fact(start, relation, end)
                all_facts.append(real_fact)
        return all_facts

    def explain_labels(self, labels):
        df = pd.DataFrame()
        for label in labels:
            label_df = to_data_frame(self.explain_fact(Fact(label, 'isA', 'object')))
            print(label_df)
            df.append(make_df_from_fact_list(label_df))
        print(df)

def make_df_from_fact_list(facts):
    output = pd.DataFrame()
    for fact in facts:
        dict_fact = fact.__dict__
        output = output.append(dict_fact, ignore_index=True)
    return output
        

class SceneMonitor:
    def __init__(self, data, rules, snapshots):
        self.data = data
        self.rules = rules
        self.snapshots = snapshots

def translate(reason):
    return ""

def get_labels(data_dict):
    KEYWORD = 'category_name'
    ontology = data_dict[KEYWORD].split('.')
    print(ontology[-1])
    return [ontology[-1]]

def snapshotMonitor(labels, context=True):
    """
    For demo purposes
    """
    anchors = ['person', 'animal', 'object', 'place', 'plant']
    relations = ['AtLocation', 'LocatedNear'] 
    return snapshot_monitor(labels, anchors, relations, True, context)

def snapshot_monitor(labels, anchors, relations, isLabels=False, context=False):
    """Local reasonableness monitor in python

    There are two possibiltiies: 
    
    1) It's in a natural language sentence that needs to be
    translated into a conceptual primitive representation.  
    

    2) It's a mostly symbolic list of labels and descriptions that
    needs to be aggregated into commonsense.  The rules change this
    way.

    """
    if isinstance(labels, dict):
        symbols = get_labels(labels)
        judgement = True 
        explanation = "Fits constructs"
    else:
        symbols = labels
        facts = add_commonsense(symbols, anchors, relations, isLabels) # what are labels?
        logging.debug("Snapshot monitor made with the following data: %s"%facts)
        monitor = SnapshotMonitor(symbols, facts, [], "vision system")

        # Forward chain
        # TODO: Prove automatically
        (judgement, explanation) = monitor.test_reasonable_snapshot(facts, symbols, context)

    # Check for alternatives / near misses in the data
    # Set explanation and judgement 

    return (judgement, explanation)

def monitor_over_time(symbols, anchors, relations, labels=False):
    """Local reasonableness monitor in python

    There are two possibiltiies: 
    
    1) It's in a natural language sentence that needs to be
    translated into a conceptual primitive representation.  
    

    2) It's a mostly symbolic list of labels and descriptions that
    needs to be aggregated into commonsense.  The rules change this
    way.

    """
    data = add_commonsense(symbols, labels)
    logging.debug(data)

    # Rules: Do some pyke/prolog stuff
    # Forward chain
    facts = data # forward chain
    # TODO: Prove automatically
    test_reasonable(facts)
    

    # Check for alternatives / near misses in the data
    # Set explanation and judgement 

    return (judgment, explanation)

def isMeaningful(data):
    """
    Checks for repeats
    """
    if 'self' not in data:
        return True
    else: return False 

def supplement(rules, data, reason="No reason given"):
    """
    This adds other forward-chained rules to the system
    A particular reason should be associated with those rules
    """
    facts = data['fact']
    logging.debug(facts)
    
    fact_data = facts.values.tolist()
    logging.debug(fact_data)
    
    big_list = forward_chain(rules, fact_data)

    if len(big_list) > len(fact_data):
        new_facts = big_list[len(fact_data)::]
        for new_fact in new_facts:
            if isMeaningful(new_fact):
                row_df = pd.DataFrame({'fact': [new_fact], 'reason':[reason]})
                data = data.append(row_df, ignore_index = True)
    return data
    
def isReasonable(data, labels):
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
    if not same_anchor(labels, data):
        explanation.append("labels are different anchors: %s"%anchor_summary())
        reasonable = False
#    else:
#        explanation.append("labels are the same anchor of type %s"%anchor_summary())

    # check same location
    if not same_location(labels, data):
        if check_alternatives(labels, data):
            explanation.append("%s located at the same location")
#            %s"%(label_summary(labels), location_summary()))
        else:
            explanation.append("labels are not at the same location")
            reasonable = False
    else:
        explanation.append("%s located at the same location of %s"
                           %(label_summary(labels), location_summary()))

    # check same size
    if not same_size(labels, data):
        explanation.append("labels are of different size: %s"%size_summary(labels))
        reasonable = False
    else:
        explanation.append(size_summary(labels))
    return (reasonable, explanation)

def same_anchor(labels, data):
    return is_consistent(labels, data, "consistent")

def same_location(labels, data):
    return is_consistent(labels, data, "sameLocation")

def same_size(labels, data):
    """
    NOT IMPLEMENTED YET
    """
    return False

def label_summary(labels):
    return ', '.join(str(x) for x in labels)

def check_alternatives(labels, data):
    return is_consistent_object(labels, data, "sameLocation")

def anchor_summary():
    return ""

def location_summary():
    return ""

def size_summary(labels):
    return "No commonsense supporting the similarity \
    between %s"%label_summary(labels)

def is_consistent(symbols, data, relation):
    facts = list(data['fact'])
    if type(symbols) is not list:
        labels = list(symbols)
    else: labels = symbols

    logging.debug(labels)
    logging.debug(facts)
    first_label = labels[0]

    for label in labels[1::]:
        one_way =  "%s %s %s"%(first_label, relation, label)
        reverse = "%s %s %s"%(label, relation, first_label)

        if not one_way in facts and not reverse in facts:
            logging.debug("not met %s"%one_way)
            return False
    return True

def near_miss():
    return False

def near_miss_summary():
    return ""

def is_consistent_object(symbols, data, relation):
    """
    Objects are not well populated, so this is an alternative case.
    """
    facts = list(data['fact'])
    if type(symbols) is not list:
        labels = list(symbols)
    else: labels = symbols

    logging.debug(labels)
    logging.debug(facts)
    first_label = labels[0]

    for label in labels[1::]:
        one_way =  "%s %s %s"%(first_label, relation, label)
        reverse = "%s %s %s"%(label, relation, first_label)

        if not one_way in facts and not reverse in facts:
            if 'object' in str(label) or 'object' in str(first_label):
                logging.debug("not met %s, but it's an object so it's ok"%one_way)
            else:
                return False
    return True

def test_reasonable(facts):
    engine.reset()
    
    for fact in facts['fact']:
        engine.add_universal_fact(fact)
        print(fact)

    engine.activate('reasonable')
    reasonable_goal = goal.compile('reasonable(facts)')
    
    #def fc_test(person1 = 'bruce'):
    """
    This function runs the forward-chaining for reasonabilit
    (reasonable.krb).
    """
    engine.reset()      # Allows us to run tests multiple times.
    
    start_time = time.time()
    engine.activate('reasonable.krb')  # Runs all applicable forward-chaining rules. 
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    logging.debug("doing proof")
    # How to input with a facts file 
    with fc_goal.prove(engine, person1=person1) as gen:
        for vars, plan in gen:
            print("%s, %s are %s") % \
                    (person1, vars['person2'], vars['relationship'])
    prove_time = time.time() - fc_end_time
    logging.debug("done proving reasonability")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec") % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time)


def add_single_commonsense(symbols, anchors, relations, labels=False):
    """
    This method adds commonsense information for a particular concept

    TODO: find the base concept 

    1.  Adds the anchor point information
    2.  Adds the important symbolic relations 
    """
    reasons = []
    if type(symbols) is not list:
        return add_single_commonsense(symbols, anchors, relations, labels=False)
    #1: Anchoring
    for sym in symbols:
        concept = str(sym)
        anchor = self.kb.find_anchor(concept, anchors)
        reasons.append(anchor)
        print("REASONS ARE %s"%reasons)

    #2: Adding commonsense for the relations of interest
    if labels:
        # Then this is a sort of description
        for concept in symbols:
            logging.debug("Accessing KB for this concept: %s" %concept)
            reasons += self.kb.aggregate(concept, relations)
    else:
        if has_verb(symbols):
        # Represent in conceptual primitives
            return "Not implemented yet"

    print("REASONS ARE %s"%reasons)
    logging.debug(reasons)
    data = pd.DataFrame(reasons, columns = ['fact', 'reason'])  
    return data

# is there anything similar between vision concepts
# This is thedefinition of a near miss
def similar(concepts):
    # is there an edge between (all) concepts 
    # check conceptnet
    reasons = []
    return (False, reasons)

def has_verb(symbols):
    """Checks whether the input contains a verb or not If the input
    contains a verb, then it should be appropriately parsed into a
    combination of conceptual primitives.

    Returns boolean: True if contains a verb, otherwise false

    """
    # 1.  Construct into a sentence
    # 2.  Parse on verb?
    # 3.  If has verb, construct into a primitive representation 
    return False 
