from setuptools import find_packages, setup

def read_file(name):
    with open(name, 'r') as f:
        return f.read()

setup(
    name="vecnet.simulation",
    version="0.1",

    # Metadata for PyPI
    description="Library for simulation models in VecNet",
    long_description=read_file('README.rst'),
    author="VecNet Team, Center for Research Computing, University of Notre Dame",
    author_email="dev@vecnet.org",
    url="https://github.com/jimm-domingo/vecnet.simulation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    packages=find_packages(),
    namespace_packages=['vecnet', ],
)
