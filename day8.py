import sys
from collections import defaultdict

def truthy(condition, state):
    reg = condition[0]
    return eval("{}".format(state[reg]) + "".join(condition[1:]))

state = defaultdict(int)
for line in sys.stdin.readlines():
    arr = line.split(" ")
    reg, op, val = arr[:3]
    condition = arr[4:]
    if truthy(condition, state):
        if op == "inc":
            state[reg] += int(val)
        else:
            state[reg] -= int(val)

print max(state.values())