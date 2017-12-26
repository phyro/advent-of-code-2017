import sys
from collections import defaultdict

g = defaultdict(list)
for line in sys.stdin.readlines():
    arr = line.split(" ")
    a = arr[0]
    connected = map(lambda x: x.replace(",", "").strip(), arr[2:])
    for node in connected:
        g[a].append(node)
        g[node].append(a)

def dfs(g, start):
    queue = [start]
    been = set()
    while len(queue) != 0:
        cur = queue.pop()
        been.add(cur)
        for node in g[cur]:
            if node not in been:
                queue.append(node)
    return len(been)

print dfs(g, "0")