from OO import c1
import re

c1.run()
#
# for p in sys.path:
#     print(p)


s = "abc"


def convert(v):
    return v.group() + '?'


print(re.sub('\w', convert, s))
print(re.sub('(\w)', r'\1?', s))
