#!/usr/bin/env python

import unittest
import tempfile
import os
import pypelinin


class TestJinjaPlugin(unittest.TestCase):
    def test_Template_with_block(self):
        tmp_fd_1 = tempfile.NamedTemporaryFile(delete=False)
        tmp_fd_2 = tempfile.NamedTemporaryFile(delete=False)
        tmp_fd_1.write('''
<html>
  <head>
    <title>Test page</title>
  </head>
  <body>
    {%% block content %%}
  </body>
</html>''')
        tmp_fd_2.write('''
{%% extends '%s' %%}
{%% block content %%}
Just testing Jinja.
{%% endblock %%}
''' % tmp_fd_1.name)
        tmp_fd_1.close()
        tmp_fd_2.close()

        plugins = ['jinja']
        parameters = [tmp_fd_1.name, tmp_fd_2.name]
        result_filenames = pypelinin.process(plugins, parameters)

        self.assertEquals(len(result_filenames), 1)

        expected_output = '''
<html>
  <head>
    <title>Test page</title>
  </head>
  <body>
    Just testing Jinja.
  </body>
</html>'''
        fd = open(result_filenames[0])
        self.assertEquals(fd.read(), expected_output)
        fd.close()

        os.remove(tmp_fd_1.name)
        os.remove(tmp_fd_2.name)
        os.remove(result_filenames[0])
