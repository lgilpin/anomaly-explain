# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'reasonable.krb'):
           [1582643718.325803, 'reasonable_fc.py'],
         ('', '', 'uber.kfb'):
           [1582643718.340747, 'uber.fbc'],
         ('', '', 'family_relations/fc_example.krb'):
           [1582643718.3753579, 'fc_example_fc.py'],
         ('', '', 'family_relations/example.krb'):
           [1582643718.418644, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'family_relations/family.kfb'):
           [1582643718.425906, 'family.fbc'],
         ('', '', 'family_relations/bc2_example.krb'):
           [1582643718.465695, 'bc2_example_bc.py'],
         ('', '', 'family_relations/bc_example.krb'):
           [1582643718.501528, 'bc_example_bc.py'],
        },
        compiler_version)

