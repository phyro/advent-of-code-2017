import sys

arr = [int(line) for line in sys.stdin.readlines()]

res = 0
pos = 0
while pos <= len(arr) - 1:
    new_pos = pos + arr[pos]
    arr[pos] += 1
    res += 1
    pos = new_pos

print res