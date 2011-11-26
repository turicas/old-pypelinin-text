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

import glob
import markdown
import plugins


def process(input_plugins, parameters=[]):
    if not isinstance(parameters, list):
        raise TypeError('Input parameters should be a list.')
    elif not input_plugins:
        raise ValueError('No plugins received')

    result = parameters
    for plugin in input_plugins:
        if plugin not in plugins.plugin_list:
            raise InvalidPluginException
        result = plugins.plugin_list[plugin](result)
    return result

class InvalidPluginException(BaseException):
    pass
