# Цветочки
def cvet(a, b, res):
    if res % a == 0 and res % b == 0:
        print(res)
        return
    else:
        cvet(a, b, res + 1)
a = int(input())
b = int(input())
cvet(a, b, a)
