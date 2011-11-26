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
import random
import pypelinin


class TestIntegration(unittest.TestCase):
    def test_when_plugin_list_is_empty_ValueError_should_be_raised(self):
        with self.assertRaises(ValueError):
            result = pypelinin.process([], ['some string'])


    def test_when_input_is_not_list_should_raise_TypeError(self):
        with self.assertRaises(TypeError):
            result = pypelinin.process(['glob'], 'some string')


    def test_when_output_is_not_list_should_raise_TypeError(self):
        result = pypelinin.process(['glob'], ['some string'])
        self.assertEquals(type(result), type([]))


    def test_simple_pipe_with_2_plugins(self):
        tmp_fd = tempfile.NamedTemporaryFile(delete=False)
        random_chars = [chr(int(97 + random.random() * 26)) for x in range(20)]
        random_string = ''.join(random_chars)
        tmp_fd.write('%s\n%s' %  (random_string, '=' * len(random_string)))
        tmp_fd.close()
        tmp_filename = tmp_fd.name

        plugins = ['glob', 'markdown']
        result_filenames = pypelinin.process(plugins, [tmp_filename])
        expected_output_filename = tmp_filename + '.html'
        self.assertEquals(result_filenames[0], expected_output_filename)
        self.assertTrue(os.path.exists(expected_output_filename))

        expected_output = '<h1>%s</h1>' % random_string
        out_fd = open(result_filenames[0])
        self.assertEquals(out_fd.read(), expected_output)

        out_fd.close()
        os.remove(result_filenames[0])
        os.remove(tmp_fd.name)
