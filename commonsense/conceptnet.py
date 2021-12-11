from dataclasses import dataclass
import requests
import logging
import pandas as pd
import queue
import re
from itertools import *
from typing import List
from commonsense.kb import *
from commonsense.logical_classes import Fact, to_data_frame, default_fact

query_prefix_old = 'http://api.conceptnet.io/c/en/'
query_prefix_older = 'http://api.conceptnet.io/query?node=/c/en/'
query_prefix = 'http://api.conceptnet.io/c/en/'
rel_term = '?rel=/r/'
limit_suffix = '&limit=1000'

isA_search = '?rel=/r/IsA&limit=1000'
# default_anchor = 'object'
limit = 20
MAX_DEPTH = 3

# TODO - this should exist elsewhere
subject_anchors = ['animal', 'object', 'place', 'plant']
verb_anchor = ['move', 'propel']
REASON = "ConceptNet"
DEFAULT_RELATIONS = ['AtLocation', 'LocatedNear']

get_relation = lambda x: x['rel']['label']
get_start = lambda x: x['start']['label']
get_end = lambda x: x['end']['label']
get_score = lambda x: x['weight']

# Might want to move to logical classes
def make_fact_from_edge(edge: dict) -> Fact:
    return Fact(get_start(edge), get_relation(edge), get_end(edge), get_score(edge))

class ConceptNet(KB):
    """
    TODO: Possibly add an argument for local or online
      1.  URL for testing
      2.  LIVE URL 
    """
    def search_for_concept(self, predicate, concept, source):
        print(f"Searching for predicate: {predicate} and concept:{concept}")
        return self.search(concept, predicate, source)

    def find_closest_anchor(self, concept_phrase, anchors, include_score: bool=False):
        return self.find_anchor(concept_phrase, anchors, include_score)

    # def find_anchor(self, concept_phrase, anchors, include_score: bool):
    #     """"""
    #     self.find_anchor(concept_phrase, anchors, include_score)
        #
        # self.find_anchor_hops(concept_phrase, anchors, include_score)
        
    # Everything is a string
    # Relation: symbolic ==> Single Phrase
    # Concepts can be Multiple Words
    def search(self, concept, relation, reason=None) -> List[Fact]:
        """
        Searches for a particular concept in ConceptNet

        :param concept: The concept to search for
        :type concept: str
        :param relation: The specific relation or predicate to search for
        :type relation: str
        :param reason: A reason to add to each fact that is aggregated
        :type reason: str
        :return: A list of facts for the starter concept for a particular relation
        :rtype: List
        """
        logging.debug("searching for an anchor point for %s" % concept)

        new_facts = []
        word_text = concept.replace(" ", "_").lower()
        obj = requests.get(query_prefix + word_text + '?rel=/r/' + relation +
                           '&limit=1000').json()
        edges = obj['edges']
        for edge in edges:
            if edge['rel']['label'] == relation:  # this will have to be changed
                end = edge['end']['label'].lower()
                start = edge['start']['label'].lower()
                new_fact = Fact(start, relation, end, reason=reason)
                new_facts.append(new_fact)
        return new_facts

    def search_all(self, concept, reason=None) -> List[Fact]:
        """
        Searches for a particular concept in ConceptNet

        :param concept: The concept to search for
        :type concept: str
        :param relation: The specific relation or predicate to search for
        :type relation: str
        :param reason: A reason to add to each fact that is aggregated
        :type reason: str
        :return: A list of facts for the starter concept for a particular relation
        :rtype: List
        """
        new_facts = []
        word_text = concept.replace(" ", "_").lower()
        obj = requests.get(query_prefix + word_text +
                           '&limit=1000').json()
        edges = obj['edges']
        for edge in edges:
            relation = edge['rel']['label']
            end = edge['end']['label'].lower()
            start = edge['start']['label'].lower()
            new_fact = Fact(start, relation, end, reason=reason)
            new_facts.append(new_fact)
        return new_facts

    def search_with_score(self, concept: str, relations: List, num_hops: int = 1) -> List:
        """
        Searches for specific concepts in conceptNet with an added score.
        Returns a list of facts
        """
        facts = []
        for relation in relations:
            logging.debug(f"searching for {concept} and relation {relation} with a score")
            word_text = concept.replace(" ", "_").lower()
            query = query_prefix + word_text + '?rel=' + relation + '&limit=1000'
            obj = requests.get(query).json()
        
            edges = obj['edges']
            for edge in edges:
                if get_relation(edge) == relation:
                    facts.append(self.extract_data(edge))
        return facts

    def extract_data(self, edge: dict) -> List:
        """
        Returns json data in a list format."""    
        return make_fact_from_edge(edge).to_infix_flat_list()
