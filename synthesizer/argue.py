
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
    LOCATIONS(kb)
    uniques = LOCATIONS(kb).apply(lambda x: x.nunique())['Word2']

    # Checking for commonsense locations.
    if len(LOCATIONS(kb)) == uniques:
        print("Commonsense failure: primitive needs common locations. ")
        detail_locations(LOCATIONS(kb))

def check_anchors(kb: pd.DataFrame, glove: pd.DataFrame) -> bool:
    """
    Checks for isA animal information"""

def detail_locations(kb: pd.DataFrame) -> None:
    print(kb.groupby('Word1').sort_values('Score').first())
    
