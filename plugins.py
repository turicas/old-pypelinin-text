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
