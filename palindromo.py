# Criando o arquivo palindromo.py
def verify_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]