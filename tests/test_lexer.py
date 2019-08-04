import unittest

from pylex.config.lexer_dict_config import LexerDictConfig
from pylex.token import Token
from pylex.lexer import PyLexer

class TestLexer(unittest.TestCase):

	def get_algebra_config(self):
		return LexerDictConfig({
			'\\s' : '',
			'\\d+': 'number',
			'\\+' : 'plus',
			'-' : 'minus',
			'\\*' : 'mul',
			'/' : 'div',
		})

	def test_static_scan_algebra(self):
		config = self.get_algebra_config()
		tokens = PyLexer.scan(config, '2 +3 /4 -1 ')
		self.assertEqual(['number', 'plus', 'number', 'div', 'number', 'minus', 'number'],map(lambda x: x.get_name(), tokens))

		self.assertEqual(['2', '+', '3', '/', '4', '-', '1'], map(lambda x: x.get_value(), tokens))


	def test_move_next(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		self.assertIsNone(lexer.get_look_ahead())
		self.assertIsNone(lexer.get_token())
		self.assertTrue(lexer.move_next())
		self.assertIsInstance(lexer.get_look_ahead(), Token)
		self.assertEqual('number', lexer.get_look_ahead().get_name())
		self.assertEqual('2', lexer.get_look_ahead().get_value())
		self.assertIsNone(lexer.get_token())
		self.assertTrue(lexer.move_next())
		self.assertIsInstance(lexer.get_look_ahead(), Token)
		self.assertEqual('plus', lexer.get_look_ahead().get_name())
		self.assertEqual('+', lexer.get_look_ahead().get_value())
		self.assertIsNone(lexer.get_token())
		self.assertEqual('number', lexer.get_look_ahead().get_name())
		self.assertEqual('2', lexer.get_look_ahead().get_value())
		self.assertTrue(lexer.move_next())
		self.assertTrue(lexer.move_next())
		self.assertTrue(lexer.move_next())
		self.assertTrue(lexer.move_next())
		self.assertTrue(lexer.move_next())
		self.assertIsInstance(lexer.get_look_ahead(), Token)
		self.assertEqual('number', lexer.get_look_ahead().get_name())
		self.assertEqual('1', lexer.get_look_ahead().get_value())
		self.assertIsNone(lexer.get_token())
		self.assertEqual('minus', lexer.get_look_ahead().get_name())
		self.assertEqual('-', lexer.get_look_ahead().get_value())
		self.assertFalse(lexer.move_next())
		self.assertIsNone(lexer.get_look_ahead())
		self.assertIsInstance(lexer.get_look_ahead(), Token)
		self.assertEqual('number', lexer.get_look_ahead().get_name())
		self.assertEqual('1', lexer.get_look_ahead().get_value())
		self.assertFalse(lexer.move_next())
		self.assertIsNone(lexer.get_token())
		self.assertIsNone(lexer.get_look_ahead())


	def test_peek(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		lexer.move_next()
		lexer.move_next()

		token = lexer.peeks()
		self.assertEqual('3', token.get_value())

		token = lexer.peeks()
		self.assertEqual('/', token.get_value())

		lexer.move_next()
		token = lexer.peeks()
		self.assertEqual('/', token.get_value())

		lexer.reset_peek()
		token = lexer.peeks()
		self.assertEqual('/', token.get_value())


	def test_skip_until(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		lexer.move_next()
		lexer.skip_until('minus')

		self.assertEqual('minus', lexer.get_look_ahead().get_name())
		self.assertEqual('4', lexer.get_token().get_value())


	def test_is_next_token(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		self.assertFalse(lexer.is_next_token('number'))

		lexer.move_next()
		self.assertTrue(lexer.is_next_token('number'))

		lexer.move_next()
		self.assertTrue(lexer.is_next_token_any(['minus','plus']))


	def test_reset_position(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		lexer.move_next()
		lexer.move_next()
		lexer.move_next()
		lexer.move_next()
		lexer.move_next()

		lexer.reset_position()
		lexer.move_next()

		self.assertEqual('2', lexer.get_look_ahead().get_value())

	def test_glimpse(self):
		lexer = PyLexer(self.get_algebra_config())
		lexer.set_input('2 +3 /4 -1 ')

		lexer.move_next()

		self.assertEqual('+', lexer.glimpse().get_value())
		self.assertEqual('+', lexer.glimpse().get_value())
		self.assertEqual('+', lexer.glimpse().get_value())
















