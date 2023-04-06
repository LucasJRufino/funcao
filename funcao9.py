def romanoParaDecimal(numRomano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(numRomano)):
        if i > 0 and valores[numRomano[i]] > valores[numRomano[i-1]]:
            decimal += valores[numRomano[i]] - 2 * valores[numRomano[i-1]]
        else:
            decimal += valores[numRomano[i]]
    return decimal
    
numRomano = 'MCMXCIV'

print(numRomano , "em decimal é: ", romanoParaDecimal(numRomano))