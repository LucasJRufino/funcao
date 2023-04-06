import random
import string
def gerarSenha(tamanho = 8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha
    
senha = gerarSenha()
print("A senha gerada foi: ", senha)