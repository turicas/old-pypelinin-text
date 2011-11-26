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


def plugin_glob(parameters=[]):
    result = []
    for parameter in parameters:
        result.extend(glob.glob(parameter))
    result = list(set(result))
    return result

def plugin_markdown(parameters=[]):
    result = []
    for parameter in parameters:
        filename = parameter + '.html'
        markdown.markdownFromFile(parameter, filename)
        result.append(filename)
    return result

plugin_list = {}

for element in dir():
    if element.startswith('plugin_'):
        plugin_list[element[7:]] = globals()[element]
