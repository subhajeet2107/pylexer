"""
 * This file is part of the subhajeet2107/pylexer package.
 *
 * (c) Subhajeet Dey <subhajeet2107@gmail.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
"""
import re
from pylex.config.lexer_config import LexerConfig
from pylex.error.custom_exception import IllegalArgumentError, UnknownTokenException

from pylex.token import Token

class PyLexer:

	def __init__(self, config):
		self.config = config

	@staticmethod
	def scan(config, input_string):
		tokens = []
		offset = 0
		position = 0
		matches = None

		while len(input_string):
			any_match = False

			for token_defination in config.get_token_definations():
				matches = re.search(token_defination.get_regex(), input_string, flags=re.IGNORECASE)
				if matches is not None:
					str_matched = matches.group(0)
					str_len = len(str_matched)

					if len(token_defination.get_name()) > 0:
						tokens.append(Token(token_defination.get_name(), str_matched, offset, position))
						position += 1

					input_string = input_string[:str_len]
					any_match = True
					offset += str_len
					break

			if not any_match:
				raise UnknownTokenException('At offset %s: %s' %( offset, input_string[0:16] + '...'))
		return tokens


	def get_input(self):
		return self.input

	def get_position(self):
		return self.position

	def get_look_ahead(self):
		return self.lookahead

	def get_token(self):
		return self.token

	def set_input(self, input_string):
		self.input = input_string
		self.reset()
		self.tokens = PyLexer.scan(self.config, input_string)

	def reset(self):
		self.position = 0
		self.peek = 0
		self.token = None
		self.lookahead = None

	def reset_position(self, position=0):
		self.position = position

	def is_next_token(self, token_name):
		return self.lookahead is not None and self.lookahead.get_name() == token_name

	def is_next_token_any(self, token_names):
		return self.lookahead is not None and self.lookahead.get_name() in token_names

	def move_next(self):
		self.peek = 0
		self.token = self.lookahead
		self.lookahead = self.tokens[self.position + 1] if self.tokens[self.position] else None
		return self.lookahead != None

	def skip_until(self, token_name):
		while self.lookahead != None and self.lookahead.get_name() != token_name:
			self.move_next()

	def skip_tokens(self, token_names):
		while self.lookahead != None and self.lookahead.get_name() in token_names:
			self.move_next()

	def peeks(self):
		if self.tokens[self.position + self.peek]:
			self.peek += 1
			return self.tokens[self.position + self.peek]
		else:
			return None


	def peek_while_tokens(self, token_names):
		token = self.peeks()
		while token:
			if token.get_name() not in token_names:
				break

		return token

	def glimpse(self):
		peek = self.peeks()
		self.peek = 0
		return peek




