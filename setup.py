from genetic_algorithm import __version__
from setuptools import setup

long_description = ''
with open('./README.md') as f:
    long_description = f.read()

setup(name='genetic_algorithm',
    version=__version__,
    description='Python package for class-driven genetic algorithm optimization.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NFI-Solutions-Engineering/genetic-algorithm',
    author='Chris Pryer',
    author_email='chris.pryer@nfiindustries.com',
    license='PUBLIC',
    packages=['genetic_algorithm'],
    zip_safe=False)
