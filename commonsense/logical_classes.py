import sys
from dataclasses import dataclass
import pandas as pd
from typing import List
import os

DEFAULT_ANCHOR = 'object'
DATA_DIR = 'datasets/'


@dataclass
class Fact:

    subject: str
    predicate: str
    object: str
    reason: str = None
    score: float = 1.0
    count: int = 1

    # Removed to_list because one can just extract the results returned by to_list from
    # the results returned by get_infix_fact_list
    def get_infix_fact_list(self):
        return [[self.subject, self.predicate, self.object], self.reason, self.score]

    def to_infix_flat_list(self) -> List:
        return [self.subject, self.predicate, self.object, self.score]

    def to_data_frame(self):

        data = {'Subject':[self.subject], 'Predicate':[self.predicate], 'Object':[self.object], 'Reason':[self.reason]}
        dataframe = pd.DataFrame(data)

        return dataframe

    def all_concepts(self) -> List:
        """
        Takes a fact and returns all the relevant concepts (e.g., the subject and object).
        :return: A list of the subject and object
        :rtype: List
        """
        return [self.subject, self.object]

    def __eq__(self, other):
        """
        Equality method.  Strips out all the prefixes (a or the)

        :param other: Another fact
        :type other:
        :return:
        :rtype:
        """
        if self.predicate != other.predicate:
            return False
        elif self.subject == other.subject and self.object == other.object:
            return True
        else:
            cleaned1 = self.clean_fact()
            cleaned2 = other.clean_fact()
            if cleaned1.subject == cleaned2.subject and cleaned1.object == cleaned2.object:
                return True
            else: return False

    def clean_fact(self):
        return Fact(clean_concept(self.subject), self.predicate, clean_concept(self.object), self.reason, self.score)

@dataclass
class Event:
    facts: List[Fact]
    timestamp: int = 0
    event_type: str = None
    label: str = None
    actor: str = None

    def __post_init__(self):
        for fact in self.facts:
            if fact.predicate == 'timestamp':
                self.timestamp = fact.object
            if fact.predicate == 'isa':
                if fact.subject.startswith("looking"):
                    self.event_type = 'looking'
                elif fact.subject.startswith("speaking"):
                    self.event_type = 'speaking'
                else:
                    self.event_type = 'final'
        self.set_label()

    def set_label(self):
        query = 'direction' if self.event_type == 'looking' else 'utterance'
        for fact in self.facts:
            if fact.predicate == query:
                self.label = fact.object


@dataclass
class EventReasoner:
    facts: List[Fact]
    is_changed: bool = False

    def assert_fact(self, fact):
        if not fact in self.facts:
            self.facts += [fact]
            self.is_changed = True

    # def forward_chain(self):
    #     while self.is_changed:
    #         is_changed = False
    #         for fact in self.facts:
    #             if fact.predicate == "direction":




def clean_concept(concept: str) -> str:
    """
    Removes the starting strings from conceptNet text

    :param concept: The input string
    :type concept: str
    :return: A cleaned concept (with a or the)
    :rtype: str
    """
    if concept.startswith("a "):
        subject = concept.replace("a ", "")
        return subject
    elif concept.startswith("the "):
        subject = concept.replace("the ", "")
        return subject


def default_fact(concept, include_score: bool = False) -> Fact:
    """
    Returns a fact of the default anchor.

    :param concept: The input concept
    :type concept: str
    :param include_score: boolean of whether to include the score (or not).
    :type include_score: bool
    :return: A default fact with the default relation and anchor (IsA right now).
    :rtype: Fact
    """
    return Fact(concept, 'IsA', DEFAULT_ANCHOR, "Default anchor point")


def to_data_frame(facts: List) -> pd.DataFrame:
    """
    Makes a dataframe from a list of facts

    :param facts: The input list of facts
    :type facts: List
    :return: A dataframe
    :rtype: pd.DataFrame
    """
    df = pd.DataFrame([vars(fact) for fact in facts])

    # Make sure the subject is the first column
    target_cols = ['subject', 'predicate','object', 'reason', 'score', 'count']
    return df[target_cols]

def parse_file_to_fact_list(fileName: str, limit: int = -1) -> List[Fact]:
    """
    Parses a file and turns it into a list of facts to parse
    :param str:
    :type str:
    :return:
    :rtype:
    """
    fact_list = []
    file1 = open("/Users/leilani/workspace/anomaly-explain/datasets/PAX/output_feb25.txt", 'r')
    lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        if line.strip() != "":
            tokens = line.strip().replace("(", "").replace(")", "").split()
            fact = Fact(tokens[1], tokens[0], tokens[2])
            fact_list.append(fact)
    file1.close()
    if limit > 0:
        return fact_list[0:limit]
    else:
        return fact_list

def parse_raw_file_to_event_list(fileName: str, event_limit: int = -1) -> List[Fact]:
    """
    Parses a file and turns it into a list of facts to parse
    :param str:
    :type str:
    :return:
    :rtype:
    """
    fact_list_per_event = []
    file1 = open("/Users/leilani/workspace/anomaly-explain/datasets/allnewsemanticdatawithmultimodal/allnewsemanticdatawithmultimodal0025.txt", 'r')
    lines = file1.readlines()
    events = []

    count = 0
    # Strips the newline character
    for line in lines:
        if line.strip() != "":
            tokens = line.strip().replace("(", "").replace(")", "").split()
            fact = Fact(tokens[1], tokens[0], tokens[2])
            fact_list_per_event.append(fact)
        else: # ending of an event
            print(line)
            new_event = Event(fact_list_per_event)
            events.append(new_event)
            fact_list_per_event = []

    file1.close()
    if event_limit > 0:
        return events[0:event_limit]
    else:
        return events


