import decode
import re


f = decode.decode_file("test.rgx")
print f
text = "exp(tan(z)/z^5+1)"
print re.findall(f, text)
