# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from reasoner.production import IF, AND, OR, NOT, THEN, DELETE #, # forward_chain, pretty_goal_tree
from reasoner.chain import forward_chain, chain_explanation
from reasoner.data import *
from commonsense.logical_classes import Fact
import pprint


transitive_rule = IF(AND('(?x) IsA (?y)', '(?y) IsA (?z)'),
                     THEN('(?x) IsA (?z)'))

class TestFactReasoner(unittest.TestCase):
    """
    TODO: Change the name (find_closest_anchor).
    """
    def test_forward_chain_fact(self):
        data_facts = [Fact('penguin', 'IsA', 'bird'),
                      Fact('bird', 'IsA', 'animal')]

        chained_data = forward_chain(data_facts)

        print("ended with %s facts" % len(chained_data))
        self.assertEqual(3, len(chained_data))
        #self.assertEqual(data_facts + [Fact('penguin', 'IsA', 'animal')], chained_data)
        # print(chained_data)

    def test_chain(self):
        my_facts = [Fact('penguin', 'IsA', 'bird'),
                 Fact('bird', 'IsA', 'animal')]
        # print(len(my_facts))
        # test_facts = my_facts
        # new_facts = forward_chain(my_facts)
        # print(new_facts)

        transitive_rule = IF(AND('(?x) IsA (?y)', '(?y) IsA (?z)'),
                             THEN('(?x) IsA (?z)'))
        # data_facts = [fact.to_string() for fact in new_facts]
        # backchain_to_goal_tree([transitive_rule], data_facts)
        print(len(my_facts))
        ret = chain_explanation(my_facts, Fact("penguin", "IsA", "animal"))
        self.assertEqual([Fact('penguin', 'IsA', 'bird'), Fact('bird', 'IsA', 'animal')], ret)
        #
        #
        chain_facts = [Fact('opus', 'IsA', 'penguin'), Fact('penguin', 'can', 'fly'),
                       Fact('fly', 'IsA', 'bird'), Fact('bird', 'IsA', 'animal')]
        ret = chain_explanation(chain_facts, Fact("opus", "IsA", "animal"))
        print(ret)


if __name__ == '__main__':
    unittest.main()
