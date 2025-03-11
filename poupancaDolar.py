def poupancaDolar(valor):
    percentual =  5
    rendimento = (percentual / 10)
    if valor == 100000:
        return 1
    else:
        return poupancaDolar(rendimento * valor)
    
poupancaDolar(250)
