from commonsense.logical_classes import Fact, parse_file_to_fact_list, create_facts_from_file, to_data_frame
import pandas as pd
import unittest

class TestFact(unittest.TestCase):

    def test_initialization(self):
        fact = Fact('penguin', 'isA', 'bird')
        self.assertTrue(fact.subject == 'penguin', 'Subject incorrectly initialized in fact')
        self.assertTrue(fact.predicate == 'isA', 'Predicate incorrectly initialized in fact')
        self.assertTrue(fact.object == 'bird', 'Object incorrectly initialized in fact')
        self.assertTrue(fact.reason is None, 'Reason incorrectly initialized in fact')
        self.assertTrue(fact.score == 1.0, 'Score incorrectly initialized in fact')

        pass

    def test_get_infix_fact_list(self):
        fact = Fact('penguin', 'isA', 'bird')
        infixList = fact.get_infix_fact_list()

        self.assertTrue(len(infixList) == 3, 'list of incorrect size returned by get_infix_fact_list')
        self.assertTrue(infixList[0] == [fact.subject, fact.predicate,
                                 fact.object], 'Incorrect value, should be of the following form [subject, predicate, object]')
        self.assertTrue(infixList[1] == fact.reason, 'Incorrect value, should be fact reason')
        self.assertTrue(infixList[2] == fact.score, 'Incorrect value, should be fact score')

        pass

    def test_to_data_frame(self):
        fact = Fact('penguin', 'isA', 'bird')
        dataframe = fact.to_data_frame()

        self.assertTrue(type(dataframe) is pd.DataFrame, 'to_data_frame returned an incorrect type')

        pass

    def test_read_file(self):
        facts = parse_file_to_fact_list("datasets/output_feb25.txt")
        test_fact = Fact('lookingInDEvent1', 'isa', 'LookingInDirectionEvent')
        self.assertTrue(test_fact in facts)
        pass

    def test_read_file_with_limt(self):
        facts = parse_file_to_fact_list("datasets/output_feb25.txt", 10)
        test_fact = Fact('lookingInDEvent1', 'isa', 'LookingInDirectionEvent')
        self.assertTrue(test_fact in facts)
        print(len(facts))
        self.assertTrue(len(facts) == 10)
        df = to_data_frame(facts)
        pass

    def test_read_file_with_limt(self):
        facts = parse_file_to_fact_list("datasets/output_feb25.txt", 30)
        test_fact = Fact('lookingInDEvent1', 'isa', 'LookingInDirectionEvent')
        self.assertTrue(test_fact in facts)
        print(len(facts))
        self.assertTrue(len(facts) == 30)
        df = to_data_frame(facts)
        pass

    def test_read_fact_file(self):
        facts = create_facts_from_file("gaze_facts.txt")
        relation = 'isA'
        true_facts = [Fact('down', relation, 'looking at the task'),
                    Fact('center', relation, 'looking at the robot'),
                    Fact('down and right', relation, 'looking at the picture')]
        self.assertEqual(facts, true_facts)


if __name__ == "__main__":
    unittest.main()
