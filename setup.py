from setuptools import setup, find_packages

version = '1.0.0'
license = 'MIT License'

setup(
    name = 'pylexer',
    version = version,
    license = license,
    author = 'Subhajeet Dey',
    author_email = 'subhajeet2107@gmail.com',
    url = 'https://github.com/subhajeet2107/pylexer/',
    long_description_content_type='text/markdown',
    description = 'A python implementation of a lexical analyzer which supports full scan, state based lexing and lookahead',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        'pytest',
        'six',
    ],
    test_suite = 'tests',
    entry_points = {
	    'console_scripts': [
	        'pylexer = pylexer.__main__:main',
	    ]
	}
)
