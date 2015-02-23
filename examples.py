import decode
import re


f = decode.decode_file("test.rgx")
g = decode.decode_file("same.rgx")
print f
print g
text = "exp(tan(z)/z^5+1)"
print re.findall(f, text)
print re.findall(g, text)