def parse_file_to_event_list(fileName: str="/Users/leilani/workspace/anomaly-explain/datasets/PAX/output_feb25.txt",
 event_limit: int = -1) -> List[Fact]:
    """
    Parses a file and turns it into a list of facts to parse
    :param str:
    :type str:
    :return:
    :rtype:
    """
    fact_list_per_event = []
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    events = []

    count = 0
    # Strips the newline character
    for line in lines:
        if line.strip() != "":
            tokens = line.strip().replace("(", "").replace(")", "").split()
            fact = Fact(tokens[1], tokens[0], tokens[2])
            fact_list_per_event.append(fact)
        else: # ending of an event
            new_event = Event(fact_list_per_event)
            events.append(new_event)
            fact_list_per_event = []

    file1.close()
    if event_limit > 0:
        return events[0:event_limit]
    else:
        return events

def get_fact_query(query: str, facts: List[Fact]) -> Fact:
    for fact in facts:
        if fact.subject == query or fact.object == query:
            return fact
    return None

def create_facts_from_file(filename: str) -> List[Fact]:
    """
    Reads in a file and creates a list of new facts.
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    facts = []
    pathName = '/Users/leilani/workspace/anomaly-explain/datasets/PAX/' + filename
    with open(pathName) as file:
        lines = file.readlines()
    for line in lines:
        tokens = line.strip().split(",")
        if len(tokens) == 2:
            facts.append(Fact(tokens[0].strip(), 'isA', tokens[1].strip()))
        else:
            facts.append(Fact(tokens[0].strip(), tokens[1], tokens[2].strip()))
    return facts

def sort_key(event: Event):
    #helper for sort_event_list
    return event.timestamp

def sort_event_list(eventList: list):
    #sorts a list of events by timestamp
    return eventList.sort(key=sort_key)

# def create_sorted_events_file(filename: str="sorted_events.txt", eventList: List):
#     #assumes that eventList is unsorted
#     #this WILL overwrite any previous text on the given filename
#     sorted_list=sort_event_list(eventList)
#     file=open(filename, "w")
#     for event in sortedList:
#         file.write('\n')
#         file.write(event.timestamp)
#         file.write(event.event_type)
#         file.write(event.label)
#         file.write(event.actor)
#         file.write(event.facts)

def preprocess(fileName: str = "allnewsemanticdatawithmultimodal0025.txt") -> List:
    """
    Preprocesses a raw file.  Data is located in datasets/PAX/allnewsemanticdatawithmultimodal/

    :param fileName: the input filename
    :type fileName: str
    :return: A list of events
    :rtype: List[Event]
    """
    prefix = os.getcwd()
    file1 = open(prefix+"/datasets/PAX/allnewsemanticdatawithmultimodal/"+fileName, 'r')
    lines = file1.readlines()
    events = []
    lookingPointCounter = 1
    lookingDirectionCounter = 1
    speaksCounter = 1

    count = 0
    # Strips the newline character
    for line in lines:  # each one is a new event
        tokens = line.strip().replace("(", "").replace(")", "").split()
        if tokens[2] == 'lookingAtPoint':
            eventName = 'lookingAtPEvent%d' % lookingPointCounter
            [Fact(eventName, 'isa', 'LookingAtPointEvent')]
            facts = make_looking_event_from_line(eventName, 'lookingAtPoint',
                                                 tokens[1], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7])
            event = Event(facts, tokens[7])
            events.append(event)
            lookingPointCounter += 1
        elif tokens[2] == 'lookingInDirection':
            eventName = 'lookingAtPEvent%d' % lookingDirectionCounter
            facts = make_direction_event_from_line(eventName, 'lookingInDirection',
                                                   tokens[1], tokens[3], tokens[4], tokens[5])
            event = Event(facts, tokens[5])
            events.append(event)
            lookingDirectionCounter += 1
        elif tokens[2] == 'speaksUtterance':  # utterance
            eventName = 'speaksUttEvent%d' % speaksCounter
            facts = make_utterance_event_from_line(eventName, 'speaksUtteranceEvent',
                                                   tokens[1], tokens[3], tokens[4], tokens[5])
            event = Event(facts, tokens[5])
            events.append(event)
            speaksCounter += 1
        else:
            facts = [Fact(tokens[2], tokens[1], tokens[3]),
                     Fact(eventName, 'timestamp', tokens[4])]
            event = Event(facts, tokens[4])
            events.append(event)
    return events


def make_looking_event_from_line(eventName, eventType, observer, looker, x, y, z, timestamp):
    return [Fact(eventName, 'isa', eventType),
            Fact(eventName, 'observedBy', observer),
            Fact(eventName, 'looker', looker),
            Fact(eventName, 'pointX', x),
            Fact(eventName, 'pointY', y),
            Fact(eventName, 'pointZ', z),
            Fact(eventName, 'timestamp', timestamp)]


def make_direction_event_from_line(eventName, eventType, observer, looker, direction, timestamp):
    return [Fact(eventName, 'isa', eventType),
            Fact(eventName, 'observedBy', observer),
            Fact(eventName, 'looker', looker),
            Fact(eventName, 'direction', direction),
            Fact(eventName, 'timestamp', timestamp)]


def make_utterance_event_from_line(eventName, eventType, observer, speaker, utterance, timestamp):
    return [Fact(eventName, 'isa', eventType),
            Fact(eventName, 'observedBy', observer),
            Fact(eventName, 'speaker', speaker),
            Fact(eventName, 'utterance', utterance),
            Fact(eventName, 'timestamp', timestamp)]
