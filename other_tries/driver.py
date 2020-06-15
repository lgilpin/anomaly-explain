from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('family.how_related($person1, $person2, $relationship)')
reasonable_goal = goal.compile('facts.reasonable()')

def reasonable_snapshot_test():
    """
    Checks reasonability rules for a single instance: a picture, a point in time, etc. 
    """
    engine.reset()

    start_time = time.time()
    engine.activate('reasonable')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    with fc_goal.prove(engine, person1=person1) as gen:
        for vars, plan in gen:
            print("%s, %s are %s"% \
                    (person1, vars['person2'], vars['relationship']))
    prove_time = time.time() - fc_end_time
    print("done")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec"% \
          (fc_time, engine.get_kb('uber').get_stats()[2] / fc_time))

def reasonable_test_over_time():
    """
    Checks for reasonability over a scene or time series
    """
    return 

import types

def make_pattern(x):
    if isinstance(x, types.StringTypes):
        if x[0] == '$': return contexts.variable(x[1:])
        return pattern.pattern_literal(x)
    if isinstance(x, (tuple, list)):
        return pattern.pattern_tuple(tuple(make_pattern(element)
                                             for element in x))
    return pattern.pattern_literal(x)
