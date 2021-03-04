# ДР
def nod(x, y):
    if x == y:
        return x
    else:
        if x > y:
            return nod(x-y, y)
        else:
            return nod(x,y-x)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())
res = 0
if b % a == 0:
    otvet = 1
else:
    otvet = nod(a, a*b//gcd(a, b))
print(otvet)
