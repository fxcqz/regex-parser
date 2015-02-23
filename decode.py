import re


def decode_(func):
    def wrapper(*args, **kwargs):
        data = re.sub("(?:\s*(\/\*([^\*\/])*.*?\*\/)?|(\/\/.*)?)[\s|\x0A]", "", 
                        func(*args, **kwargs), re.M)
        return re.sub("\s+", "", data)
    return wrapper

@decode_
def decode_file(filename):
    contents = None
    try:
        with open(filename, 'r') as handle:
            contents = ''.join(handle.readlines())
    except IOError as e:
        print e
    return contents

@decode_
def decode(string):
    return string
