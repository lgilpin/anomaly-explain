import requests
import logging as log

query_prefix = 'http://api.conceptnet.io/c/en/'

# Counts the amount of IsA hops from a start to an anchor point
def get_hops(start, anchor):
    if(has_IsA_edge(start, anchor)):
        return 1
    else:
        # get all IsA relations from start -> a 
        search = clean_search(start)
        log.debug("Now hooping through the IsA hiearchy for %s %s"%(search, anchor))
        obj = requests.get(query_prefix+search+'?rel=/r/IsA&limit=1000').json()
        edges = obj['edges']
        for edge in edges:
            from_node = clean_search(edge['start']['label'])
            to_node = clean_search(edge['end']['label'])
            rel = edge['rel']['label']
            # May need more processing
            if(search_equals(from_node, search) and rel == 'IsA'): # make sure its the right way
                node = (to_node, len(path))
                if node not in queue and node not in new_queue and \
                        not search_equals(node[0], start):
                    new_queue.append(node)
                    if len(new_queue) >=10:
                        break
            get_hops(edge, anchor) + 1

# TODO change from finding IsA path to any relation path
# Check with how this can work with ConceptNet
def find_IsA_path(start, end, path=None, queue=None, seen=None):
    if path is None:
        path = []
        path.append(clean_search(start))

    if queue is None:
        queue = []

    if seen is None:
        seen = []
        
    search = clean_search(start)
    log.debug("Now searching through the IsA hiearchy for %s %s"%(search, path))
    log.debug("We've seen %s"% seen)
    obj = requests.get(query_prefix+search+'?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    
    if(has_IsA_edge(start,end)):
        log.debug("Found an edge between and %s" %(start,end))
        path.append(end)
        return path
    else:
        new_queue = []
        if(start not in seen): # Might need more preprocessing
            for edge in edges:
                from_node = clean_search(edge['start']['label'])
                to_node = clean_search(edge['end']['label'])
                rel = edge['rel']['label']
                # May need more processing
                if(search_equals(from_node, search) and rel == 'IsA'): # make sure its the right way
                    node = (to_node, len(path))
                    if node not in queue and node not in new_queue and \
                            not search_equals(node[0], start):
                        new_queue.append(node)
                        if len(new_queue) >=10:
                            break
            seen.append(start)
        merged_queue = []
        merged_queue.extend(new_queue)
        merged_queue.extend(queue)
        log.debug("new queue is %s" %merged_queue)
        if merged_queue:
            node = merged_queue.pop(0)[0]
            if node not in path:
                if(len(path) < limit-1 ):
                    log.debug("recursing with %s" %node)
                    path.append(node)
                    newpath = find_IsA_path(node, end, path, merged_queue, seen)
                    return newpath
                else: # we've gone too far
                    if not (containsConcept(end, merged_queue)):
                        log.debug("We've gone too far")
                        path.pop()
                        node=path[-1]
                        newpath = find_IsA_path(node, end, path, 
                                                [(x,y) for (x,y) in merged_queue if y != 2],
                                                seen)
                        return newpath
                    else: 
                        path.append(end)
                        return path
    return None

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
