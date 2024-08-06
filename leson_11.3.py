import sys
from pprint import pprint
import inspect


def introspection_info(obj):
    info = {}

    info['type'] = type(obj)
    info['attributes'] = str(dir(obj))
    f = [arg for arg in dir(obj) if not callable(getattr(obj, arg))]
    info['methods'] = str(f)
    info['module'] = str(inspect.getmodule(introspection_info))
    return info


number_info = introspection_info(42)
pprint(number_info)