#return make_fact_from_edge(edge).to_list() 

    def get_domain(facts: pd.DataFrame) -> str:
        """
        Returns the best domain for the facts.  Right now, it returns the highest scoring 'AtLocation' fact
        """
        return facts.sort_values(by=['Score'], ascending=False).iloc[0]['Word2']
        # return facts[facts['Relation']=='AtLocation'].max()['Word2']

    # Facts are lists: A fact, last term is the reason, easily added to pandas this way
    # Some things returned as tuples
    # Clean is string manipulation
    # Triple is a RDF fact from concept net
    # Reason is a string phrase
    # def make_fact(self, triple, reason):
    #     """
    #     Makes a basic data fact base in pandas data
    #     """
    #     logging.debug("Making a new fact: %s with reason: %s" % (triple, reason))
    #     [subject, predicate, obj] = triple
    #     fact_term = "%s %s %s" % (subject, predicate, self.clean_phrase(obj))
    #     return [fact_term, reason]


    def build_df(self, concepts: List, relations: List = DEFAULT_RELATIONS) -> pd.DataFrame:
        """"
        Makes a data frame of facts from conceptNet for a list of concepts
        """
        facts = self.build_facts(concepts, relations)
        return to_data_frame(facts)
        # return pd.DataFrame([vars(fact) for fact in facts]) # This is the key

    def build_facts(self, concepts: List, relations: List = DEFAULT_RELATIONS, reason: str = "", include_anchor = True) -> List[Fact]:
        """
        Makes a list of facts for a list of concepts.
        Heelper method for build_df
        :param concepts:
        :type concepts: List[str]
        :param relations:
        :type relations:
        :return:
        :rtype:
        """
        facts = []
        reason_str = reason if reason != "" else "ConceptNet search"
        for concept in concepts:
            if include_anchor:
                facts.append(self.find_anchor(concept, subject_anchors, True))
            # facts.extend(self.search_all(concept, reason=reason_str))
            for relation in relations:
                facts.extend(self.search(concept, relation, reason=reason_str))
        return facts

    def clean(self, description):
        """
        Strips a description and removes spaces, stop words, etc
        TODO: Remove POS tagging and stuff.
        """
        # remove "the" and "a" or "an"
        cleaned = description
        starters = ['a ', 'the ', 'an ', 'and ']
        for starter in starters:
            if description.startswith(starter):
                cleaned = description.replace(starter, '')
        return cleaned.replace(' ', '_')


    def make_prolog_fact(self, triple, reason):
        """
        Makes facts in the prolog style
        """
        [subject, predicate, obj] = triple
        fact_term = "%s(%s, %s)" % (predicate, subject, obj)
        logging.debug("Making a new prolog style fact:%s" % fact_term)
        return [fact_term, reason]


    def find_anchor(self, concept_phrase, anchors, include_score: bool = False) -> Fact:
        """
        Finds the anchor point (from a list of anchors) and returns a Fact of that anchor point as
        Fact(concept_phrase, 'IsA', anchor_point)

        :param concept_phrase: The phrase (or concept) to find an anchor point for
        :type concept_phrase: str
        :param anchors: the list of anchor points
        :type anchors: List
        :param include_score: whether to include the score or not
        :type include_score: bool
        :return: A fact with an IsA relation of the chosen anchor point
        :rtype: Fact
        """
        logging.debug("searching for an anchor point for %s" % concept_phrase)

        for anchor in anchors:
            if anchor in concept_phrase:
                logging.debug("anchor point %s is partof the concept phrase: %s"
                              % (anchor, concept_phrase))
                return Fact(concept_phrase, 'IsA', anchor, "direct search")

        for anchor in anchors:
            if type(concept_phrase) is list:
                concept = concept_phrase[-1]
            else:
                concept = concept_phrase
            return self.get_closest_anchor(concept, anchors, 'IsA')


    ########### Is this how we want the cleaning ###########################
    def clean(self, symbolic_phrase):
        """
        Helper function for cleaning the symbols.

        May be unnecessary if instead focused on strings.
        """
        str_phrase = str(symbolic_phrase).split(' ') #Splitting along the spaces allows proper access to the primary term
        if type(str_phrase) is list:
            return str_phrase[0] #changed this from last term to first term in the string to properly do the aggregation
        else:
            return str_phrase


    def build_relation(self, phrase, relation):
        facts = []

        concept = phrase  # Might want to get the last one, not so sure right now.
        obj = requests.get(query_prefix + concept + rel_term + relation).json()
        edges = obj['edges']
        for edge in edges:
            if edge['rel']['label'] == relation:
                fact = edge['end']['label'].lower()
                new_fact = Fact(phrase, relation, fact, reason="ConceptNet")
                if new_fact not in facts:
                    facts.append(new_fact)
        return facts
    

    def get_closest_anchor(self, concept, anchors, relation='IsA', include_score: bool = False) -> Fact:
        """
        Goes through all the relations and tries to find the closest one.

        :param concept: The concept to search for
        :type concept: str
        :param anchors: A list of possible anchor points
        :type anchors: List
        :param relation: The relation or predicate to use for searching the hierarchy
        :type relation: str
        :param include_score: Whether to include the score from ConceptNet (or not)
        :type include_score: bool
        :return: A fact with the relation/predicate as chosen: Fact(concept, relation, anchor_point)
        :rtype: Fact
        """
        """
        If the anchor point is in the isA hierarchy at all, it
        """
        for anchor in anchors:
            logging.debug("Searching for an IsA link between %s and %s" % (concept, anchor))

            obj = requests.get(query_prefix + concept + rel_term + 'IsA' + limit_suffix).json()
            edges = obj['edges']
            if edges:
                for edge in edges:
                    if self.check_IsA_relation(anchor, edge, concept):
                        score = get_score(edge) if include_score else 1.0
                        return Fact(concept, 'IsA', anchor, reason="ConceptNet IsA link", score=score)
            else:
                print(f"IsA relation not found between concept: {concept} and anchors.")
                return default_fact(concept, include_score)
        # If it is never found, make default object
        return default_fact(concept, include_score)

    def find_anchor_point(self, concept, anchors, relation='IsA', include_score: bool = False):
        """
        Goes through all the relations and tries to find the closest one.
        If the anchor point is in the isA hierarchy at all, it
        Currently, this only looks for it within ONE hop.
        TODO: Find the shortest hops
        """
        for anchor in anchors:
            logging.debug("Searching for an IsA link between %s and %s" % (concept, anchor))

            obj = requests.get(query_prefix + concept + rel_term + 'IsA' + limit_suffix).json()
            edges = obj['edges']
            if edges:
                for edge in edges:
                    if self.check_IsA_relation(anchor, edge, concept):
                        return anchor
                # return highest score
            else:
                print("IsA relation not found between concept and anchors")
                return "object"
        # If it is never found, make default object
        return "object"

    def find_anchor_point_hops(self, concept, anchors, relation='IsA', include_score: bool = False):
        """
        Goes through all the relations and tries to find the closest one.
        If the anchor point is in the isA hierarchy at all, it
        Currently, this only looks for it within ONE hop.
        TODO: Find the shortest hops
        """
        for anchor in anchors:
            logging.debug("Searching for an IsA link between %s and %s" % (concept, anchor))

            obj = requests.get(query_prefix + concept + rel_term + 'IsA' + limit_suffix).json()
            edges = obj['edges']
            if edges:
                for edge in edges:
                    if self.check_IsA_relation(anchor, edge, concept):
                        return anchor
                # return highest score
            else:
                print("IsA relation not found between concept and anchors")
                for edge in edges:
                    self.find_anchor_point_hops(edge, anchors)
                # return "object"
        # If it is never found, make default object
        return "object"
    

    # def default_fact(self, concept, include_score: bool = False) -> Fact:
    #     """
    #     Returns a fact of is to the default anchor.
    #     TODO: We might want to move this to the logical classes?
    #     """
    #     return Fact(concept, 'IsA', default_anchor, "Default anchor point")
        # triple = [concept, 'IsA', default_anchor]
        # if include_score:
        #     return triple
        # else:
        #     return self.make_fact(triple, "Default anchor point")

    def check_IsA_relation(self, anchor, edge, concept=None):
        if edge['rel']['label'] == 'IsA':
            result = edge['end']['label']
            if anchor in result:
                return True
        return False


    def clean_concept(self,word):
        """
        Remove dashes into a phrase
        """
        if "-" in word:
            phrase = word.split("-")
            return phrase
        else:
            return word.lower()


    # Counts the amount of IsA hops from a start to an anchor point
    # This should be a shortest path algorithm

    def get_shortest_hops(self, start, relation='IsA'):
        shortest = None
        target = None
        for anchor in subject_anchors:  # Will want to toggle for verb
            candidate = self.find_shortest_path(start, anchor, relation)
            try:
                if candidate and not shortest or len(candidate) < len(shortest):
                    shortest = candidate
                    target = anchor
            except TypeError:
                continue
        return (target, shortest)


    # Finds the shortest path for a specificed relation

    def find_shortest_path(self, start, anchor, relation='IsA', path=None):
        """
        """
        if path == None:
            path = []
        path = path + [start]
        if self.has_IsA_edge(start, anchor):
            return path + [anchor]
        if len(path) >= MAX_DEPTH:
            return None
        shortest = None
        search = self.clean_search(start)
        obj = requests.get(query_prefix + search + isA_search).json()
        edges = obj['edges']

        for edge in edges:
            from_node = self.clean_search(edge['start']['label'])
            to_node = self.clean_search(edge['end']['label'])
            rel = edge['rel']['label']

            # May need more processing
            if (self.search_equals(from_node, search) and rel == relation):
                if to_node not in path:
                    newpath = self.find_shortest_path(to_node, anchor, relation, path)
                    if newpath:
                        if not shortest or len(newpath) < len(shortest):
                            shortest = newpath
        return shortest



    def search_equals(self, string1, string2):
        """"""
        if (self.clean_search(string1) == self.clean_search(string2)):
            return True
        return False

    def clean_search(self, input):
        cleaned = input.lower()
        if (cleaned.startswith("a ")):
            cleaned = cleaned.replace("a ", "", 1)
        elif (cleaned.startswith("an ")):
            cleaned = cleaned.replace("an ", "", 1)
        return cleaned.replace(" ", "_").lower()

    def connected(self, labels):
        for (start,end) in combinations(labels,2):
            x = str(start)
            y = str(end)
            if self.has_any_edge(x,y):
                continue
            else:
                print("found no direct edge between %s and %s"%(x,y))
                if x == 'man' or y == 'man' or x == 'motorcycle' or y=='motorcycle': # Checking for the person anchor point
                    print("found anchor point")
                    continue
                else:
                    return False
        return True

    # Checks if there is any correlation (just an edge)
    #
    # Only to be used
    # for verb primitives, otherwise not strong enough correlation
    def has_any_edge(self, word, verb_primitive, verbose=False):
        word_text = word.replace(" ", "_").lower()
        logging.debug("ConceptNet Query: Searching for an edge between %s and the verb primitive %s"
                      % (word, verb_primitive))
        obj = requests.get('http://api.conceptnet.io/query?node=/c/en/' + word_text + \
                           '&other=/c/en/' + verb_primitive).json()
        edges = obj['edges']
        if (edges):
            logging.debug("Edges found between %s and the verb primitive %s"
                          % (word, verb_primitive))
            return True
        else:
            logging.debug("No edge found between %s and the verb primitive %s"
                          % (word, verb_primitive))
            logging.debug("Going to search for the next the verb primitive")
            return False


    # First check if there is a direct connection via an IsA relation

    def has_IsA_edge(self, word, concept, verbose=False):
        word_text = word.replace(" ", "_").lower()

        obj = requests.get(query_prefix + word_text + '?rel=/r/IsA&limit=1000').json()
        edges = obj['edges']
        logging.debug("ConceptNet Query: Searching for an IsA relation between %s and the anchor point %s"
                      % (word, concept))
        for edge in edges:
            start = edge['start']['label'].lower()
            end = edge['end']['label'].lower()

            if (self.search_equals(word, start) and self.isA_equals(concept, end.lower())):
                logging.debug("IsA relation found; %s bound to the anchor point %s"
                              % (word, concept))
                return True
        logging.debug("No IsA relation found.")
        return False


    def has_edge(self, word, concept, relation):
        word_text = word.replace(" ", "_").lower()

        obj = requests.get(query_prefix + word_text + '?rel=/r/' + relation + '&limit=1000').json()
        edges = obj['edges']
        for edge in edges:
            start = edge['start']['label'].lower()
            end = edge['end']['label'].lower()

            if (self.search_equals(word, start) and self.isA_equals(concept, end.lower())):  # == concept.lower()):
                return True
        return False


    # Phrases don't always count

    def isA_equals(self, concept, phrase):
        if concept in phrase:
            return True
        else:
            return False



    def containsConcept(self, concept, list):
        for item in list:
            if concept in item[0]:
                return item[0]
        return False


    # TODO - something strange about the query request
    # So hard-coded in a check for the relation

    def search_relation(self, word, relation):
        concepts = []
        word_text = word.replace(" ", "_").lower()
        obj = requests.get(query_prefix + word_text + '?rel=/r/' + relation +
                           '&limit=1000').json()
        edges = obj['edges']
        for edge in edges:
            if edge['rel']['label'] == relation:
                end = edge['end']['label'].lower()
                concepts.append(end)
        return concepts


    # TODO fix this to not be hardcoded
    # A force that can move things
    def isConfusion(self, item):
        confusions = ['hurricane', 'storm', 'earthquake']
        if item in confusions:
            return True
        else:
            return False


    # Added for the new primitives
    def can_move(self,subject):
        if self.has_IsA_edge(subject, 'vehicle') or self.has_IsA_edge(subject, 'animal'):
            return True
        else:
            return False



    # Assume this is a list for now
    def can_propel(self,contexts):
        for context in contexts:
            if self.isConfusion(context):
                return True
        return False

    def explain_location(self, concepts: List, df: pd.DataFrame) -> str:
        """
        This a new explain function for demonstration purposes.  It will be moved to the monitor eventually.
        :param concepts: the set of concepts to search for
        :type concepts: List
        :param df: the dataframe of facts
        :type df: pd.Dataframe
        :return: A string of the explanation
        :rtype: str
        """
        bad_ones = []
        location = df[df['predicate'] == 'AtLocation']['object'].value_counts().idxmax()

        # We assume that the concepts are aggregated in order. (by score).

        for concept in concepts[1::]:
            # get the highest AtLocation from the dataframe
            locations = df[(df['predicate'] == 'AtLocation') & (df['subject'] == concept)]
            if locations.empty:
                locations = df[(df['predicate'] == 'AtLocation') & (df['subject'] == "a "+concept)]
            # print(locations)
            if locations.empty:
                bad_ones.append(concept)
        return f"All concepts share a common location of {location} except for {bad_ones}.  " \
               f"These concepts are unreasonble."

    def explain_location_by_rank(self, concepts: List) -> str:
        """
        This a new explain function for finding the best location in order.
        It counts the number of times it gets such a location.
        This will be moved to the monitor eventually.
        :param concepts: the set of concepts to search.  We assume that their scores are in order
        :type concepts: List
        :return: A string of the explanation
        :rtype: str
        """
        bad_ones = []
        concept = concepts[0]  # This highest ranked one
        # df = self.build_df([concept])
        all_facts = self.build_facts([concept], reason=concept)
        intersection = all_facts
        unique_locations = set([fact.object for fact in all_facts if fact.predicate=='AtLocation'])
        # unique_location_facts = [Fact(concept, 'AtLocation', fact.object, reason=concept, count=1) for fact in unique_locations]

        for concept in concepts[1::]:
            facts = self.build_facts([concept], reason=concept)
            intersection = self.fact_intersection(facts, intersection, concept, relation='AtLocation')

            print(f"After {concept}")
            if intersection is None:
                print(f"No common location found for {concept}")
            else:
                intersections = to_data_frame(intersection)
                print(intersections)



        #     # get the highest AtLocation from the dataframe
        #     locations = df[(df['predicate'] == 'AtLocation') & (df['subject'] == concept)]
        #     if locations.empty:
        #         locations = df[(df['predicate'] == 'AtLocation') & (df['subject'] == "a "+concept)]
        #     # print(locations)
        #     if locations.empty:
        #         bad_ones.append(concept)
        # return f"All concepts share a common location of {location} except for {bad_ones}.  " \
        #        f"These concepts are unreasonble."

    def fact_intersection(self, base_facts: List, new_facts: List, concept: str, relation:str = "") -> List:
        """
        Finds the intersection of two lists of facts.  It will filter on a relation if it's given.

        :param base_facts: The base list of facts
        :type base_facts: List[Fact]
        :param new_facts: The second list of facts
        :type new_facts: List[Fact]
        :param concept: The starter concept (for the explanation).
        :type concept: str
        :param relation: The relation to check for
        :type relation: str
        :return: A list of the intersection
        :rtype: str
        """
        intersection = []
        for fact in new_facts:
            for prev_fact in base_facts:
                if fact == prev_fact:
                    logging.debug(f"Does this ever happen with {fact}")
                    new_fact = Fact(fact.subject, fact.predicate, fact.object,
                                    reason=f"{prev_fact.reason}, {concept}",
                                    score=prev_fact.score + fact.score,
                                    count=prev_fact.count + 1)
                    if relation != "" and fact.predicate == relation:
                        intersection.append(new_fact)
                    elif relation == "":
                        intersection.append(new_fact)
        return intersection
