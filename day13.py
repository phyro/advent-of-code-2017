import sys

def is_at_top(arr, pos):
    return pos == 0 or pos % (2*arr[pos] - 2) == 0

arr = {}
for line in sys.stdin.readlines():
    pos, val = map(lambda x: int(x.strip()), line.split(":"))
    arr[int(pos)] = val

print sum(pos * arr[pos] for pos in sorted(arr.keys()) if is_at_top(arr, pos))