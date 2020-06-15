# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from typing import Dict, List

import numpy as np
from conceptnet import *

class TestConceptnet(unittest.TestCase):
    def test_find_anchor(self):
        """
        Tests the anchor point labeling for the uber example
        """
        concepts = ['vehicle', 'bicycle']
        anchors = ['animal', 'object', 'place', 'place', 'plant']
        reason = 'ConceptNet IsA link'

        for concept in concepts:
            result = make_fact([concept, 'IsA', 'object'], reason)
            trial = find_anchor(concept, anchors)
            self.assertEqual(result, trial)

    def test_make_prolog_fact(self):
        """
        Tests the anchor point labeling for the uber example
        """
        concepts = ['vehicle', 'bicycle']
        anchors = ['animal', 'object', 'place', 'place', 'plant']
        reason = 'ConceptNet IsA link'

        for concept in concepts:
            result = make_prolog_fact([concept, 'IsA', 'object'], reason)
            trial = ("IsA("+concept+", object)", reason)
            self.assertEqual(result, trial)
        
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
