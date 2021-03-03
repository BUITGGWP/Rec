# Наибольший общий делитель (НОД)
def nod(x, y):
    if x == y:
        print(x)
    else:
        if x > y:
            nod(x-y, y)
        else:
            nod(x,y-x)

nod(int(input()), int(input()))