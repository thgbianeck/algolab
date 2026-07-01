# test_funcoes_uteis.py
# Testes automatizados para a Aula 05: Funções
# Execute com: pytest testes/ -v
#
# Filosofia dos testes:
# - Parâmetros padrão: testar com e sem o argumento opcional
# - Retorno múltiplo: verificar cada componente da tupla retornada
# - Primo: testar casos especiais (0, 1, 2), primos conhecidos e não-primos
# - Higher-order: testar com cada função auxiliar como argumento

import pytest

# Importamos todas as funções que vamos testar
from codigo_05.funcoes_uteis import (
    saudar,
    calcular_estatisticas,
    e_primo,
    aplicar_operacao,
    dobrar,
    triplicar,
    quadrado,
    inverter_sinal,
    contar_vogais,
    aplicar_e_filtrar,
)


# ============================================================
# TESTES PARA saudar()
# ============================================================

class TestSaudar:
    """
    Testa todos os comportamentos da função saudar.
    Verifica: saudação padrão, saudação personalizada, normalização de entrada.
    """

    def test_saudacao_padrao(self):
        """Sem segundo argumento, usa a saudação padrão 'Olá'."""
        assert saudar("Ana") == "Olá, Ana!"

    def test_saudacao_personalizada(self):
        """Com segundo argumento, usa a saudação fornecida."""
        assert saudar("Carlos", "Bom dia") == "Bom dia, Carlos!"

    def test_saudacao_boa_noite(self):
        """Outro exemplo de saudação personalizada."""
        assert saudar("Maria", "Boa noite") == "Boa noite, Maria!"

    def test_nome_em_minusculas_capitalizado(self):
        """Nome em minúsculas deve ser capitalizado automaticamente."""
        assert saudar("pedro") == "Olá, Pedro!"

    def test_nome_em_maiusculas_normalizado(self):
        """Nome em maiúsculas deve ser normalizado pelo capitalize."""
        # capitalize() coloca apenas a primeira letra maiúscula
        assert saudar("JOAO") == "Olá, Joao!"

    def test_nome_com_espacos_extras(self):
        """Espaços extras no nome devem ser removidos."""
        assert saudar("  Maria  ") == "Olá, Maria!"

    def test_retorna_string(self):
        """A função deve sempre retornar uma string."""
        assert isinstance(saudar("Ana"), str)

    def test_resultado_termina_com_exclamacao(self):
        """A saudação deve sempre terminar com ponto de exclamação."""
        resultado = saudar("Teste", "Oi")
        assert resultado.endswith("!")

    def test_saudacao_com_espacos_extras(self):
        """Espaços extras na saudação também devem ser removidos."""
        assert saudar("Ana", "  Oi  ") == "Oi, Ana!"


# ============================================================
# TESTES PARA calcular_estatisticas()
# ============================================================

class TestCalcularEstatisticas:
    """
    Testa todos os comportamentos da função calcular_estatisticas.
    Verifica: valores corretos, lista vazia, lista unitária, negativos.
    """

    def test_estatisticas_lista_simples(self):
        """Caso normal: lista com cinco números distintos."""
        minimo, maximo, media = calcular_estatisticas([7, 3, 9, 4, 5])
        assert minimo == 3
        assert maximo == 9
        assert media == pytest.approx(5.6)

    def test_lista_vazia_retorna_tres_none(self):
        """Lista vazia deve retornar (None, None, None)."""
        resultado = calcular_estatisticas([])
        assert resultado == (None, None, None)

    def test_lista_com_um_elemento(self):
        """Lista com um único elemento — mínimo, máximo e média são iguais."""
        minimo, maximo, media = calcular_estatisticas([42])
        assert minimo == 42
        assert maximo == 42
        assert media == pytest.approx(42.0)

    def test_lista_com_negativos(self):
        """Caso com números negativos."""
        minimo, maximo, media = calcular_estatisticas([-5, -1, -3])
        assert minimo == -5
        assert maximo == -1
        assert media == pytest.approx(-3.0)

    def test_lista_com_positivos_e_negativos(self):
        """Caso com mistura de positivos e negativos."""
        minimo, maximo, media = calcular_estatisticas([-10, 0, 10])
        assert minimo == -10
        assert maximo == 10
        assert media == pytest.approx(0.0)

    def test_lista_com_elementos_iguais(self):
        """Lista com todos os elementos iguais — mín e máx são o mesmo."""
        minimo, maximo, media = calcular_estatisticas([5, 5, 5, 5])
        assert minimo == 5
        assert maximo == 5
        assert media == pytest.approx(5.0)

    def test_retorno_e_tupla(self):
        """A função deve retornar uma tupla com três elementos."""
        resultado = calcular_estatisticas([1, 2, 3])
        assert isinstance(resultado, tuple)
        assert len(resultado) == 3

    def test_desempacotamento_funciona(self):
        """O retorno múltiplo deve suportar desempacotamento."""
        # Esta sintaxe deve funcionar sem erros
        mn, mx, med = calcular_estatisticas([1, 5, 3])
        assert mn == 1
        assert mx == 5
        assert med == pytest.approx(3.0)


# ============================================================
# TESTES PARA e_primo()
# ============================================================

