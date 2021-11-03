from dataclasses import dataclass
import pandas as pd
from typing import List

@dataclass
class Fact:

    subject: str
    predicate: str
    object: str
    reason = None
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
