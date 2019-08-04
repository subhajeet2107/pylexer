"""
 * This file is part of the subhajeet2107/pylexer package.
 *
 * (c) Subhajeet Dey <subhajeet2107@gmail.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
"""
from pylex.config.lexer_config import LexerConfig
from pylex.config.token_defination import TokenDefination

class LexerDictConfig(LexerConfig):
	"""
	Lexer Configuration using a dictionary
	"""

	def __init__(self, token_definations={}):
		self.definations = []

		for k,v in token_definations.items():
			if type(v) == TokenDefination:
				self.add_token_defination(v)
			else:
				self.add_token_defination(TokenDefination(v, k))


	def add_token_defination(self, token_defination):
		self.definations.append(token_defination)

	def get_token_definations(self):
		return self.definations


		