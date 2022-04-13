import sys
from dataclasses import dataclass
import pandas as pd
from typing import List

DEFAULT_ANCHOR = 'object'


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

def parse_file_to_fact_list(fileName: str) -> List[Fact]:
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
    return fact_list

