import sys
import hashlib

def hash_state(state):
    return hashlib.md5(
        ",".join(map(str, state))
    ).hexdigest()

def move(state, idx):
    val = state[idx]
    state[idx] = 0
    for i in range(val):
        state[(idx + 1 + i) % len(state)] += 1

state = map(int, raw_input().split())

been = {}
while hash_state(state) not in been:
    been[hash_state(state)] = 1
    maxi = max(state)
    start = state.index(maxi)
    move(state, start)

print len(been)