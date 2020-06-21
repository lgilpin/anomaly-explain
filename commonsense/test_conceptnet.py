# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from typing import Dict, List

import numpy as np
from commonsense.conceptnet import *


class TestConceptnet(unittest.TestCase):
    def test_find_anchor(self):
        """
        Tests the anchor point labeling for the uber example
        and other default "objects"
        """
        concepts = ['ball', 'bicycle', 'trash']
        anchors = ['animal', 'object', 'place', 'plant']
        reason = 'ConceptNet IsA link'
        default_reason = 'Default anchor point'

        for concept in concepts:
            result = make_fact([concept, 'IsA', 'object'], reason)
            trial = find_anchor(concept, anchors)
            self.assertEqual(result, trial)

        # LHG adds spring 2020: test the default anchor
        bad_concepts = ['vehicle', 'mailbox']
        for concept in bad_concepts:
            result = make_fact([concept, 'IsA', 'object'],
                               default_reason)
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
            result = make_prolog_fact([concept, 'IsA', 'object'],
                                      reason)
            trial = ["IsA(" + concept + ", object)", reason]
            self.assertEqual(trial, result)

    def test_make_fact(self):
        """
        Tests the make fact function
        """
        # Tests if the following concepts are recognized as objects with the making of facts
        concepts = ['vehicle', 'bicycle', 'person', 'motorcycle']
        reason = 'ConceptNet IsA link'

        for concept in concepts:
            result = make_fact([concept, 'IsA', 'object'],
                               reason)
            answer = [concept + " IsA object", reason]
            self.assertEqual(answer, result)

    # TODO: Come back and update once Leilani cleaned up function
    def test_clean_phrase(self):
        """
        Tests cleaning out un-necessary words from text
        """
        # Groups of cleaned an uncleaned words in tuples for easy testing
        set_a = ("the cat in hat", "cat_in_hat")
        set_b = ("a car speeding", "car_speeding")
        set_c = ("an elevated sloped road", "elevated_sloped_road")
        set_d = ("and man ran", "man_ran")

        set_list = [set_a, set_b, set_c, set_d]  # Add all sets to a list

        for set in set_list:
            result = clean_phrase(set[0])  # gives cleaned phrase
            answer = set[1]
            self.assertEqual(answer, result)

    def test_clean(self):
        """
        Checks the clean function to make sure that it properly cleans out phrases and leaves strings alone
        """
        # TODO: Not sure if test clean is supposted to work like this
        set_a = ("man_isA_object", "object")
        set_b = ("bicycle", "bicycle")
        set_c = ("car_isA_vehicle", "vehicle")
        set_d = ("car", "car")

        set_list = [set_a, set_b, set_c, set_d]  # Add all sets to a list

        for set in set_list:
            result = clean(set[0])  # gives cleaned phrase
            answer = set[1]
            self.assertEqual(answer, result)

    def test_build_relation(self):
        """
        Checks whether facts are being correctly built
        Answers directly from ConceptNet Website (https://conceptnet.io/)

        """
        # TODO: Not all answers showing up properly from query itself
        # Answers
        a_answer = [['bicycle IsA two_wheel_vehicle', 'ConceptNet'], ['bicycle IsA bicycle', 'ConceptNet'],
                    ['bicycle IsA transportation', 'ConceptNet']]
        b_answer = [['dog IsA loyal_friend', 'ConceptNet'], ['dog IsA pet', 'ConceptNet'],
                    ['dog IsA mammal', 'ConceptNet'], ['dog IsA dog', 'ConceptNet'], ['dog IsA canine', 'ConceptNet']]
        c_answer = [['car CapableOf go_fast', 'ConceptNet'], ['car CapableOf crash', 'ConceptNet'],
                    ['car CapableOf roll_over', 'ConceptNet'], ['car CapableOf slow_down', 'ConceptNet']]
        d_answer = [['vehicle AtLocation street', 'ConceptNet'], ['vehicle AtLocation vehicle', 'ConceptNet']]

        # The prompts with the answers attached
        set_a = (("bicycle", "IsA"), a_answer)
        set_b = (("dog", "IsA"), b_answer)
        set_c = (("car", "CapableOf"), c_answer)
        set_d = (("vehicle", "AtLocation"), d_answer)

        set_list = [set_a, set_b, set_c, set_d]  # Add all sets to a list

        for set in set_list:
            result = build_relation(set[0][0], set[0][1])  # gives cleaned phrase
            answer = set[1]
            self.assertEqual(answer, result)

    def test_aggregate(self):

        # a_answer =
        # b_answer =
        # c_answer =
        # d_answer =
        # TODO: Does not take in fact, only works if a non-fact goes in
        list_of_relations = ["IsA", "AtLocation", "CapableOf"]  # List of relations we will test with

        # The prompts with the answers attached
        set_a = aggregate(['bicycle IsA two_wheel_vehicle', 'ConceptNet'], list_of_relations)
        print(set_a)
        set_b = aggregate(['dog IsA loyal_friend', 'ConceptNet'], list_of_relations)
        print(set_b)
        set_c = aggregate(['car CapableOf go_fast', 'ConceptNet'], list_of_relations)
        print(set_c)
        set_d = aggregate(['vehicle AtLocation street', 'ConceptNet'], list_of_relations)
        print(set_d)
        # set_list = [set_a, set_b, set_c, set_d]  # Add all sets to a list


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
