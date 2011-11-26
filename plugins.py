import glob
import markdown
from jinja2 import Environment
from jinja2.loaders import DictLoader
import os


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

def plugin_jinja(parameters=[]):
    template_fp = open(parameters[0])
    body_fp = open(parameters[1])

    template_dict = {}
    template_dict[parameters[0]] = template_fp.read()
    template_dict[parameters[1]] = body_fp.read()
    print template_dict

    new_filename = '%s_%s' % (parameters[0], os.path.basename(parameters[1]))
    result = [new_filename]
    env = Environment(loader=DictLoader(template_dict))

    fd = open(new_filename, 'w')
    fd.write(env.get_template(parameters[1]).render())
    fd.close()

    template_fp.close()
    body_fp.close()
    return result

plugin_list = {}

for element in dir():
    if element.startswith('plugin_'):
        plugin_list[element[7:]] = globals()[element]
