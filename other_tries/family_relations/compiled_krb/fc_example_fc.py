# fc_example_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def son_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def daughter_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brothers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('brother1') != context.lookup_data('brother2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sisters(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sister1') != context.lookup_data('sister2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brother_and_sister(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            engine.assert_('family', 'siblings',
                           (rule.pattern(1).as_data(context),
                            rule.pattern(0).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def facts_for_bc_rules(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    engine.assert_('family', 'as_au',
                   (rule.pattern(0).as_data(context),
                    rule.pattern(1).as_data(context),)),
    engine.assert_('family', 'as_au',
                   (rule.pattern(2).as_data(context),
                    rule.pattern(3).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(4).as_data(context),
                    rule.pattern(5).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(6).as_data(context),
                    rule.pattern(7).as_data(context),)),
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def niece_or_nephew_and_aunt_or_uncle(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'as_au', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('family', 'as_nn', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    mark4 = context.mark(True)
                    if rule.pattern(0).match_data(context, context,
                            ('great',) * len(context.lookup_data('depth'))):
                      context.end_save_all_undo()
                      engine.assert_('family', 'nn_au',
                                     (rule.pattern(1).as_data(context),
                                      rule.pattern(2).as_data(context),
                                      rule.pattern(0).as_data(context),
                                      rule.pattern(3).as_data(context),
                                      rule.pattern(4).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
  finally:
    context.done()

def parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def great_grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def first_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('family', 'cousins',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),
                                rule.pattern(2).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def nth_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                mark3 = context.mark(True)
                if rule.pattern(0).match_data(context, context,
                        context.lookup_data('n') + 1):
                  context.end_save_all_undo()
                  engine.assert_('family', 'cousins',
                                 (rule.pattern(1).as_data(context),
                                  rule.pattern(2).as_data(context),
                                  rule.pattern(0).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
  finally:
    context.done()

def how_related_child_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_parent_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_siblings(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'siblings', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'how_related',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def how_related_nn_au(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_au_nn(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                nth(context.lookup_data('n'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(3).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_removed_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def how_related_cousins_removed(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_example')
  
  fc_rule.fc_rule('son_of', This_rule_base, son_of,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('son'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('daughter_of', This_rule_base, daughter_of,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('daughter'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('brothers', This_rule_base, brothers,
    (('family', 'son_of',
      (contexts.variable('brother1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother1'),
     contexts.variable('brother2'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('sisters', This_rule_base, sisters,
    (('family', 'daughter_of',
      (contexts.variable('sister1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister1'),
     contexts.variable('sister2'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('brother_and_sister', This_rule_base, brother_and_sister,
    (('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother'),
     contexts.variable('sister'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('facts_for_bc_rules', This_rule_base, facts_for_bc_rules,
    (),
    (pattern.pattern_literal('brother'),
     pattern.pattern_literal('uncle'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('aunt'),
     pattern.pattern_literal('son'),
     pattern.pattern_literal('nephew'),
     pattern.pattern_literal('daughter'),
     pattern.pattern_literal('niece'),))
  
  fc_rule.fc_rule('niece_or_nephew_and_aunt_or_uncle', This_rule_base, niece_or_nephew_and_aunt_or_uncle,
    (('family', 'child_parent',
      (contexts.variable('nn'),
       contexts.variable('parent'),
       contexts.variable('depth'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'siblings',
      (contexts.variable('parent'),
       contexts.variable('au'),
       contexts.variable('sibling_type'),
       contexts.anonymous('_'),),
      False),
     ('family', 'as_au',
      (contexts.variable('sibling_type'),
       contexts.variable('au_type'),),
      False),
     ('family', 'as_nn',
      (contexts.variable('child_type'),
       contexts.variable('nn_type'),),
      False),),
    (contexts.variable('greats'),
     contexts.variable('nn'),
     contexts.variable('au'),
     contexts.variable('au_type'),
     contexts.variable('nn_type'),))
  
  fc_rule.fc_rule('parent_and_child', This_rule_base, parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.variable('parent_type'),
       contexts.variable('child_type'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('parent'),
     pattern.pattern_literal(()),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('grand_parent_and_child', This_rule_base, grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('parent'),
       contexts.variable('grand_parent'),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_literal(('grand',)),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('great_grand_parent_and_child', This_rule_base, great_grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('grand_child'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('grand_child'),
       contexts.variable('grand_parent'),
       pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('first_cousins', This_rule_base, first_cousins,
    (('family', 'child_parent',
      (contexts.variable('cousin1'),
       contexts.variable('sibling1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'siblings',
      (contexts.variable('sibling1'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('cousin2'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_literal(1),))
  
  fc_rule.fc_rule('nth_cousins', This_rule_base, nth_cousins,
    (('family', 'child_parent',
      (contexts.variable('next_cousin1'),
       contexts.variable('cousin1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('next_cousin2'),
       contexts.variable('cousin2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('next_n'),
     contexts.variable('next_cousin1'),
     contexts.variable('next_cousin2'),))
  
  fc_rule.fc_rule('how_related_child_parent', This_rule_base, how_related_child_parent,
    (('family', 'child_parent',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_parent_child', This_rule_base, how_related_parent_child,
    (('family', 'child_parent',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_siblings', This_rule_base, how_related_siblings,
    (('family', 'siblings',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('person1'),
     contexts.variable('person2'),
     pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),))
  
  fc_rule.fc_rule('how_related_nn_au', This_rule_base, how_related_nn_au,
    (('family', 'nn_au',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_au_nn', This_rule_base, how_related_au_nn,
    (('family', 'nn_au',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_cousins', This_rule_base, how_related_cousins,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'),), None),))
  
  fc_rule.fc_rule('how_related_removed_cousins', This_rule_base, how_related_removed_cousins,
    (('family', 'child_parent',
      (contexts.variable('removed_cousin1'),
       contexts.variable('cousin1'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('removed_cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))
  
  fc_rule.fc_rule('how_related_cousins_removed', This_rule_base, how_related_cousins_removed,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('removed_cousin2'),
       contexts.variable('cousin2'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('cousin1'),
     contexts.variable('removed_cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '../fc_example.krb'
Krb_lineno_map = (
    ((12, 16), (33, 33)),
    ((17, 21), (35, 35)),
    ((22, 26), (36, 36)),
    ((35, 39), (40, 40)),
    ((40, 44), (42, 42)),
    ((45, 49), (43, 43)),
    ((58, 62), (48, 48)),
    ((63, 67), (49, 49)),
    ((68, 68), (50, 50)),
    ((69, 73), (52, 52)),
    ((82, 86), (56, 56)),
    ((87, 91), (57, 57)),
    ((92, 92), (58, 58)),
    ((93, 97), (60, 60)),
    ((106, 110), (64, 64)),
    ((111, 115), (65, 65)),
    ((116, 120), (67, 67)),
    ((121, 125), (68, 68)),
    ((134, 136), (78, 78)),
    ((137, 139), (79, 79)),
    ((140, 142), (80, 80)),
    ((143, 145), (81, 81)),
    ((154, 158), (85, 85)),
    ((159, 163), (86, 86)),
    ((164, 168), (87, 87)),
    ((169, 173), (88, 88)),
    ((176, 176), (89, 89)),
    ((178, 183), (91, 91)),
    ((194, 198), (97, 97)),
    ((199, 204), (99, 99)),
    ((213, 217), (103, 103)),
    ((218, 222), (104, 104)),
    ((223, 228), (108, 109)),
    ((237, 241), (113, 113)),
    ((242, 246), (115, 116)),
    ((247, 252), (118, 119)),
    ((261, 265), (123, 123)),
    ((266, 270), (124, 124)),
    ((271, 275), (125, 125)),
    ((276, 279), (127, 127)),
    ((288, 292), (131, 131)),
    ((293, 297), (132, 132)),
    ((298, 302), (133, 133)),
    ((305, 305), (134, 134)),
    ((307, 310), (136, 136)),
    ((321, 325), (140, 140)),
    ((328, 328), (141, 141)),
    ((330, 333), (143, 143)),
    ((344, 348), (159, 159)),
    ((351, 351), (160, 160)),
    ((353, 356), (162, 162)),
    ((367, 371), (166, 166)),
    ((372, 375), (168, 168)),
    ((384, 388), (172, 172)),
    ((391, 391), (173, 173)),
    ((393, 396), (175, 175)),
    ((407, 411), (182, 182)),
    ((414, 414), (183, 183)),
    ((416, 419), (185, 185)),
    ((430, 434), (189, 189)),
    ((437, 437), (190, 190)),
    ((439, 442), (192, 192)),
    ((453, 457), (196, 196)),
    ((458, 462), (197, 197)),
    ((465, 465), (198, 198)),
    ((469, 469), (199, 199)),
    ((471, 474), (201, 202)),
    ((487, 491), (206, 206)),
    ((492, 496), (207, 207)),
    ((499, 499), (208, 208)),
    ((503, 503), (209, 209)),
    ((505, 508), (211, 212)),
)
