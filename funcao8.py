def verificarPalindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace("-", "").replace( "ô", "o")
    return texto == texto[::-1]
    
texto = "Socorram-me, subi no ônibus em Marrocos"

if verificarPalindromo(texto):
    print(texto, "É um palíndromo")
    
else:
    print("Não é um palíndromo")