
import pandas as pd
from enum import Enum

LOCATIONS = lambda x: x[x['Relation']=='AtLocation']
ANCHORS = lambda x: x[x['Relation']=='IsA']

class Primitives(Enum):
    INGEST = "ingest"
    MOVE = "move"

def challenge(kb: pd.DataFrame, glove: pd.DataFrame, description: str) -> None:
    """
    Challenges facts that are important to reasonability between conceptNet and Glove"""
    words = description.split()
    verb = words[1]
    if verb.startswith('eat'):
        print("Binding to the INGEST primitive")
        check_locations(kb, glove)
    else:
        print("Binding to the MOVE primitive")
        check_anchors(kb, glove)
    return 

def check_locations(kb: pd.DataFrame, glove: pd.DataFrame) -> bool:
    """
    Checks for location information"""
    uniques = LOCATIONS(kb).apply(lambda x: x.nunique())['Word2']

    # Checking for commonsense locations.
    if len(LOCATIONS(kb)) == uniques:
        print("Commonsense failure: primitive needs common locations. ")
        #detail_locations(LOCATIONS(kb))

    glove_support = 0 
    subjects = []
    locations = []
    for i, row in enumerate(glove.sort_values(by = ['Score'], ascending=False).values):
        [subject, _, value, score] = row
        if value in locations:
            if glove_support < 2:
                print(f"GloVe support for common location: {value} with score: {score}")
                glove_support += 1
        subjects.append(subject)
        locations.append(value)
    if glove_support > 0:
        print(f"Commonsense lacking, Synthesizer trusting GloVe; with common locations: {locations[0]}, {locations[1]}")

def check_anchors(kb: pd.DataFrame, glove: pd.DataFrame) -> bool:
    """
    Checks for isA animal information"""
    glove_support = False
    commonsense = False
    if 'animal' in kb['Word2'].values:
        print("Subject is an animal that can move on it's own.  Trusting commonsense.")
        commonsense = True
    else:
        print("No commonsense support.")
    if 'animal' in glove['Word2'].values:
        print("Subject is an animal that can move on it's own.  Trusting GloVe.")
        glove_support = True
    else:
        print("No GloVe support supporting the support as an animal.")

    # Debating
    if not glove_support and not commonsense:
        print("No commonsense or Glove knowledge supporting a moveable subject.")
    elif glove_support and commonse:
        print("Both support moveable support.")
    else:
        if commonsense: trust = "commonsense"
        else: trust = "GloVe"
        print(f"Disagreement between commonsense and glove.  Trusting {trust}")

def detail_locations(kb: pd.DataFrame) -> None:
    print(kb.groupby('Word1').sort_values('Score').first())
    
