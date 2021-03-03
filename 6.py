# ДР

n = int(input())
m = int(input())
def remaind(x, y):
    if x >= y:
        return remaind(x-y, y)
    else:
        return x

a = remaind(n, m)
c = int((n / m)+a)
print(c)
