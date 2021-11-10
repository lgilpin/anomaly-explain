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
    target_cols = ['subject', 'predicate','object', 'reason', 'score']
    return df[target_cols]