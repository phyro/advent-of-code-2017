import sys

parent = {}
all_nodes = []
for line in sys.stdin.readlines():
    arr = line.split(" ")
    name = arr[0]
    all_nodes.append(name)
    if len(arr) > 2:
        nodes = map(lambda x: x.replace(",", "").strip(), arr[3:])
        for node in nodes:
            parent[node] = name

def depth(node):
    if node not in parent:
        return 0, node
    depth_, root = depth(parent[node])
    return 1 + depth_, root

print max(map(depth, all_nodes), key=lambda x: x[0])[1]