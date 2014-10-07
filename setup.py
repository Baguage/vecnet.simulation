from setuptools import find_packages, setup

def read_file(name):
    with open(name, 'r') as f:
        return f.read()

setup(
    name="vecnet.simulation",
    version="0.1",
    description="Library for simulation models in VecNet",
    long_description=read_file('README.rst'),
    author='Center for Research Computing, University of Notre Dame',
    packages=find_packages(),
    namespace_packages=['vecnet', ],
)
