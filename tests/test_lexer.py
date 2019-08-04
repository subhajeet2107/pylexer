import unittest

from pylex.config.lexer_dict_config import LexerDictConfig
from pylex.token import Token
from pylex.lexer import PyLexer

class TestLexer(unittest.TestCase):

	def test_static_scan_algebra(self):
		config = self.get_algebra_config()
		tokens = PyLexer.scan(config, '2 +3 /4 -1 ')
		self.assertEqual(['number', 'plus', 'number', 'div', 'number', 'minus', 'number'],map(lambda x: x.get_name(), tokens))

		self.assertEqual(['2', '+', '3', '/', '4', '-', '1'], map(lambda x: x.get_value(), tokens))


	def get_algebra_config(self):
		return LexerDictConfig({
			'\\s' : '',
			'\\d+': 'number',
			'\\+' : 'plus',
			'-' : 'minus',
			'\\*' : 'mul',
			'/' : 'div',
		})

