#!/usr/bin/env python

import os
import pypelinin


plugins = ['glob', 'markdown']
parameters = [os.getcwd() + os.path.sep + '*.markdown']
pypelinin.process(plugins, parameters)
