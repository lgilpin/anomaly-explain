# this is a test of the create_sorted_events_file function given the

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import logical_classes as lc

event_list=lc.parse_file_to_event_list("/Users/Ariel/Documents/College/Research/anomaly-explain/datasets/PAX/output_feb25.txt")
lc.create_sorted_events_file(event_list)

print("test complete")