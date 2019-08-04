pylexer
==========================
A python implementation of a lexical analyzer which supports full scan, state based lexing and lookahead


[![Build Status](https://travis-ci.org/subhajeet2107/pylexer.svg?branch=master)](https://travis-ci.org/subhajeet2107/pylexer) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![PyPI version](https://badge.fury.io/py/pylexer.svg)](https://badge.fury.io/py/pylexer) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

> **Warning**
> This is not a GENERATOR like classical lexer is. It does not produce any python code. It's a simple plain scanner
> of the given input string and tokenizer into given set of tokens by matching regular expressions.
> Thus, at runtime you can change the token definition and use one same code for any token set

## Installation

Install in your project with pip:

```bash
pip install pylexer
```

## Usage

An example use:

```python

from pylexer import PyLexer
config = {
	'\\s' :'',
    '\\d+' :'number',
    '\\+' : 'plus',
    '-': 'minus',
    '\\*' : 'mul',
    '/' : 'div',
}
#Static Scan method that returns list of tokens
tokens = PyLexer.scan(config, '2 + 3')
map(lambda x:x.get_name(), tokens)

#PyLexer Config is a dict, so you can also use it like
lexer = PyLexer()
lexer.set_input('2 + 3')
lexer.move_next()
while lexer.get_look_ahead():
	print(lexer.get_look_ahead().get_name())
	lexer.move_next()


```

## Token Definition
Tokens are defined with ```TokenDefinition``` class that holds token name and regular expression. Token name can be empty, and in that case lexer will ignore/skip such tokens

## Lexer Configuration
The lexer configuration holds a list of all token definitions. With LexerDictConfig it can be easily created from an array where keys are regular expressions and values are names of tokens

## Full scan
Pylexer's static scan method can be used to scan given input string and returns a list of tokens, Pylexer can also be used to walk through scanned tokens with single look ahead

## License

MIT license. See `LICENSE.md` for more information.

## Contributors
Pylexer is inspired from PHP's Lexer(https://github.com/tmilos/lexer) and takes code heavily from doctrine API, all credits due with Milos Tomic
