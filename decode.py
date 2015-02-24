import re
import os


def decode_(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        # remove single line comments
        data = re.sub("\s*\/\/.*", "", data)
        # remove multiline comments
        data = re.sub("\/\*([\s\S]*?)\*\/", "", data)
        # remove indentation
        data = [d.lstrip() for d in data.split('\n')]
        # remove trailing spaces from lines
        data = [d.rstrip() for d in data]
        # final expression as a string
        return ''.join(data)
    return wrapper


def get_file(filename):
    contents = None
    try:
        with open(filename, 'r') as handle:
            contents = ''.join(handle.readlines())
    except IOError as e:
        print e
    return contents


@decode_
def decode(string):
    if os.path.isfile(string):
        return get_file(string)
    return string
