import sys

def isValid(s):
    words = map(lambda x: x.strip(), s.split(" "))
    return len(words) == len(list(set(words)))

lines = [x for x in sys.stdin.readlines()]
print len(filter(isValid, lines))
