#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by roadhump
# Copyright (c) 2014 roadhump
# Forked for textlint by Joey Baker
# Copyright (c) 2016 Joey Baker
#
# License: MIT
#

"""This module exports the Textlint plugin class."""

import sublime
import os
import re
from SublimeLinter.lint import NodeLinter, util


class Textlint(NodeLinter):
    """Provides an interface to textlint."""

    syntax = (
        'markdown',
        'text',
        'plain text',
        'Markdown GFM',
        'MarkdownEditing',
        'Markdown Extended',
        'Markdown',
        'MultiMarkdown'
    )
    cmd = ('textlint', '--format', 'compact', '--stdin', '--stdin-filename', '@')
    npm_name='textlint'
    # executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 5.3.0'
    regex = (
        r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) - '
        r'(?P<message>.+)'
    )
    # multiline = False
    line_col_base = (1, 1)
    # tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    # selectors = {}
    # word_re = None
    # defaults = {}
    # inline_settings = None
    # inline_overrides = None
    comment_re = r'\s*/[/*]'
    config_fail_regex = re.compile(r'^Cannot read config file: .*\r?\n')
    crash_regex = re.compile(
        r'^(.*?)\r?\n\w*Error: \1',
        re.MULTILINE
    )

    def find_errors(self, output):
        """
        Parse errors from linter's output.

        We override this method to handle parsing textlint crashes.
        """

        match = self.config_fail_regex.match(output)
        if match:
            return [(match, 0, None, "Error", "", match.group(0), None)]

        match = self.crash_regex.match(output)
        if match:
            msg = "TextLint crashed: %s" % match.group(1)
            return [(match, 0, None, "Error", "", msg, None)]

        return super().find_errors(output)

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method to silent warning by .textlintignore settings.
        """

        match, line, col, error, warning, message, near = super().split_match(match)
        if message and message == 'File ignored because of your .textlintignore file. Use --no-ignore to override.':
            return match, None, None, None, None, '', None

        return match, line, col, error, warning, message, near

    def communicate(self, cmd, code=None):
        """Run an external executable using stdin to pass code and return its output."""
        relfilename = self.filename

        if '__RELATIVE_TO_FOLDER__' in cmd:

            window = self.view.window()

            # can't get active folder, it will work only if there is one folder in project
            if int(sublime.version()) >= 3080 and len(window.folders()) < 2:

                vars = window.extract_variables()

                if 'folder' in vars:
                    relfilename = os.path.relpath(relfilename, vars['folder'])

            cmd[cmd.index('__RELATIVE_TO_FOLDER__')] = relfilename

        elif not code:
            cmd.append(relfilename)

        return super().communicate(cmd, code)
