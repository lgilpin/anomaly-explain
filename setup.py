from setuptools import setup

setup(
    name='ADE_Engine',
    version='1.0',
    description='ADE Explanation Engine',
    url='https://github.com/lgilpin/anomaly-explain',
    packages=['commonsense', 'monitor', 'old_monitor', 'other_tries', 'pkg_scramble', 'reasoning', 'sensor', 'synthesizer'],
    install_requires=['certifi', 'charset-normalizer', 'idna', 'numpy', 'pandas', 'pip', 'python-dateutil', 'pytz', 'pyzmq', 'requests', 'six', 'wheel'],
    classifiers=[]
)