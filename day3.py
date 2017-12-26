import math

def f(n):
    rv = int(math.ceil(math.sqrt(n)))
    if rv % 2 == 0:
        rv += 1
    return rv

nn = int(raw_input())
fn = f(nn)
diff = nn - (fn - 2)**2
x = mid = fn/2
y = abs(mid - diff % (fn - 1))
res = x + y
print res
