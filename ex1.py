import re

def findIntsInString(s: str):
    l: list = []
    l += (re.findall(r'\d+', s))
    return l

def stringToInt(s: str):
  result = 0
  for i in range(0, len(s)):
    result = result * 10 + int(s[i])
  return result

def output(s):
    l = findIntsInString(s)

    print(l)

    ints: list = []

    for i in l:
        ints.append( stringToInt(i))

    print( ints)

s = " x = 123" \
    "y =234" \
    "z = 567";


