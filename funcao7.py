def calculaRaizQuadrada(numero, precisao = 0.0001):
    raiz = numero/2
    while abs(numero - raiz**2) > precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz
    
numero = 50
print("A raiz é: ", calculaRaizQuadrada(numero))