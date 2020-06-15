# bc2_example_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def father_son(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.father_son: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mother_son(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.mother_son: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def father_daughter(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.father_daughter: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mother_daughter(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.mother_daughter: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brothers(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.brothers: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.brothers: got unexpected plan from when clause 2"
                if context.lookup_data('brother1') != context.lookup_data('brother2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sisters(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.sisters: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.sisters: got unexpected plan from when clause 2"
                if context.lookup_data('sister1') != context.lookup_data('sister2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brother_sister(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.brother_sister: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.brother_sister: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sister_brother(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.sister_brother: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.sister_brother: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_au_brother_uncle(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_au_sister_aunt(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_nn_son_nephew(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_nn_daughter_niece(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def niece_or_nephew_and_aunt_or_uncle_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.is_bound(contexts.variable('nn')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(1),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(3),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'as_au', context,
                                    (rule.pattern(6),
                                     rule.pattern(7),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'as_nn', context,
                                        (rule.pattern(4),
                                         rule.pattern(8),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 5"
                          mark6 = context.mark(True)
                          if rule.pattern(9).match_data(context, context,
                                  ('great',) * len(context.lookup_data('depth'))):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def niece_or_nephew_and_aunt_or_uncle_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if not context.is_bound(contexts.variable('nn')):
          with engine.prove(rule.rule_base.root_name, 'siblings', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(1),
                                 rule.pattern(5),
                                 rule.pattern(2),
                                 rule.pattern(6),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'as_au', context,
                                    (rule.pattern(3),
                                     rule.pattern(7),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'as_nn', context,
                                        (rule.pattern(6),
                                         rule.pattern(8),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 5"
                          mark6 = context.mark(True)
                          if rule.pattern(9).match_data(context, context,
                                  ('great',) * len(context.lookup_data('depth'))):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def parent_and_child(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.parent_and_child: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_parent_and_child_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.grand_parent_and_child_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(1),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(2),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.grand_parent_and_child_1: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_parent_and_child_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if not context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.grand_parent_and_child_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(0),
                                 rule.pattern(3),
                                 rule.pattern(5),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.grand_parent_and_child_2: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_parent_and_child_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.great_grand_parent_and_child_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(1),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(2),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.great_grand_parent_and_child_1: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_parent_and_child_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if not context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.great_grand_parent_and_child_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(0),
                                 rule.pattern(5),
                                 rule.pattern(3),
                                 rule.pattern(6),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.great_grand_parent_and_child_2: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def first_cousins(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.first_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.first_cousins: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                  (rule.pattern(4),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc2_example.first_cousins: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousins(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.nth_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.nth_cousins: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                  (rule.pattern(5),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc2_example.nth_cousins: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(6).match_data(context, context,
                            context.lookup_data('n') + 1):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_child_parent(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_child_parent: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_parent_child(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_parent_child: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_siblings(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'siblings', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_siblings: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_nn_au(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'nn_au', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_nn_au: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_au_nn(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'nn_au', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_au_nn: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_cousins(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'cousins', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_cousins: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_removed_cousins(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_removed_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.how_related_removed_cousins: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(6).match_data(context, context,
                        nth(context.lookup_data('n'))):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(7).match_data(context, context,
                          len(context.lookup_data('grand')) + 1):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_cousins_removed(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'cousins', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_cousins_removed: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.how_related_cousins_removed: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(6).match_data(context, context,
                        nth(context.lookup_data('n'))):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(7).match_data(context, context,
                          len(context.lookup_data('grand')) + 1):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc2_example')
  
  bc_rule.bc_rule('father_son', This_rule_base, 'child_parent',
                  father_son, None,
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   pattern.pattern_literal('father'),
                   pattern.pattern_literal('son'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('mother_son', This_rule_base, 'child_parent',
                  mother_son, None,
                  (contexts.variable('child'),
                   contexts.variable('mother'),
                   pattern.pattern_literal('mother'),
                   pattern.pattern_literal('son'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('father_daughter', This_rule_base, 'child_parent',
                  father_daughter, None,
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   pattern.pattern_literal('father'),
                   pattern.pattern_literal('daughter'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('mother_daughter', This_rule_base, 'child_parent',
                  mother_daughter, None,
                  (contexts.variable('child'),
                   contexts.variable('mother'),
                   pattern.pattern_literal('mother'),
                   pattern.pattern_literal('daughter'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('brothers', This_rule_base, 'siblings',
                  brothers, None,
                  (contexts.variable('brother1'),
                   contexts.variable('brother2'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother2'),))
  
  bc_rule.bc_rule('sisters', This_rule_base, 'siblings',
                  sisters, None,
                  (contexts.variable('sister1'),
                   contexts.variable('sister2'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister2'),))
  
  bc_rule.bc_rule('brother_sister', This_rule_base, 'siblings',
                  brother_sister, None,
                  (contexts.variable('sister'),
                   contexts.variable('brother'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother'),))
  
  bc_rule.bc_rule('sister_brother', This_rule_base, 'siblings',
                  sister_brother, None,
                  (contexts.variable('brother'),
                   contexts.variable('sister'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister'),))
  
  bc_rule.bc_rule('as_au_brother_uncle', This_rule_base, 'as_au',
                  as_au_brother_uncle, None,
                  (pattern.pattern_literal('brother'),
                   pattern.pattern_literal('uncle'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_au_sister_aunt', This_rule_base, 'as_au',
                  as_au_sister_aunt, None,
                  (pattern.pattern_literal('sister'),
                   pattern.pattern_literal('aunt'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_nn_son_nephew', This_rule_base, 'as_nn',
                  as_nn_son_nephew, None,
                  (pattern.pattern_literal('son'),
                   pattern.pattern_literal('nephew'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_nn_daughter_niece', This_rule_base, 'as_nn',
                  as_nn_daughter_niece, None,
                  (pattern.pattern_literal('daughter'),
                   pattern.pattern_literal('niece'),),
                  (),
                  ())
  
  bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle_1', This_rule_base, 'nn_au',
                  niece_or_nephew_and_aunt_or_uncle_1, None,
                  (contexts.variable('nn'),
                   contexts.variable('au'),
                   contexts.variable('greats'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),),
                  (),
                  (contexts.variable('nn'),
                   contexts.variable('parent'),
                   contexts.variable('depth'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('au'),
                   contexts.variable('sibling_type'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),
                   contexts.variable('greats'),))
  
  bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle_2', This_rule_base, 'nn_au',
                  niece_or_nephew_and_aunt_or_uncle_2, None,
                  (contexts.variable('nn'),
                   contexts.variable('au'),
                   contexts.variable('greats'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),),
                  (),
                  (contexts.variable('au'),
                   contexts.variable('parent'),
                   contexts.anonymous('_'),
                   contexts.variable('sibling_type'),
                   contexts.variable('nn'),
                   contexts.variable('depth'),
                   contexts.variable('child_type'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),
                   contexts.variable('greats'),))
  
  bc_rule.bc_rule('parent_and_child', This_rule_base, 'child_parent',
                  parent_and_child, None,
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   pattern.pattern_literal(()),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('grand_parent_and_child_1', This_rule_base, 'child_parent',
                  grand_parent_and_child_1, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_literal(('grand',)),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),))
  
  bc_rule.bc_rule('grand_parent_and_child_2', This_rule_base, 'child_parent',
                  grand_parent_and_child_2, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_literal(('grand',)),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('parent'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),
                   contexts.anonymous('_'),
                   contexts.variable('child'),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('great_grand_parent_and_child_1', This_rule_base, 'child_parent',
                  great_grand_parent_and_child_1, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('grand_child'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),))
  
  bc_rule.bc_rule('great_grand_parent_and_child_2', This_rule_base, 'child_parent',
                  great_grand_parent_and_child_2, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('parent'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),
                   contexts.anonymous('_'),
                   contexts.variable('child'),
                   pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('first_cousins', This_rule_base, 'cousins',
                  first_cousins, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_literal(1),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('sibling1'),
                   contexts.anonymous('_'),
                   contexts.variable('sibling2'),
                   contexts.variable('cousin2'),))
  
  bc_rule.bc_rule('nth_cousins', This_rule_base, 'cousins',
                  nth_cousins, None,
                  (contexts.variable('next_cousin1'),
                   contexts.variable('next_cousin2'),
                   contexts.variable('next_n'),),
                  (),
                  (contexts.variable('next_cousin1'),
                   contexts.variable('cousin1'),
                   contexts.anonymous('_'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('next_cousin2'),
                   contexts.variable('next_n'),))
  
  bc_rule.bc_rule('how_related_child_parent', This_rule_base, 'how_related',
                  how_related_child_parent, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_parent_child', This_rule_base, 'how_related',
                  how_related_parent_child, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_siblings', This_rule_base, 'how_related',
                  how_related_siblings, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),))
  
  bc_rule.bc_rule('how_related_nn_au', This_rule_base, 'how_related',
                  how_related_nn_au, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_au_nn', This_rule_base, 'how_related',
                  how_related_au_nn, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_cousins', This_rule_base, 'how_related',
                  how_related_cousins, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'),), None),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('nth'),))
  
  bc_rule.bc_rule('how_related_removed_cousins', This_rule_base, 'how_related',
                  how_related_removed_cousins, None,
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),),
                  (),
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin1'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('nth'),
                   contexts.variable('r1'),))
  
  bc_rule.bc_rule('how_related_cousins_removed', This_rule_base, 'how_related',
                  how_related_cousins_removed, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('removed_cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('removed_cousin2'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('nth'),
                   contexts.variable('r1'),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '../bc2_example.krb'
Krb_lineno_map = (
    ((14, 18), (25, 25)),
    ((20, 27), (27, 27)),
    ((40, 44), (30, 30)),
    ((46, 53), (32, 32)),
    ((66, 70), (35, 35)),
    ((72, 79), (37, 37)),
    ((92, 96), (40, 40)),
    ((98, 105), (42, 42)),
    ((118, 122), (46, 46)),
    ((124, 131), (48, 48)),
    ((132, 139), (49, 49)),
    ((140, 140), (50, 50)),
    ((153, 157), (53, 53)),
    ((159, 166), (55, 55)),
    ((167, 174), (56, 56)),
    ((175, 175), (57, 57)),
    ((188, 192), (60, 60)),
    ((194, 201), (62, 62)),
    ((202, 209), (63, 63)),
    ((222, 226), (66, 66)),
    ((228, 235), (68, 68)),
    ((236, 243), (69, 69)),
    ((256, 260), (72, 72)),
    ((274, 278), (75, 75)),
    ((292, 296), (78, 78)),
    ((310, 314), (81, 81)),
    ((328, 332), (84, 84)),
    ((334, 334), (86, 86)),
    ((335, 344), (87, 87)),
    ((345, 353), (88, 88)),
    ((354, 360), (89, 89)),
    ((361, 367), (90, 90)),
    ((370, 370), (91, 91)),
    ((386, 390), (94, 94)),
    ((392, 392), (96, 96)),
    ((393, 401), (97, 97)),
    ((402, 411), (98, 98)),
    ((412, 418), (99, 99)),
    ((419, 425), (100, 100)),
    ((428, 428), (101, 101)),
    ((444, 448), (106, 106)),
    ((450, 458), (108, 108)),
    ((471, 475), (113, 113)),
    ((477, 477), (115, 115)),
    ((478, 486), (116, 116)),
    ((487, 495), (117, 117)),
    ((508, 512), (122, 122)),
    ((514, 514), (124, 124)),
    ((515, 523), (125, 125)),
    ((524, 532), (126, 126)),
    ((545, 549), (129, 130)),
    ((551, 551), (132, 132)),
    ((552, 560), (133, 133)),
    ((561, 570), (135, 135)),
    ((583, 587), (138, 139)),
    ((589, 589), (141, 141)),
    ((590, 598), (142, 142)),
    ((599, 608), (144, 144)),
    ((621, 625), (147, 147)),
    ((627, 635), (149, 149)),
    ((636, 644), (150, 150)),
    ((645, 653), (151, 151)),
    ((666, 670), (154, 154)),
    ((672, 680), (156, 156)),
    ((681, 688), (157, 157)),
    ((689, 697), (158, 158)),
    ((700, 700), (159, 159)),
    ((716, 720), (162, 162)),
    ((722, 731), (164, 164)),
    ((734, 734), (165, 165)),
    ((750, 754), (168, 168)),
    ((756, 765), (182, 182)),
    ((768, 768), (183, 183)),
    ((784, 788), (186, 186)),
    ((790, 798), (188, 188)),
    ((811, 815), (191, 191)),
    ((817, 826), (193, 193)),
    ((829, 829), (194, 194)),
    ((845, 849), (197, 197)),
    ((851, 860), (202, 202)),
    ((863, 863), (203, 203)),
    ((879, 883), (206, 206)),
    ((885, 892), (208, 208)),
    ((895, 895), (209, 209)),
    ((911, 915), (212, 212)),
    ((917, 926), (214, 214)),
    ((927, 934), (215, 215)),
    ((937, 937), (216, 216)),
    ((941, 941), (217, 217)),
    ((959, 963), (220, 220)),
    ((965, 972), (222, 222)),
    ((973, 982), (223, 223)),
    ((985, 985), (224, 224)),
    ((989, 989), (225, 225)),
)
