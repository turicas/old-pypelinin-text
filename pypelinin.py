import glob
import markdown


def process(plugins, parameters=[]):
    result = []
    if plugins[0] == 'glob':
        for parameter in parameters:
            result.extend(glob.glob(parameter))
        return list(set(result))
    elif plugins[0] == 'markdown':
        for parameter in parameters:
            filename = parameter + '.html'
            markdown.markdownFromFile(parameter, filename)
            result.append(filename)
        return result
    raise InvalidPluginException


class InvalidPluginException(BaseException):
    pass

