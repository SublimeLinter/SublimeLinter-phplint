#
# phplint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-phplint
# License: MIT
#

"""This module provides the PHPLint plugin class."""

import re

from SublimeLinter.lint import Linter


class PHPLint(Linter):

    """Provide an interface to the phplint executable."""

    language = ('php', 'html')
    cmd = 'phplint --print-path shortest --print-context --tab-size 4 --no-overall'
    regex = (
        r'^(?:'
        r'\t.*?\r?\n'
        r'\t(?P<col>.*)\\_ HERE\r?\n)?'
        r'(?P<filename>.+?):(?P<line>\d+): '
        r'(?:(?P<error>(?:fatal )?error)|(?P<warning>warning|notice)): '
        r'(?P<message>[^`\r\n]*(?P<near>`.+\')?[^\r\n]*)$'
    )
    multiline = True
    re_flags = re.IGNORECASE
    tempfile_suffix = 'php'
    selectors = {
        'html': 'source.php.embedded.block.html'
    }

    def split_match(self, match):
        """Return the match with ` quotes transformed to '."""
        match, line, col, error, warning, message, near = super().split_match(match)

        message = message.replace('`', '\'')

        if near:
            near = near.replace('`', '\'')

        return match, line, col, error, warning, message, near
