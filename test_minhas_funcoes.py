# test_minhas_funcoes.py
import pytest
from minhas_funcoes import remover_duplicatas

def test_remover_duplicatas():
    assert remover_duplicatas([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]
    assert remover_duplicatas([1, 1, 1, 1, 1]) == [1]
    assert remover_duplicatas([]) == []
    assert remover_duplicatas([10, 20, 20, 30, 30, 40, 50, 50]) == [10, 20, 30, 40, 50]

# test_minhas_funcoes.py
import pytest
from minhas_funcoes import calcular_fatorial

def test_calcular_fatorial():
    assert calcular_fatorial(0) == 1
    assert calcular_fatorial(5) == 120
    assert calcular_fatorial(10) == 3628800
   # with pytest.raises(RecursionError):
    #    calcular_fatorial(3000)

# test_minhas_funcoes.py
import pytest
from minhas_funcoes import verificar_ordenacao

def test_verificar_ordenacao_2():
    assert verificar_ordenacao([1, 2, 3, 4, 5]) == True
    assert verificar_ordenacao([1, 2, 2, 4, 5]) == True
    assert verificar_ordenacao([5, 4, 3, 2, 1]) == False
    assert verificar_ordenacao([1, 3, 2]) == False
    assert verificar_ordenacao([]) == True
    assert verificar_ordenacao([1]) == True
