"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from lmdo import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=lmdo', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'lmdo',
    version = __version__,
    description = 'CLI tools for microservices automation using AWS Lambda function',
    long_description = long_description,
    url = 'https://github.com/liangrog/lmdauto',
    author = 'Roger Liang',
    author_email = 'pinguroger@gmail.com',
    license = 'APACHE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'boto3', 'PyYAML', 'jinja2'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'lmdo=lmdo.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
