from commonsense.logical_classes import Fact
from commonsense import *
import pandas as pd
from commonsense.conceptnet import ConceptNet, query_prefix, rel_term, limit_suffix
import unittest

class TestDF(unittest.TestCase):

    def test_df(self):
        cn = ConceptNet()

        description = 'penguin crossing the street'
        concepts = ['penguin', 'street']
        commonsense_facts = cn.build_df(concepts)
        print(commonsense_facts)

        pass

if __name__ == "__main__":
    unittest.main()
