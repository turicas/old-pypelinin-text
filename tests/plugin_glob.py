#!/usr/bin/env python

import unittest
import tempfile
import shutil
import sys

sys.path.insert(0, '..')
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

unittest.main()
