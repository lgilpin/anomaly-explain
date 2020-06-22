# File: test_synthesize.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description:  Unit tests for the explanation Synthesizer code

import sys
import os
import unittest

sys.path.append(os.path.abspath('../'))

import numpy as np
from synthesizer.synthesize import *

class TestSynthesizer(unittest.TestCase):
    def test_blank(self):
        self.assertEqual("hello","hello")


class TestBackChain(unittest.TestCase):
    def penguin_test(self):
        
        # Uncomment this to test out your backward chainer
        pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules,
                                        'opus is a penguin'))
        a = pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules,
                                        'opus is a penguin'))
        self.assertEqual(a, 'b')
        

if __name__ == '__main__':
    unittest.main()
