import requests
import logging
import queue
import re

query_prefix_old = 'http://api.conceptnet.io/c/en/'
query_prefix_older = 'http://api.conceptnet.io/query?node=/c/en/'
query_prefix = 'http://api.conceptnet.io/c/en/'
rel_term = '?rel=/r/'
limit_suffix = '&limit=1000'

isA_search = '?rel=/r/IsA&limit=1000'
default_anchor = 'object'
limit = 20
MAX_DEPTH = 3

# TODO - this should exist elsewhere
subject_anchors = ['animal', 'object', 'place', 'plant']
verb_anchor = ['move', 'propel']
REASON = "ConceptNet" 

def search(concept, relation, reasons=None):
    """
    Search for a specific relation in the knowledge base

    Aggregates 
    """
    logging.debug("searching for an anchor point for %s"%concept)
    
    concepts = []
    word_text = concept.replace(" ", "_").lower()
    obj = requests.get(query_prefix+word_text+'?rel='+relation+
                       '&limit=100').json()
    edges = obj['edges']
    for edge in edges:
        if edge['rel']['label'] == relation: # this will have to be changed 
            end = edge['end']['label'].lower()
            concepts.append(end)
    return concepts

def make_fact(triple, reason):
    """
    Makes a basic data fact base in pandas data
    """
    logging.debug("Making a new fact: %s with reason: %s"%(triple, reason))
    [subject, predicate, obj] = triple
    fact_term = "%s %s %s"%(subject, predicate, clean_phrase(obj))
    return [fact_term, reason]

def clean_phrase(description):
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

def make_prolog_fact(triple, reason):
    """
    Makes facts in the prolog style
    """
    [subject, predicate, obj] = triple
    fact_term = "%s(%s, %s)"%(predicate, subject, obj)
    logging.debug("Making a new prolog style fact:%s"%fact_term)
    return [fact_term, reason]

def find_anchor(concept_phrase, anchors):
    """
    Search for a specific anchor from a set of anchors
    """
    logging.debug("searching for an anchor point for %s"%concept_phrase)

    for anchor in anchors:
        if anchor in concept_phrase:
            logging.debug("anchor point %s is partof the concept phrase: %s"
                          %(anchor, concept_phrase))
            triple = [concept_phrase, 'IsA', anchor]
            return make_fact(triple, "direct search")

    for anchor in anchors:
        if type(concept_phrase) is list:
            concept = concept_phrase[-1]
        else: concept = concept_phrase
        return get_closest_anchor(concept, 'IsA', anchors)

def aggregate(fact, relations):
    """
    Aggregates a commonsense reasons for a particular concept and the relations of interest 
    """
    all_facts = []
    for relation in relations:
        concept_phrase = clean(fact)
        new_facts = build_relation(concept_phrase, relation)
        all_facts += new_facts
    return all_facts

def clean(symbolic_phrase):
    """
    Helper function for cleaning the symbols.

    May be unnecessary if instead focused on strings. 
    """
    str_phrase = str(symbolic_phrase).split('_')
    if type(str_phrase) is list:
        return str_phrase[-1]
    else: return str_phrase

def build_relation(phrase, relation):
    facts = []

    concept = phrase # Might want to get the last one, not so sure right now. 
    obj = requests.get(query_prefix+concept+rel_term+relation).json()
    edges = obj['edges']
    for edge in edges:
        if edge['rel']['label'] == relation:
            fact = edge['end']['label'].lower()
            new_fact = make_fact([phrase, relation, fact], "ConceptNet")
            if new_fact not in facts:
                facts.append(new_fact)
    return facts

def get_closest_anchor(concept, relation, anchors):
    """
    Goes through all the relations and tries to find the closest one.
    If the anchor point is in the isA hierarchy at all, it 
    """
    print("are we in the closest")
    for anchor in anchors:
        logging.debug("Searching for an IsA link between %s and %s"%(concept,anchor))

        obj = requests.get(query_prefix+concept+rel_term+'IsA'+limit_suffix).json()  
        edges = obj['edges']
        if edges:
            for edge in edges:
                if check_IsA_relation(concept,anchor,edge):
                    triple = [concept, 'IsA', anchor]
                    return make_fact(triple, "ConceptNet IsA link")
        else:
            return "not found" # TODO this needs a better message
    # If it is never found, make default object
    triple = [concept, 'IsA', default_anchor]
    return make_fact(triple, "Default anchor point")

def check_IsA_relation(concept,anchor, edge):
    if edge['rel']['label'] == 'IsA':
        result = edge['end']['label']
        if anchor in result:
            return True
    return False

def clean_concept(word):
    """
    Remove dashes into a phrase 
    """
    if "-" in word:
        phrase = word.split("-")
        return phrase
    else: return word.lower()

