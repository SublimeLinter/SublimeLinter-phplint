from SublimeLinter.lint import PhpLinter


class PHPLint(PhpLinter):
    cmd = 'phpl --print-path relative --print-column-number --no-overall ${args} ${file}'
    regex = (
        r'(?i)^(?:'
        r'\t.*?\r?\n)?'
        r'==== (?P<line>\d+):(?P<col>.*): '
        r'(?:(?P<error>error)|(?P<warning>warning|notice)): '
        r'(?P<message>[^`\r\n]*(?:`(?P<near>[^\']+)\')?[^\r\n]*)'
    )
    multiline = True
    tempfile_suffix = '-'
    defaults = {
        'selector': 'embedding.php, source.php'
    }

    def split_match(self, match):
        """Return the match with ` quotes transformed to '."""
        match, line, col, error, warning, message, near = super().split_match(match)

        if message == 'no PHP code found at all':
            return None

        message = message.replace('`', '\'')

        # If the message contains a complaint about a function
        # and near looks like a function reference, remove the trailing
        # () so it can be found.
        if 'function \'' in message and near and near.endswith('()'):
            near = near[:-2]

        return match, line, col, error, warning, message, near
