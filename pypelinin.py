import glob
import markdown


def plugin_glob(parameters=[]):
    result = []
    for parameter in parameters:
        result.extend(glob.glob(parameter))
    return list(set(result))


def plugin_markdown(parameters=[]):
    result = []
    for parameter in parameters:
        filename = parameter + '.html'
        markdown.markdownFromFile(parameter, filename)
        result.append(filename)
    return result


plugin_list = {'glob': plugin_glob,
               'markdown': plugin_markdown,}


def process(plugins, parameters=[]):
    result = parameters
    for plugin in plugins:
        if plugin not in plugin_list:
            raise InvalidPluginException
        result = plugin_list[plugin](result)
    return result


class InvalidPluginException(BaseException):
    pass