# Counts the amount of IsA hops from a start to an anchor point
# This should be a shortest path algorithm
def get_shortest_hops(start, relation='IsA'):
    shortest = None
    target = None
    for anchor in subject_anchors: # Will want to toggle for verb
        candidate = find_shortest_path(start, anchor, relation)
        try:
            if candidate and not shortest or len(candidate) < len(shortest):
                shortest = candidate
                target = anchor
        except TypeError:
            continue
    return (target, shortest)

# Finds the shortest path for a specificed relation
def find_shortest_path(start, anchor, relation='IsA', path=None):
    if path==None:
        path = []
    path = path + [start]
    if has_IsA_edge(start, anchor):
        return path + [anchor]
    if len(path) >= MAX_DEPTH:
        return None
    shortest = None
    search = clean_search(start)
    obj = requests.get(query_prefix+search+isA_search).json()
    edges = obj['edges']
    
    for edge in edges:
        from_node = clean_search(edge['start']['label'])
        to_node = clean_search(edge['end']['label'])
        rel = edge['rel']['label']
        
        # May need more processing
        if(search_equals(from_node, search) and rel == relation):
            if to_node not in path:
                newpath = find_shortest_path(to_node, anchor, relation, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
    return shortest

def search_equals(string1, string2):
    if(clean_search(string1) == clean_search(string2)):
        return True
    return False

def clean_search(input):
    cleaned = input.lower()
    if(cleaned.startswith("a ")):
        cleaned = cleaned.replace("a ", "", 1)
    elif(cleaned.startswith("an ")):
        cleaned = cleaned.replace("an ", "", 1)           
    return cleaned.replace(" ", "_").lower()

# Checks if there is any correlation (just an edge)
# Only to be used for verb primitives, otherwise not strong enough correlation
def has_any_edge(word, verb_primitive, verbose=False):
    word_text = word.replace(" ", "_").lower()
    logging.debug("ConceptNet Query: Searching for an edge between %s and the verb primitive %s" 
              %(word,verb_primitive))
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word_text+\
                           '&other=/c/en/'+verb_primitive).json()
    edges = obj['edges']
    if(edges):
        logging.debug("Edges found between %s and the verb primitive %s" 
                  %(word,verb_primitive))
        return True
    else:
        logging.debug("No edge found between %s and the verb primitive %s"
                  %(word,verb_primitive))
        logging.debug("Going to search for the next the verb primitive")
        return False

# First check if there is a direct connection via an IsA relation
# TODO - This needs to be rigorously checked
def has_IsA_edge(word, concept, verbose=False):
    word_text = word.replace(" ", "_").lower()

    obj = requests.get(query_prefix+word_text+'?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    logging.debug("ConceptNet Query: Searching for an IsA relation between %s and the anchor point %s"
              %(word,concept))
    for edge in edges:
        start = edge['start']['label'].lower()
        end = edge['end']['label'].lower()

        if(search_equals(word, start) and isA_equals(concept, end.lower())):
            logging.debug("IsA relation found; %s bound to the anchor point %s"
                          %(word,concept))
            return True
    logging.debug("No IsA relation found.")
    return False

def has_edge(word, concept, relation):
    word_text = word.replace(" ", "_").lower()

    obj = requests.get(query_prefix+word_text+'?rel=/r/' + relation + '&limit=1000').json()
    edges = obj['edges']
    for edge in edges:
        start = edge['start']['label'].lower()
        end = edge['end']['label'].lower()

        if(search_equals(word, start) and isA_equals(concept, end.lower())):# == concept.lower()):
            return True
    return False

# Phrases don't always count
def isA_equals(concept, phrase):
    if concept in phrase:
        return True
    else: return False

def containsConcept(concept, list):
    for item in list:
        if concept in item[0]:
            return item[0]
    return False

# TODO - something strange about the query request
# So hard-coded in a check for the relation
def search_relation(word, relation):
    concepts = []
    word_text = word.replace(" ", "_").lower()
    obj = requests.get(query_prefix+word_text+'?rel=/r/'+relation+
                       '&limit=1000').json()
    edges = obj['edges']
    for edge in edges:
        if edge['rel']['label'] == relation:
            end = edge['end']['label'].lower()
            concepts.append(end)
    return concepts

# TODO fix this to not be hardcoded
# A force that can move things
def isConfusion(item):
    confusions = ['hurricane', 'storm', 'earthquake']
    if item in confusions:
        return True
    else: return False

# Added for the new primitives
def can_move(subject):
    if has_IsA_edge(subject, 'vehicle') or has_IsA_edge(subject, 'animal'): 
        return True
    else: return False

# Assume this is a list for now
def can_propel(contexts):
    for context in contexts:
        if isConfusion(context):
            return True
    return False
