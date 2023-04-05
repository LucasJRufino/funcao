def verificarPrimo(numero):
    if numero<2:
        return "Não é primo"
    for i in range(2, int(numero/2 ) + 1):
        if numero % i == 0:
            return "Não é primo"
    return "É primo"
    
numero = 108

print(verificarPrimo(numero))