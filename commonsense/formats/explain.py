import requests
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from sympy import *
from ..anchor.anchors import * 
#from conceptnet5.db.query import AssertionFinder

def search_between(start, end, path=[]):
    path = path + [start]
    obj = requests.get('http://api.conceptnet.io/c/en/'+start+'?limit=10000').json()
    edges = obj['edges']
    if start == end:
        return path
    #if not graph.has_key(start):
    #    return None
    #for node in graph[start]:
    for edge in edges:
        node2 = edge['start']['label']
        node1 = edge['end']['label']
        if node1 == start:
            node = node2
        else:
            node = node1
        #print("looking though " + node + " had choice of :"+ node2 + " and "+node1)
        if node not in path:
            newpath = search_between(node, end, path)
            if newpath:
                return newpath
    return None

def search_shortest_between(start, end, path=[]):
    path = path + [start]
    obj = requests.get('http://api.conceptnet.io/c/en/'+start+'?limit=10000').json()
    edges = obj['edges']
    if start == end:
        return path
    #if not graph.has_key(start):
    #    return None
    #for node in graph[start]:
    shortest = None
    for edge in edges:
        node2 = edge['start']['label']
        node1 = edge['end']['label']
        if node1 == start:
            node = node2
        else:
            node = node1
        #print("looking though " + node + " had choice of :"+ node2 + " and "+node1)
        if node not in path:
            #if shortest and len(path) < len(shortest):
            newpath = search_shortest_between(node, end, path)
            if newpath:
                print(newpath)
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

# More generic function for detecting relationship
def isA(word, concept):
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word+'&other=/c/en/'+concept).json()
    edges = obj['edges']

    if(not edges):
        #print("going through the hiearchy to find "+concept)
        return find_hierarchy_path(word, concept)
    else: return (word, 'IsA', concept)

# Confusing conditions are enviornment
# Check for weather
# Judgement can be impaired 
def isConfusion(word):
    impairments = ['fog', 'smoke'] 
    if(word in impairments):
        return (word, 'IsA', 'confusion')
    else: # Check that it's in weather
        isA(word, 'weather')
    return 

# # Finds the specific anchor point or type of a specific word
# def find_anchor_point(word):
#     concepts = ['animal', 'plant', 'object', 'place']
#     for concept in concepts:
#         relation = isA(word, concept)

def find_hierarchy_path(start, end, count=0, path=[]):
    limit = 5 # May want to be global

    #cnfinder = AssertionFinder()
    #path = path + [start]
    #edges = cnfinder.query({'node': '/c/en/penguin', 'rel': '/r/IsA'})

    obj = requests.get('http://api.conceptnet.io/c/en/'+start+ \
                           '?rel=/r/IsA&limit=1000').json()
    edges = obj['edges']
    
    if start == end:
        return path
    shortest = None
    for edge in edges:
        node2 = edge['start']['label']
        node1 = edge['end']['label']
        #print(node2 + " " + node1)

        # Need to replace the spaces with _
        node2.replace(" ", "_") 
        node1.replace(" ", "_")
        if node1 == start:
            node = node2
        else:
            node = node1
        if node not in path and count<limit:
            if(count < limit):
                newpath = find_hierarchy_path(node, end, (count+1), path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
            else: return null
    return shortest
    
def split_caption(caption):
    stops = set(stopwords.words("english"))
    tokens = caption.split()
    filtered_words = [word for word in tokens if word not in stops]
    # maybe we want to map stop words to something meaningful
    # in - location
    # in -time
    return filtered_words

def get_base(word):
    # Change this to use conceptnet5 local
    obj = requests.get('http://api.conceptnet.io/c/en'+word).json()
    edges = obj['edges']
    for edge in edges:
        print(edge['surfaceText'])

# Returns true if there are no edges between words (no commonality)
def not_related(word1, word2):
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word1+'&other=/c/en/'+word2).json()
    edges = obj['edges']
    if(not edges):
        print(word1+" is not reasonably related to "+word2)
        explain_non_relation(word1, word2)
        return True
    else:
        print(word1+" is related to "+word2)
        explain_relation(word1,word2)
        return False

# Propagate through conceptNet to find a contradiction
def explain_non_relation(word1,word2):
    obj1 = requests.get('http://api.conceptnet.io/c/en/'+word1+'?limit=10000').json()
    obj2 = requests.get('http://api.conceptnet.io/c/en/'+word2).json()
    obj1_dict = {}
    obj2_dict = {}
    edges1 = obj1['edges']
    edges2 = obj2['edges']
    
    for edge in edges1:
        first = edge['start']['label']
        relation = edge['rel']['label']
        last = edge['end']['label']
        score = edge['weight']
        if(relation != 'Synonym'):
            obj1_dict[(first, relation, last)] = score
    for edge in edges2:
        first = edge['start']['label']
        relation = edge['rel']['label']
        last = edge['end']['label']
        score = edge['weight']
        obj2_dict[(first, relation, last)] = score
    return

# Go through the set of edges and see what makes sense
def explain_relation(word1,word2):
    obj = requests.get('http://api.conceptnet.io/query?node=/c/en/'+word1+'&other=/c/en/'+word2).json()
    edges = obj['edges']
    relation_list = []

    for edge in edges:
        #print(edge)
        relation = edge['rel']['label']
        # get the label
        if(relation not in relation_list):
            print("REASONSING:  ")
            start = edge['start']['label']
            end = edge['end']['label']
            explain(relation, start, end)
            relation_list.append(relation)
    return

def find_hierarchy_target(word):
    return
    
# Explains how two words are related
def explain(label, word1, word2):
    if(label=="IsA"):
        print("  "+word1+" is a sub type or a specific instance of "+word2)
    elif(label=="partOf"):
        print("  "+word1+" is a part of "+word2)

# returns all the tags of a particular sentence
# Step 1 towards understanding.  
def tag(sentence):
    return pos_tag(word_tokenize(sentence))

# Finds the appropriate concepts from a sentence
# TODO - Step two, make all SVO triples
def findConcepts(tags):
    concepts = []
    subject = ""
    verb = "" 
    object = ""

    for tag in tags:
        (word, part) = tag
        if part=='NN' or part=='NP': # Maybe something special for proper?
            if subject == "":
                subject = word
            else:
                print("object is " + word)
                object = word
        elif part.startswith('V'): # This means that it is some sort of verb
            verb = word
        if subject and verb and object:
            svo = (subject, verb, object)
            concepts.append(svo)
            subject = ""
            verb = ""
            object = ""
    return concepts

# Use to run the whole thing
def explain_concepts(sentence):
    concepts = findConcepts(tag(sentence))
    return concepts
    
# Add another set of tests

def main():
    print(not_related("penguin", "bamboo"))
    tokens = split_caption('penguin in july')
    for word in tokens:
        get_base(word)
    print(tokens)

if __name__ == "__main__":
    print(not_related("fog", "weather"))
    print(not_related("wind", "weather"))
    print(not_related("smog", "weather"))
    print(explain_concepts("A mailbox crossing the street and I am a sad bunny"))
