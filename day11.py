path = map(lambda x: x.strip(), raw_input().split(","))
dirs = {
    "nw": (-1, 1),
    "n": (0, 2),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -2),
    "sw": (-1, -1)
}

def move_to(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

end = reduce(lambda cur, cur_move: move_to(cur, dirs[cur_move]), path, (0, 0))

res = abs(end[0])/2 + abs(end[1])/2
if end[0] % 2 == 1 or end[1] % 2 == 1:
    res += 1
print res