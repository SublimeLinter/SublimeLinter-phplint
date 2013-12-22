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

    syntax = ('php', 'html', 'html 5')
    cmd = 'phplint --print-path shortest --print-context --tab-size 4 --no-overall'
    regex = (
        r'(?i)^(?:'
        r'\t.*?\r?\n'
        r'\t(?P<col>.*) \\_ HERE\r?\n)?'
        r'(?P<filename>.+?):(?P<line>\d+): '
        r'(?:(?P<error>(?:fatal )?error)|(?P<warning>warning|notice)): '
        r'(?P<message>[^`\r\n]*(?:`(?P<near>[^\']+)\')?[^\r\n]*)'
    )
    multiline = True
    tempfile_suffix = 'php'

    def split_match(self, match):
        """Return the match with ` quotes transformed to '."""
        match, line, col, error, warning, message, near = super().split_match(match)

        if message == 'no PHP code found at all':
            match = None
        else:
            message = message.replace('`', '\'')

            # If the message contains a complaint about a function
            # and near looks like a function reference, remove the trailing
            # () so it can be found.
            if 'function \'' in message and near and near.endswith('()'):
                near = near[:-2]

        return match, line, col, error, warning, message, near
