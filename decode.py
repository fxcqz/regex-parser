import re


def decode_regex(regex):
    return re.sub(r"(?:\s*(\/\*([^\*\/])*.*?\*\/)?|(\/\/.*)?)?\s+", "", regex, re.I|re.M)

s = """(
    /* this regex will do
       something  totally
       awesome! */
    [a-z]*? // might need some letters
    (
        [0-9]{3} // then the 3 numbers
    )
    /* 
        that was coolo RIGHT?????
    */
    )"""
teststr = "test123"
print "Decoded regex: ", decode_regex(s)
print re.sub(decode_regex(s), r"\2 are the numbers yo", teststr)
