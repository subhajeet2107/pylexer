"""
 * This file is part of the subhajeet2107/pylexer package.
 *
 * (c) Subhajeet Dey <subhajeet2107@gmail.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
"""
import re
from pylex.error.custom_exception import IllegalArgumentError

class TokenDefination:

	def __init__(self, name, regex, modifiers='i'):
		self.name = name
		delimiter = self.find_delimeter(regex)

		self.regex = '%s^%s%s%s' % (delimiter, regex, delimiter, modifiers)
		if re.match(self.regex, '') == False:
			raise IllegalArgumentError('Invalid regex for token %s : %s' % (name, regex))


	def get_regex(self):
		return self.regex

	def get_name(self):
		return self.name

	def find_delimeter(self, regex):
		choices = ['/', '|', '#', '~', '@']
		for choice in choices:
			if choice not in regex:
				return choice

		raise IllegalArgumentError('Unable to determine delimiter for regex %s' % (regex))

