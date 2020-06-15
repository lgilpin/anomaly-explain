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
         ('', '', 'fc_example.krb'):
           [1582642184.574948, 'fc_example_fc.py'],
         ('', '', 'example.krb'):
           [1582642184.622607, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'family.kfb'):
           [1582642184.6421309, 'family.fbc'],
         ('', '', 'bc2_example.krb'):
           [1582642184.6881, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1582642184.72239, 'bc_example_bc.py'],
        },
        compiler_version)

