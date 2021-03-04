# Цветочки
def cvet(a, b, res):
    if res % a == 0 and res % b == 0:
        return res
        
    else:
        return cvet(a, b, res + 1)
a = int(input())
b = int(input())
print(cvet(a, b, a))