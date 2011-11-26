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
