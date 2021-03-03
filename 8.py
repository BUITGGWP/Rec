# Точная степень двойки

def stepen(n):
    if n > 1:
        return stepen(n / 2)
    elif n == 1:
        return 'YES'
    else:
        return 'NO'
print(stepen(int(input())))