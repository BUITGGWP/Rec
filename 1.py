# Наибольший общий делитель (НОД)
def nod(x, y):
    if x == y:
        return x
    else:
        if x > y:
            return nod(x-y, y)
        else:
            return nod(x,y-x)

print(nod(int(input()), int(input())))