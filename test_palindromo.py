# Criando o arquivo test_palindromo.py
from palindromo import verify_palindromo

def test_palindromo_simples():
    assert verify_palindromo("radar") == True
    assert verify_palindromo("python") == False
    assert verify_palindromo("ana") == True

def test_palindromo_com_espacos():
    assert verify_palindromo("A man a plan a canal Panama") == True

def test_palindromo_maiusculas_minusculas():
    assert verify_palindromo("Radar") == True
    assert verify_palindromo("Ana") == True