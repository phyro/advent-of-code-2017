def solve(s):
    open_brackets = 0 
    comments = 0
    i = 0
    res = 0
    while i != len(s):
        if s[i] == '!':
            i += 2
            continue
        if s[i] == '{':
            if comments == 0:
                open_brackets += 1
        if s[i] == '}':
            if comments == 0:
                res += open_brackets
                open_brackets -= 1
        if s[i] == '<':
            if comments == 0:
                comments = 1
        if s[i] == '>':
            if comments != 0:
                comments = 0
        i += 1
    return res

s = raw_input()
print solve(s)