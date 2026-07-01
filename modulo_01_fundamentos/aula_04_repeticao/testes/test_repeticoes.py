# test_repeticoes.py
# Testes automatizados para a Aula 04: Estruturas de Repetição
# Execute com: pytest testes/ -v
#
# Filosofia dos testes:
# - Casos normais: entrada típica com resultado esperado claro
# - Casos extremos: lista vazia, um elemento, limite zero, todos negativos
# - Casos de comportamento: verificar que break e continue funcionam corretamente

import pytest

# Importamos as quatro funções que vamos testar
from codigo_04.repeticoes import (
    somar_lista,
    contar_ate,
    encontrar_primeiro_par,
    filtrar_positivos,
    tabuada,
    tabuada_formatada,
)


# ============================================================
# TESTES PARA somar_lista()
# ============================================================

class TestSomarLista:
    """
    Testa todos os comportamentos da função somar_lista.
    Verifica: soma correta, lista vazia, elemento único, negativos, floats.
    """

    def test_soma_lista_simples(self):
        """Caso normal: soma de cinco números positivos."""
        # 1 + 2 + 3 + 4 + 5 = 15
        assert somar_lista([1, 2, 3, 4, 5]) == 15

    def test_soma_lista_vazia(self):
        """Caso extremo: lista vazia deve retornar 0."""
        # A soma de nenhum elemento é o elemento neutro da adição: 0
        assert somar_lista([]) == 0

    def test_soma_com_um_elemento(self):
        """Caso extremo: lista com um único elemento."""
        # A soma de uma lista com um elemento é o próprio elemento
        assert somar_lista([42]) == 42

    def test_soma_com_numeros_negativos(self):
        """Caso com números negativos."""
        # -3 + (-7) + (-2) = -12
        assert somar_lista([-3, -7, -2]) == -12

    def test_soma_com_positivos_e_negativos(self):
        """Caso com mistura de positivos e negativos."""
        # -3 + 3 = 0
        assert somar_lista([-3, 3]) == 0

    def test_soma_com_zero_na_lista(self):
        """Zero na lista não deve alterar a soma."""
        assert somar_lista([5, 0, 3]) == 8

    def test_soma_com_floats(self):
        """Caso com números decimais."""
        assert somar_lista([1.5, 2.5, 1.0]) == pytest.approx(5.0)

    def test_soma_lista_grande(self):
        """Caso com lista maior — verifica corretude para N elementos."""
        # Soma de 1 a 10 = 55 (fórmula: n*(n+1)/2 = 10*11/2 = 55)
        assert somar_lista(list(range(1, 11))) == 55

    def test_retorna_numero(self):
        """A função deve retornar um número (int ou float)."""
        resultado = somar_lista([1, 2, 3])
        assert isinstance(resultado, (int, float))


# ============================================================
# TESTES PARA contar_ate()
# ============================================================

class TestContarAte:
    """
    Testa todos os comportamentos da função contar_ate.
    Verifica: contagem correta, limite zero, limite negativo, limite um.
    """

    def test_contar_ate_cinco(self):
        """Caso normal: contar de 1 até 5."""
        assert contar_ate(5) == [1, 2, 3, 4, 5]

    def test_contar_ate_um(self):
        """Caso extremo: limite igual a 1 deve retornar lista com apenas [1]."""
        assert contar_ate(1) == [1]

    def test_contar_ate_zero(self):
        """Caso extremo: limite zero deve retornar lista vazia."""
        # Não há nenhum número entre 1 e 0
        assert contar_ate(0) == []

    def test_contar_ate_negativo(self):
        """Caso extremo: limite negativo deve retornar lista vazia."""
        assert contar_ate(-5) == []

    def test_contar_ate_dez(self):
        """Caso normal com limite maior."""
        resultado = contar_ate(10)
        # A lista deve ter exatamente 10 elementos
        assert len(resultado) == 10
        # O primeiro elemento deve ser 1
        assert resultado[0] == 1
        # O último elemento deve ser 10 (o limite é inclusivo)
        assert resultado[-1] == 10

    def test_contar_preserva_ordem_crescente(self):
        """Os números devem estar em ordem crescente."""
        resultado = contar_ate(5)
        # Verificamos que cada elemento é exatamente um maior que o anterior
        for i in range(len(resultado) - 1):
            assert resultado[i + 1] == resultado[i] + 1

    def test_retorna_lista(self):
        """A função deve sempre retornar uma lista."""
        assert isinstance(contar_ate(5), list)
        assert isinstance(contar_ate(0), list)


# ============================================================
# TESTES PARA encontrar_primeiro_par()
# ============================================================

