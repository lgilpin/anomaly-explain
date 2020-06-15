# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from typing import Dict, List

import numpy as np
from reasoner import *

class TestReasoner(unittest.TestCase):
    def test_add_commonsense(self):
        self.assertEqual(1,1)
    # def _mock_results(nsamples, ngt, npred, detection_name):

    #     def random_attr():
    #         """
    #         This is the most straight-forward way to generate a random attribute.
    #         Not currently used b/c we want the test fixture to be back-wards compatible.
    #         """
    #         # Get relevant attributes.
    #         rel_attributes = detection_name_to_rel_attributes(detection_name)

    #         if len(rel_attributes) == 0:
    #             # Empty string for classes without attributes.
    #             return ''
    #         else:
    #             # Pick a random attribute otherwise.
    #             return rel_attributes[np.random.randint(0, len(rel_attributes))]

    #                 tp = np.nan
    #             else:
    #                 tp = calc_tp(metric_data, self.cfg.min_recall, metric_name)
    #             metrics.add_label_tp(class_name, metric_name, tp)

    #     self.assertEqual(0.08606662159639042, metrics.nd_score)

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
