from setuptools import find_packages, setup

setup(
    name="vecnet.simulation",
    version="0.1",
    description="Library for simulation models in VecNet",
    author='Center for Research Computing, University of Notre Dame',
    packages=find_packages(),
    namespace_packages=['vecnet', ],
)
