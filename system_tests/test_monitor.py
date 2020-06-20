# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from typing import Dict, List
import sys
import os

sys.path.append(os.path.abspath('../'))

import numpy as np
from monitor.reasonableness_monitor import *

class TestSnapshotMonitor(unittest.TestCase):
    def test_blank(self):
        self.assertEqual("hello","hello")

    def test_add_data(self):
        """
        Test that the data gets adds to the monitor 
        """
        monitor = SnapshotMonitor([], [], [])
        new_data = "blank"
        monitor.add_data(new_data)
        self.assertEqual(monitor.data, new_data)

    def test_add_reason(self):
        """
        These reasons aren't used right now, but they might be
        """
        monitor = SnapshotMonitor([], [], [])
        new_reason = "blank"
        monitor.add_reason(new_reason)
        self.assertEqual(monitor.reasons, [new_reason])
        
    def test_label_summary(self):
        """
        TODO Check the null case
        """
        labels = ['bicycle', 'vehicle', 'unknown_object']
        monitor = SnapshotMonitor(labels, [], [])
        summary = 'bicycle, vehicle, unknown_object'
        self.assertEqual(monitor.label_summary(), summary)

#     def test_find_anchor(self):
#         """
#         Tests the anchor point labeling for the uber example
#         and other default "objects"
#         """
#         concepts = ['ball', 'bicycle', 'trash']
#         anchors = ['animal', 'object', 'place', 'plant']
#         reason = 'ConceptNet IsA link'
#         default_reason = 'Default anchor point'
        
#         for concept in concepts:
#             result = make_fact([concept, 'IsA', 'object'], reason)
#             trial = find_anchor(concept, anchors)
#             self.assertEqual(result, trial)

#         # LHG adds spring 2020: test the default anchor
#         bad_concepts = ['vehicle', 'mailbox']
#         for concept in bad_concepts:
#             result = make_fact([concept, 'IsA', 'object'],
#                            default_reason)
#             trial = find_anchor(concept, anchors)
#             self.assertEqual(result, trial)

#     def test_make_prolog_fact(self):
#         """
#         Tests the anchor point labeling for the uber example
#         """
#         concepts = ['vehicle', 'bicycle']
#         anchors = ['animal', 'object', 'place', 'place', 'plant']
#         reason = 'ConceptNet IsA link'

#         for concept in concepts:
#             result = make_prolog_fact([concept, 'IsA', 'object'],
#                                       reason)
#             trial = ["IsA("+concept+", object)", reason]
#             self.assertEqual(result, trial)
        
# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

if __name__ == '__main__':
    unittest.main()
