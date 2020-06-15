# reasonable_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def reasonable(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('uber', 'labels', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('uber', 'IsA',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        engine.assert_('uber', 'IsA',
                       (rule.pattern(2).as_data(context),
                        rule.pattern(1).as_data(context),)),
        engine.assert_('uber', 'IsA',
                       (rule.pattern(3).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('reasonable')
  
  fc_rule.fc_rule('reasonable', This_rule_base, reasonable,
    (('uber', 'labels',
      (contexts.variable('concept1'),
       contexts.variable('concept2'),
       contexts.variable('concept3'),),
      False),),
    (contexts.variable('concept1'),
     contexts.variable('a'),
     contexts.variable('concept2'),
     contexts.variable('concept3'),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '../reasonable.krb'
Krb_lineno_map = (
    ((12, 16), (8, 8)),
    ((17, 19), (10, 10)),
    ((20, 22), (11, 11)),
    ((23, 25), (12, 12)),
)
