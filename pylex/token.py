"""
 * This file is part of the subhajeet2107/pylexer package.
 *
 * (c) Subhajeet Dey <subhajeet2107@gmail.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
"""
from pylex.error.custom_exception import IllegalArgumentError

class Token:
	"""
    Token Implementation class, which converts string to tokens, using lexer
	"""
	def __init__(self, name, value, offset, count):
		self.name = name
		self.value = value
		self.offset = offset
		self.position = count

	def get_position(self):
		return self.position

	def get_offset(self):
		return self.offset

	def get_name(self):
		return self.name

	def get_value(self):
		return self.value

	def is_token(self, token):
		if isinstance(token, self):
			return self.name == token.get_name()
		elif type(token) == str:
			return self.name == token
		else:
			raise InvalidArgumentException('Expected string or Token')
