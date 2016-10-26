#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015-2016 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
#
# License: MIT
#

"""This module exports the PHPLint plugin class."""

from SublimeLinter.lint import Linter


class PHPLint(Linter):
    """Provides an interface to the phplint executable."""

    syntax = ('php', 'html')

    version_args = '--version'
    version_re = r'PHPLint (?P<version>\d+\.\d+)'
    version_requirement = '>= 2.0'
    regex = (
        r'(?i)^(?:'
        r'\t.*?\r?\n)?'
        r'==== (?P<line>\d+):(?P<col>.*): '
        r'(?:(?P<error>error)|(?P<warning>warning|notice)): '
        r'(?P<message>[^`\r\n]*(?:`(?P<near>[^\']+)\')?[^\r\n]*)'
    )
    multiline = True
    tempfile_suffix = 'php'

    def cmd(self):
        """Return the command line to execute."""

        """Get settings for PHPLinter"""
        view_settings = self.get_view_settings(inline=True)
        php_version = \
            view_settings.get('php_version', 5)

        cmd = 'phpl --php-version'
        cmd += ' ' + php_version
        cmd += ' --print-path relative --print-column-number --tab-size 4 --no-overall'

        return cmd

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
