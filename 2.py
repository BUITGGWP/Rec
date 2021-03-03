# Возведение в степень
def stepen(a, n):
    if n == 1:
        return a
    return a * stepen(a, n - 1)

print(stepen(int(input()), int(input())))