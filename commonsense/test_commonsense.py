# nuScenes dev-kit.
# Code written by Leilani H. Gilpin, 2019/2020.

import random
import unittest
from typing import Dict, List

import numpy as np
# from commonsense.conceptnet import *
from conceptnet import ConceptNet, query_prefix, rel_term, limit_suffix, subject_anchors
import requests
from kb import *

class TestKB(unittest.TestCase):

    """
    TODO: Change the name (find_closest_anchor).
    """
    def test_find_anchor_point(self):
        cn = ConceptNet()
        for anchor in subject_anchors:
            self.assertEqual(cn.find_anchor_point(anchor, subject_anchors), anchor)

    def test_find_anchor_point_animal(self):
        cn = ConceptNet()
        self.assertEqual(cn.find_anchor_point("dog", subject_anchors), "animal")

    def test_find_anchor_point_object(self):
        cn = ConceptNet()
        self.assertEqual(cn.find_anchor_point("table", subject_anchors), "object")

    def test_find_anchor_point_plant(self):
        cn = ConceptNet()
        self.assertEqual(cn.find_anchor_point("tree", subject_anchors), "plant")

    def test_find_anchor(self):
        """
        OLDER
        Tests the anchor point labeling for the uber example
        and other default "objects"
        """
        concepts = ['ball', 'bicycle', 'trash']
        anchors = ['animal', 'object', 'place', 'plant']
        reason = 'ConceptNet IsA link'
        default_reason = 'Default anchor point'
        cn = ConceptNet()

        for concept in concepts:
            result = cn.make_fact([concept, 'IsA', 'object'], reason)
            trial = cn.find_anchor(concept, anchors)
            self.assertEqual(result, trial)

        # LHG adds spring 2020: test the default anchor
        bad_concepts = ['vehicle', 'mailbox']
        for concept in bad_concepts:
            result = cn.make_fact([concept, 'IsA', 'object'],
                               default_reason)
            trial = cn.find_anchor(concept, anchors)
            self.assertEqual(result, trial)

    def test_get_closest_anchor(self):

        concept_a = 'car'
        concept_b = 'dog'
        concept_c = 'human'
        anchors = ['vehicle', 'animal', 'object', 'person']
        cn = ConceptNet()
        # Trying to see if concepts has the isA relation with the above anchors

        self.assertEqual(['car IsA vehicle', 'ConceptNet IsA link'], cn.get_closest_anchor(concept_a, anchors))
        self.assertEqual(['dog IsA animal', 'ConceptNet IsA link'], cn.get_closest_anchor(concept_b, anchors))
        self.assertEqual(['human IsA animal', 'ConceptNet IsA link'], cn.get_closest_anchor(concept_c, anchors))

    def test_search_relation(self):
        """
        TODO: Maybe just add the ESSENTIALS
        e.g., bicycle -> has wheels, etc.
        """
        #This just tests that the function works, not necessarily the accuracy of the function

        a_answer = {'an environmentally friendly mode of trasportation', 'wheeled vehicle', 'a two wheeled method of transportation', 'a vehicle type', 'a two wheel vehicle', 'transportation', 'much smaller than a fire truck', 'steered y handlebars', 'toy', 'bike', 'bicycle', 'mountable transporter device', 'bicycle market category', 'bilaterally symmetric object', 'a two-wheeled vehicle,', 'good exercise', 'a bicycle', 'user powered device', 'a human powered vehicle', 'a vehicle with two wheels', 'an efficient form of human transportation', 'user guided device', 'vehicle'}
        b_answer = {'a nice friend', 'shedding', 'a good friend', 'a faithful companion', 'so big', 'canine', 'a dog', 'mammal', 'pet', 'a domesticated canine', 'happy when it wags its tail', 'domestic animal', 'a canine', 'cuter than your kids', 'an example of a pet', 'a four legged animal', 'dog', 'straining at its leash', 'chap', 'a mans best friend', 'a curious observer of mankind', 'a thing', 'a loyal friend'}
        c_answer = {'drive over a cat', 'carry few persons', 'go fast', 'kill a cat', 'pass another car', 'seat riders', 'crash', 'slow near schools', 'kill a person', 'pull a car', 'rush through traffic', 'corner a corner', 'pass a bus', 'get a flat tire', 'bottom out', 'cost money', 'move quickly', 'travel down the road', 'pass other car', 'serve to transport', 'slow down', 'kill people', 'be heading north', 'move on a road', 'cost a lot of money', 'roll over', 'tail another car', 'set off', 'enter that garage', 'head north', 'need petrol', 'last several years', 'start running', 'roll downhill', "start if it's working", 'fail to start', 'travel over a bridge', 'come up the drive', 'drive up the street', 'back up', 'turn around', 'hit a wall', 'seat people', 'move a person'}
        d_answer = {'vehicle', 'a vehicle', 'a freeway', 'the street'}

        set_a = (("bicycle", "IsA"), a_answer)
        set_b = (("dog", "IsA"), b_answer)
        set_c = (("car", "CapableOf"), c_answer)
        set_d = (("vehicle", "AtLocation"), d_answer)

        answer_list = [a_answer,b_answer,c_answer,d_answer]
        set_list = [set_a,set_b,set_c,set_d]
        cn = ConceptNet()

        for index,answer in enumerate(answer_list):
            self.assertEqual(answer,set(cn.search_relation(set_list[index][0][0],set_list[index][0][1])))

if __name__ == '__main__':
    unittest.main()
