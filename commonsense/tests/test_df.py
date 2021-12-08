from commonsense.logical_classes import Fact
from commonsense.conceptnet import ConceptNet, query_prefix, rel_term, limit_suffix
from monitor.reasonableness_monitor import SnapshotMonitor
import unittest

class TestDF(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_df(self):
        cn = ConceptNet()

        description = 'penguin crossing the street'
        concepts = ['penguin', 'street']
        commonsense_facts = cn.build_df(concepts)
        # print(commonsense_facts)

        pass

    @unittest.skip("demonstrating skipping")
    def test_location(self):
        cn = ConceptNet()
        concepts = ['building', 'property', 'table', 'real estate', 'room', 'recreation', 'event',
                    'flooring', 'ceiling', 'vehicle']
        commonsense_facts = cn.build_df(concepts)
        # print(commonsense_facts)
        str = cn.explain_location(concepts, commonsense_facts)
        print(str)
        # cn.explain()

        pass

    def test_location_order(self):
        cn = ConceptNet()
        concepts = ['building', 'property', 'table', 'real estate', 'room', 'recreation', 'event',
                    'flooring', 'ceiling', 'vehicle']
        # commonsense_facts = cn.build_df(concepts)
        # print(commonsense_facts)
        str = cn.explain_location_by_rank(concepts)
        print(str)
        # cn.explain()

        pass

    @unittest.skip("demonstrating skipping")
    def test_anchor(self):
        fact = Fact("penguin", "IsA", "animal")
        subject_anchors = ['animal', 'object', 'place', 'plant']

        cn_kb = ConceptNet()
        cn_monitor = SnapshotMonitor()  # labels=labels, data=data, rules=rules)
        print("Trying find anchor")
        result=cn_kb.find_closest_anchor(fact.subject, subject_anchors, include_score=False)
        print(result)
        print("Made a ConceptNet monitor, now trying to explain")
        cn_facts = cn_monitor.explain_fact(fact)

        pass


if __name__ == "__main__":
    unittest.main()
