#!/usr/bin/env python

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
