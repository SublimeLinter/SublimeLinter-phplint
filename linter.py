#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the PHPLint plugin class."""

from SublimeLinter.lint import Linter


class PHPLint(Linter):

    """Provides an interface to the phplint executable."""

    syntax = ('php', 'html')
    cmd = 'phplint --print-path shortest --print-context --tab-size 4 --no-overall'
    regex = (
        r'^(?i)(?:'
        r'\t.*?\r?\n'
        r'\t(?P<col>.*)\\_ HERE\r?\n)?'
        r'(?P<filename>.+?):(?P<line>\d+): '
        r'(?:(?P<error>(?:fatal )?error)|(?P<warning>warning|notice)): '
        r'(?P<message>[^`\r\n]*(?:`(?P<near>[^\']+)\')?[^\r\n]*)$'
    )
    multiline = True
    tempfile_suffix = 'php'
    selectors = {
        'html': 'source.php.embedded.block.html'
    }

    def split_match(self, match):
        """Return the match with ` quotes transformed to '."""
        match, line, col, error, warning, message, near = super().split_match(match)

        message = message.replace('`', '\'')

        return match, line, col, error, warning, message, near
