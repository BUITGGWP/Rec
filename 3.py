# Наименьшее общее кратное
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = int(input()), int(input())
print(a*b//gcd(a, b))
