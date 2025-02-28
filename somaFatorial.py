def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)
    
while True:
    numero = int(input('Fatorial de um numero recursivo de 1 ate: '))
    print("Soma:", somatorio(numero))
