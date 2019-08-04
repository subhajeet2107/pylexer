"""
 * This file is part of the subhajeet2107/pylexer package.
 *
 * (c) Subhajeet Dey <subhajeet2107@gmail.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
"""

import abc, six

@six.add_metaclass(abc.ABCMeta)
class LexerConfig:
    """
    Lexer Config base class for all clases to implement
    """

    @abc.abstractmethod
    def get_token_definations():
        pass