def rev(s, pos, length):
    ss = s + s
    rrv = ss[:pos] + ss[pos: pos+length][::-1] + ss[pos+length:]
    over = (pos + length) % len(s) if pos + length > len(s) else 0
    rrv = rrv[len(s): len(s) + over] + rrv[over: len(s)]
    return rrv

cur_pos = 0
skip_size = 0
res = range(256)
for length in [14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244]:
    res = rev(res, cur_pos, length)
    cur_pos = (cur_pos + length + skip_size) % len(res)
    skip_size += 1

print res[0] * res[1]