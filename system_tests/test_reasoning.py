# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest

import numpy as np

from reasoning.rules import *
from reasoning.test_rules import *
from reasoning.production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from reasoning.data import *
import pprint

class TestRules(unittest.TestCase):
    def test_anchor_rule(self):
        true_rule = IF (AND ("IsA((?a), (?x))", "IsA((?b), (?x))"),
                        THEN ("consistent (?a) (?b)"))
        test_rule = same_anchor_rule(2)
        self.assertEqual(str(test_rule), str(true_rule))
    def test_forward_chain(self):
        test_rule = IF(AND("(?x) IsA (?y)", "(?z) IsA (?y)",
                           NOT("self (?x) (?z)")),
                       THEN("(?x) consistent (?z)"))
        same_rule = IF('(?x) IsA (?y)', THEN('self (?x) (?x)'))
        test_data = ['unknown_object IsA object',
                     'vehicle IsA object',
                     'bicycle IsA object',
                     'vehicle AtLocation street',
                     'bicycle AtLocation garage',
                     'bicycle AtLocation street',
                     'bicycle AtLocation toy_store']
        testing = forward_chain([same_rule, test_rule], test_data)
        IsA_answer = ['unknown_object IsA object', 'vehicle IsA object', 'bicycle IsA object',
                      'vehicle AtLocation street', 'bicycle AtLocation garage',
                      'bicycle AtLocation street', 'bicycle AtLocation toy_store',
                      'self unknown_object unknown_object', 'self vehicle vehicle',
                      'self bicycle bicycle',
                      'unknown_object consistent vehicle',
                      'unknown_object consistent bicycle', 'vehicle consistent unknown_object',
                      'vehicle consistent bicycle', 'bicycle consistent unknown_object',
                      'bicycle consistent vehicle']
        self.assertEqual(set(IsA_answer), set(testing))
                       

class TestTransitive(unittest.TestCase):
    def test_abc(self):
        abc_answer =  ( 'a beats b', 'b beats c', 'a beats c' )
        transitive_rule_abc = forward_chain([transitive_rule], abc_data)
        self.assertEqual(transitive_rule_abc, abc_answer)

    def test_poker(self):
        """
        Does set equals, probably want to do something else 
        """
        poker_answer = ('flush beats pair', 'flush beats straight',
                'flush beats three-of-a-kind', 'flush beats two-pair',
                'full-house beats flush', 'full-house beats pair',
                'full-house beats straight', 'full-house beats three-of-a-kind',
                'full-house beats two-pair', 'straight beats pair',
                'straight beats three-of-a-kind', 'straight beats two-pair',
                'straight-flush beats flush', 'straight-flush beats full-house',
                'straight-flush beats pair', 'straight-flush beats straight',
                'straight-flush beats three-of-a-kind',
                'straight-flush beats two-pair', 'three-of-a-kind beats pair',
                'three-of-a-kind beats two-pair', 'two-pair beats pair')
        transitive_rule_poker = forward_chain([transitive_rule], poker_data)
        self.assertEqual(set(transitive_rule_poker), set(poker_answer))

    def test_family_rules(self):
        """
        Does another splitting equals
        """
        sibling_answer = ['child luigi papa', 'child mario papa', \
                          'parent papa luigi', 'parent papa mario',
                          'sibling luigi mario', 'sibling mario luigi']
        grandparent_answer = ['child alex claire', 'child claire jay',
                      'grandchild alex jay', 'grandparent jay alex',
                      'parent claire alex', 'parent jay claire']

        anonymous_family_answer = [ 'cousin c1 c3',
                            'cousin c1 c4',
                            'cousin c2 c3',
                            'cousin c2 c4',
                            'cousin c3 c1',
                            'cousin c3 c2',
                            'cousin c4 c1',
                            'cousin c4 c2',
                            'cousin d1 d2',
                            'cousin d2 d1',
                            'cousin d3 d4',
                            'cousin d4 d3' ]
        
        expected_sibling = set(sibling_answer)
        family_rules_sibling = forward_chain(family_rules, sibling_test_data)

        expected_grandparent = set(grandparent_answer)
        family_rules_grandparent = forward_chain(family_rules, grandparent_test_data)

        expected_anonymous = set(anonymous_family_answer)
        family_rules_anonymous = forward_chain(family_rules, anonymous_family_test_data)
        
        self.assertEqual(set( [x for x in family_rules_sibling if
                               x.split()[0] in ('parent', 'child', 'sibling')]), expected_sibling)
        self.assertEqual(set( [x for x in family_rules_grandparent if
                               x.split()[0] in ('parent', 'child','grandparent', 'grandchild')]),
                         expected_grandparent)
        self.assertEqual(set( [x for x in family_rules_anonymous if
                               x.split()[0] =='cousin']),
                         expected_anonymous)
        
#    def test_family_grandparent(self):


class TestBackChain(unittest.TestCase):
    def test_abitrary(self):
        """
        In HW 1 this is test 17
        """
        ARBITRARY_EXP = (
            IF( AND( 'a (?x)',
                     'b (?x)' ),
                THEN( 'c d' '(?x) e' )),
            IF( OR( '(?y) f e',
                    '(?y) g' ),
                THEN( 'h (?y) j' )),
            IF( AND( 'h c d j',
                     'h i j' ),
                THEN( 'zot' )),
            IF( '(?z) i',
                THEN( 'i (?z)' ))
        )
        result_bc_5 = OR('zot',
                 AND('h c d j',
                     OR('h i j', 'i f e', 'i g', 'g i')))
        self.assertEqual(str(backchain_to_goal_tree(ARBITRARY_EXP, 'zot')), str(result_bc_5))
        
if __name__ == '__main__':
    unittest.main()
