# Перевод в любую систему счисления
def nbr_base(nbr, st_bs, base):
    if nbr >= st_bs:
        nbr_base(nbr // st_bs, st_bs, base)
    print(base[nbr % st_bs], end='')
    
nbr_base(int(input()), int(input()), input())
