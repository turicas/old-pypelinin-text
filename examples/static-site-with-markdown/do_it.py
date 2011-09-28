#!/usr/bin/env python

import os
import sys

sys.path.insert(0, '../../')
import pypelinin


plugins = ['glob', 'markdown']
parameters = [os.getcwd() + os.path.sep + '*.markdown']
pypelinin.process(plugins, parameters)
