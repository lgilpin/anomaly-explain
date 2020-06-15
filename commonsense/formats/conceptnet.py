import requests
import logging as log
import queue

query_prefix = 'http://api.conceptnet.io/c/en/'
isA_search = '?rel=/r/IsA&limit=1000'
limit = 20
MAX_DEPTH = 3

# TODO - this should exist elsewhere
subject_anchors = ['animal', 'object', 'place', 'plant']
verb_anchor = ['move', 'propel']

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
    log.debug("ConceptNet Query: Searching for an edge between %s and the verb primitive %s" 
              %(word,verb_primitive))
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word_text+\
                           '&other=/c/en/'+verb_primitive).json()
    edges = obj['edges']
    if(edges):
        log.debug("Edges found between %s and the verb primitive %s" 
                  %(word,verb_primitive))
        return True
    else:
        log.debug("No edge found between %s and the verb primitive %s"
                  %(word,verb_primitive))
        log.debug("Going to search for the next the verb primitive")
        return False

# First check if there is a direct connection via an IsA relation
# TODO - This needs to be rigorously checked
def has_IsA_edge(word, concept, verbose=False):
    word_text = word.replace(" ", "_").lower()

    obj = requests.get(query_prefix+word_text+'?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    log.debug("ConceptNet Query: Searching for an IsA relation between %s and the anchor point %s"
              %(word,concept))
    for edge in edges:
        start = edge['start']['label'].lower()
        end = edge['end']['label'].lower()

        if(search_equals(word, start) and isA_equals(concept, end.lower())):
            log.debug("IsA relation found; %s bound to the anchor point %s"
                          %(word,concept))
            return True
    log.debug("No IsA relation found.")
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
