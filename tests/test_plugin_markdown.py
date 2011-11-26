#!/usr/bin/env python
# coding: utf-8

# Copyright 2011 Álvaro Justen
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import tempfile
import os
import pypelinin


class TestMarkdownPlugin(unittest.TestCase):
    def test_simple(self):
        tmp_fd = tempfile.NamedTemporaryFile(delete=False)
        tmp_fd.write('testing\n=======')
        tmp_fd.close()

        plugins = ['markdown']
        result_filenames = pypelinin.process(plugins, [tmp_fd.name])
        expected_output = '<h1>testing</h1>'
        out_fd = open(result_filenames[0])

        self.assertEquals(out_fd.read(), expected_output)

        out_fd.close()
        os.remove(result_filenames[0])
        os.remove(tmp_fd.name)


    def test_more_than_one_file(self):
        tmp_fd_1 = tempfile.NamedTemporaryFile(delete=False)
        tmp_fd_1.write('testing 1\n=========')
        tmp_fd_1.close()

        tmp_fd_2 = tempfile.NamedTemporaryFile(delete=False)
        tmp_fd_2.write('testing 2\n=========')
        tmp_fd_2.close()

        plugins = ['markdown']
        expected_filenames = [tmp_fd_1.name, tmp_fd_2.name]
        result_filenames = pypelinin.process(plugins, expected_filenames)
        out_fd_1 = open(result_filenames[0])
        out_fd_2 = open(result_filenames[1])

        self.assertEquals(out_fd_1.read(), '<h1>testing 1</h1>')
        self.assertEquals(out_fd_2.read(), '<h1>testing 2</h1>')

        out_fd_1.close()
        out_fd_2.close()
        os.remove(tmp_fd_1.name)
        os.remove(tmp_fd_2.name)
        os.remove(result_filenames[0])
        os.remove(result_filenames[1])
