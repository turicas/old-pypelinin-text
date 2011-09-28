#!/usr/bin/env python

import unittest
import tempfile
import sys
import os
import random

sys.path.insert(0, '..')
import pypelinin


class TestIntegration(unittest.TestCase):
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



unittest.main()