class TestEPrimo:
    """
    Testa todos os comportamentos da função e_primo.
    Verifica: casos especiais (0, 1, 2), primos conhecidos, não-primos, negativos.
    """

    # --- Casos especiais ---

    def test_zero_nao_e_primo(self):
        """Zero não é primo por definição."""
        assert e_primo(0) is False

    def test_um_nao_e_primo(self):
        """1 não é primo — caso especial importante."""
        assert e_primo(1) is False

    def test_dois_e_primo(self):
        """2 é primo — o único número primo par."""
        assert e_primo(2) is True

    def test_negativo_nao_e_primo(self):
        """Números negativos não são primos."""
        assert e_primo(-5) is False
        assert e_primo(-2) is False

    # --- Primos conhecidos ---

    def test_tres_e_primo(self):
        assert e_primo(3) is True

    def test_cinco_e_primo(self):
        assert e_primo(5) is True

    def test_sete_e_primo(self):
        assert e_primo(7) is True

    def test_onze_e_primo(self):
        assert e_primo(11) is True

    def test_treze_e_primo(self):
        assert e_primo(13) is True

    def test_dezessete_e_primo(self):
        assert e_primo(17) is True

    def test_dezenove_e_primo(self):
        assert e_primo(19) is True

    # --- Não-primos conhecidos ---

    def test_quatro_nao_e_primo(self):
        """4 = 2 × 2 — não é primo."""
        assert e_primo(4) is False

    def test_seis_nao_e_primo(self):
        """6 = 2 × 3 — não é primo."""
        assert e_primo(6) is False

    def test_nove_nao_e_primo(self):
        """9 = 3 × 3 — não é primo."""
        assert e_primo(9) is False

    def test_vinte_e_cinco_nao_e_primo(self):
        """25 = 5 × 5 — não é primo."""
        assert e_primo(25) is False

    def test_cem_nao_e_primo(self):
        """100 = 4 × 25 — não é primo."""
        assert e_primo(100) is False

    def test_retorna_booleano(self):
        """A função deve sempre retornar um booleano."""
        assert isinstance(e_primo(7), bool)
        assert isinstance(e_primo(4), bool)


# ============================================================
# TESTES PARA aplicar_operacao() e funções auxiliares
# ============================================================

class TestAplicarOperacao:
    """
    Testa a função aplicar_operacao com cada função auxiliar como argumento.
    Verifica: resultado correto, passagem de diferentes funções, zero e negativos.
    """

    def test_dobrar_numero_positivo(self):
        """Aplicar dobrar a 5 deve retornar 10."""
        assert aplicar_operacao(5, dobrar) == 10

    def test_triplicar_numero_positivo(self):
        """Aplicar triplicar a 5 deve retornar 15."""
        assert aplicar_operacao(5, triplicar) == 15

    def test_quadrado_numero_positivo(self):
        """Aplicar quadrado a 4 deve retornar 16."""
        assert aplicar_operacao(4, quadrado) == 16

    def test_inverter_sinal_positivo(self):
        """Aplicar inverter_sinal a 7 deve retornar -7."""
        assert aplicar_operacao(7, inverter_sinal) == -7

    def test_inverter_sinal_negativo(self):
        """Aplicar inverter_sinal a número negativo deve retornar positivo."""
        assert aplicar_operacao(-3, inverter_sinal) == 3

    def test_operacao_com_zero(self):
        """Dobrar zero deve retornar zero."""
        assert aplicar_operacao(0, dobrar) == 0

    def test_operacao_com_negativo(self):
        """Dobrar número negativo deve retornar negativo dobrado."""
        assert aplicar_operacao(-4, dobrar) == -8

    def test_operacao_com_float(self):
        """Dobrar float deve funcionar corretamente."""
        assert aplicar_operacao(2.5, dobrar) == pytest.approx(5.0)

    def test_quadrado_de_zero(self):
        """Zero ao quadrado é zero."""
        assert aplicar_operacao(0, quadrado) == 0

    def test_resultado_depende_da_operacao_passada(self):
        """O mesmo número com operações diferentes deve dar resultados diferentes."""
        resultado_dobro = aplicar_operacao(6, dobrar)
        resultado_triplo = aplicar_operacao(6, triplicar)
        resultado_quad = aplicar_operacao(6, quadrado)
        # Os três resultados devem ser diferentes entre si
        assert resultado_dobro != resultado_triplo
        assert resultado_triplo != resultado_quad
        assert resultado_dobro == 12
        assert resultado_triplo == 18
        assert resultado_quad == 36


# ============================================================
# TESTES DAS FUNÇÕES AUXILIARES INDIVIDUALMENTE
# ============================================================

class TestFuncoesAuxiliares:
    """Testa as funções auxiliares dobrar, triplicar, quadrado e inverter_sinal."""

    def test_dobrar(self):
        assert dobrar(3) == 6
        assert dobrar(0) == 0
        assert dobrar(-2) == -4

    def test_triplicar(self):
        assert triplicar(3) == 9
        assert triplicar(0) == 0
        assert triplicar(-2) == -6

    def test_quadrado(self):
        assert quadrado(3) == 9
        assert quadrado(0) == 0
        assert quadrado(-3) == 9  # (-3)² = 9

    def test_inverter_sinal(self):
        assert inverter_sinal(5) == -5
        assert inverter_sinal(-5) == 5
        assert inverter_sinal(0) == 0

class TestContarVogais:
    
    def test_contar_vogais_frase(self):
        resultado = contar_vogais("Python")
        assert resultado["total"] == 1
        assert resultado["por_vogal"]["o"] == 1

    def test_contar_vogais_maiusculas(self):
        resultado = contar_vogais("AEIOUaeiou")
        assert resultado["total"] == 10

    def test_contar_vogais_sem_vogais(self):
        resultado = contar_vogais("rhythm")
        assert resultado["total"] == 0

    def test_aplicar_e_filtrar(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = aplicar_e_filtrar(numeros, dobrar, 6)
        # dobrar([1,2,3,4,5]) = [2,4,6,8,10] — filtrar >= 6 = [6,8,10]
        assert resultado == [6, 8, 10]