def calculaFatorial(numero):
    if numero != 0:
        return numero * calculaFatorial(numero - 1)
    return 1

numero = 5
print("O fatorial de: ", numero, " é ", calculaFatorial(numero))