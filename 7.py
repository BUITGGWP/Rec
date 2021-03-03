# Дроби

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))


def nod(x, y):
    if y == 0:
        return x
    return nod(y, x % y)


d1[0] = d1[0] * d2[1]
d2[0] = d2[0] * d1[1]
d1[1] = d1[1] * d2[1]
d2[1] = d1[1]
d3 = [d1[0] + d2[0], d2[1]]
c = nod(d3[0], d3[1])
print(f'{d3[0]//c} {d3[1]//c}')
