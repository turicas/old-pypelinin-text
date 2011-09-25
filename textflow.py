import glob

def process(plugins, parameters=[]):
    result = []
    if plugins[0] == 'glob':
        for parameter in parameters:
            result.extend(glob.glob(parameter))
    return list(set(result))

