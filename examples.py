import decode
import re


f = decode.decode("test.rgx")
print f
text = "exp(tan(z)/z^5+1)"
print re.findall(f, text)
g = decode.decode("[a-z]+[0-9]?")
print g
print re.findall(g, "abc1")
print re.findall(g, "def")
