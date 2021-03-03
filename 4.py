# Сокращение дроби

def nod(x, y):
    if y==0:
        return x
    return nod(y, x % y)

a = int(input())
b = int(input())
c = nod(a, b)
print(f'{a//c}/{b//c}')