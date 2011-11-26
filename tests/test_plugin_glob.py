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
import shutil
import pypelinin


class TestGlobPlugin(unittest.TestCase):
    def test_invalid_plugin_should_raise_InvalidPluginException(self):
        with self.assertRaises(pypelinin.InvalidPluginException):
            pypelinin.process(['this_plugin_does_not_exist'])


    def test_plugin_glob_with_one_parameter(self):
        tmp_dir = tempfile.mkdtemp()
        plugins = ['glob']
        expected_result = pypelinin.process(plugins, [tmp_dir])
        try:
            self.assertEquals(expected_result, [tmp_dir])
        finally:
            shutil.rmtree(tmp_dir)


    def test_plugin_glob_with_two_parameters_without_asterisk_should_return_a_list_with_those_parameters(self):
        tmp_dir_1 = tempfile.mkdtemp()
        tmp_dir_2 = tempfile.mkdtemp()
        plugins = ['glob']
        expected_result = pypelinin.process(plugins, [tmp_dir_1, tmp_dir_2])
        try:
            self.assertEquals(len(expected_result), 2)
            self.assertItemsEqual(expected_result, [tmp_dir_1, tmp_dir_2])
        finally:
            shutil.rmtree(tmp_dir_1)
            shutil.rmtree(tmp_dir_2)


    def test_plugin_glob_with_two_equal_parameters(self):
        tmp_dir = tempfile.mkdtemp()
        plugins = ['glob']
        expected_result = pypelinin.process(plugins, [tmp_dir, tmp_dir])
        try:
            self.assertEquals(len(expected_result), 1)
            self.assertEquals(expected_result, [tmp_dir])
        finally:
            shutil.rmtree(tmp_dir)
#TODO test using * on filenames -> return only one and return a lot of files
