#!/usr/bin/env python

import unittest
import tempfile
import shutil
import textflow


class TestSimplePipeline(unittest.TestCase):
    def test_action_glob_with_one_parameter(self):
        tmp_dir = tempfile.mkdtemp()
        plugins = ['glob']
        result = textflow.process(plugins, [tmp_dir])
        try:
            self.assertEqual(result, [tmp_dir])
        finally:
            shutil.rmtree(tmp_dir)


    def test_action_glob_with_two_parameters_without_asterisk_should_return_a_list_with_those_parameters(self):
        tmp_dir_1 = tempfile.mkdtemp()
        tmp_dir_2 = tempfile.mkdtemp()
        plugins = ['glob']
        result = textflow.process(plugins, [tmp_dir_1, tmp_dir_2])
        try:
            self.assertEqual(result, [tmp_dir_1, tmp_dir_2])
        finally:
            shutil.rmtree(tmp_dir_1)
            shutil.rmtree(tmp_dir_2)


    def test_action_glob_with_two_equal_parameters(self):
        tmp_dir = tempfile.mkdtemp()
        plugins = ['glob']
        result = textflow.process(plugins, [tmp_dir, tmp_dir])
        try:
            self.assertEqual(result, [tmp_dir])
        finally:
            shutil.rmtree(tmp_dir)


unittest.main()