class TestEncontrarPrimeiroPar:
    """
    Testa todos os comportamentos da função encontrar_primeiro_par.
    Verifica: par no início, no meio, no fim, sem par, lista vazia.
    Foco especial: comportamento do break.
    """

    def test_par_no_inicio(self):
        """O primeiro elemento já é par — deve ser retornado imediatamente."""
        assert encontrar_primeiro_par([2, 3, 5, 7]) == 2

    def test_par_no_meio(self):
        """Caso normal: primeiro par está no meio da lista."""
        assert encontrar_primeiro_par([3, 7, 4, 9, 2]) == 4

    def test_par_no_fim(self):
        """O par está apenas no último elemento."""
        assert encontrar_primeiro_par([1, 3, 5, 7, 8]) == 8

    def test_sem_par_retorna_none(self):
        """Lista sem nenhum número par deve retornar None."""
        assert encontrar_primeiro_par([1, 3, 5, 7]) is None

    def test_lista_vazia_retorna_none(self):
        """Lista vazia não tem par — deve retornar None."""
        assert encontrar_primeiro_par([]) is None

    def test_todos_pares_retorna_o_primeiro(self):
        """Quando todos são pares, deve retornar apenas o primeiro."""
        # O break deve garantir que apenas o primeiro seja retornado
        assert encontrar_primeiro_par([2, 4, 6, 8]) == 2

    def test_zero_e_par(self):
        """Zero é par (resto de 0/2 é 0) — deve ser retornado."""
        assert encontrar_primeiro_par([1, 3, 0, 5]) == 0

    def test_numero_negativo_par(self):
        """Números negativos pares também devem ser encontrados."""
        assert encontrar_primeiro_par([1, 3, -4, 5]) == -4

    def test_retorno_e_int_ou_none(self):
        """A função deve retornar int ou None."""
        resultado_com_par = encontrar_primeiro_par([1, 2, 3])
        resultado_sem_par = encontrar_primeiro_par([1, 3, 5])
        assert isinstance(resultado_com_par, int)
        assert resultado_sem_par is None


# ============================================================
# TESTES PARA filtrar_positivos()
# ============================================================

class TestFiltrarPositivos:
    """
    Testa todos os comportamentos da função filtrar_positivos.
    Verifica: filtragem correta, lista vazia, todos positivos, todos negativos.
    Foco especial: comportamento do continue e tratamento do zero.
    """

    def test_filtragem_mista(self):
        """Caso normal: lista com positivos, negativos e zero."""
        resultado = filtrar_positivos([3, -1, 5, 0, -7, 2])
        assert resultado == [3, 5, 2]

    def test_lista_vazia(self):
        """Lista vazia deve retornar lista vazia."""
        assert filtrar_positivos([]) == []

    def test_todos_positivos(self):
        """Quando todos são positivos, a lista retornada é igual à original."""
        numeros = [1, 2, 3, 4, 5]
        assert filtrar_positivos(numeros) == numeros

    def test_todos_negativos(self):
        """Quando todos são negativos, deve retornar lista vazia."""
        assert filtrar_positivos([-1, -2, -3]) == []

    def test_zero_nao_e_positivo(self):
        """Zero não é estritamente positivo — deve ser filtrado."""
        assert filtrar_positivos([0, 0, 0]) == []

    def test_zero_e_negativos_filtrados(self):
        """Mistura de zeros e negativos deve resultar em lista vazia."""
        assert filtrar_positivos([-5, 0, -3, 0]) == []

    def test_preserva_ordem_original(self):
        """Os positivos devem aparecer na mesma ordem da lista original."""
        resultado = filtrar_positivos([5, -1, 3, -2, 1])
        assert resultado == [5, 3, 1]

    def test_com_floats_positivos(self):
        """Floats positivos também devem ser incluídos."""
        resultado = filtrar_positivos([-1.5, 0.5, 2.3, -0.1])
        assert resultado == [0.5, 2.3]

    def test_nao_modifica_lista_original(self):
        """A função não deve modificar a lista de entrada."""
        original = [3, -1, 5, 0, -7, 2]
        copia = original.copy()
        filtrar_positivos(original)
        # A lista original deve permanecer inalterada
        assert original == copia

    def test_retorna_lista(self):
        """A função deve sempre retornar uma lista."""
        assert isinstance(filtrar_positivos([1, -1, 0]), list)

class TestTabuada:

    def test_tabuada_do_sete(self):
        resultado = tabuada(7)
        assert resultado == [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

    def test_tabuada_tem_dez_elementos(self):
        assert len(tabuada(5)) == 10

    def test_tabuada_do_zero(self):
        # A tabuada do zero são dez zeros
        assert tabuada(0) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_tabuada_formatada_primeiro_elemento(self):
        resultado = tabuada_formatada(3)
        assert resultado[0] == "3 x 1 = 3"

    def test_tabuada_formatada_ultimo_elemento(self):
        resultado = tabuada_formatada(3)
        assert resultado[-1] == "3 x 10 = 30"

    def test_tabuada_formatada_tem_dez_linhas(self):
        assert len(tabuada_formatada(5)) == 10