# test_algoritmo_intro.py 
# Testes automatizados para a Aula 01: O que é um Algoritmo? 
# Execute com: pytest testes/ -v 

# Importamos as três funções que vamos testar 
from codigo.algoritmo_intro import fazer_sanduiche, calcular_media, e_maior_de_idade, e_par


# ============================================================
# TESTES PARA fazer_sanduiche() 
# ============================================================ 

class TestFazerSanduiche:
    """Agrupa todos os testes da função fazer_sanduiche."""

    def test_sanduiche_com_tres_ingredientes(self):
        """Caso normal: lista com três ingredientes."""
        # DADO uma lista de três ingredientes
        ingredientes = ["pão", "queijo", "presunto"]

        # QUANDO chamamos a função
        resultado = fazer_sanduiche(ingredientes)

        # ENTÃO o resultado deve ser uma lista com quatro passos
        # (três ingredientes + o passo de fechar)
        assert len(resultado) == 4
        # E o primeiro passo deve mencionar o pão
        assert "pão" in resultado[0]
        # E o último passo deve ser fechar o sanduíche
        assert "Feche" in resultado[-1]

    def test_sanduiche_com_um_ingrediente(self):
        """Caso extremo: lista com apenas um ingrediente."""
        ingredientes = ["pão"]

        resultado = fazer_sanduiche(ingredientes)

        # Com um ingrediente, temos: pegar o pão + fechar = 2 passos
        assert len(resultado) == 2
        assert "pão" in resultado[0]
        assert "Feche" in resultado[-1]

    def test_sanduiche_com_lista_vazia(self):
        """Caso extremo: lista vazia não deve gerar erro."""
        ingredientes = []

        resultado = fazer_sanduiche(ingredientes)

        # Deve retornar uma lista com uma mensagem de aviso
        assert len(resultado) == 1
        assert "Sem ingredientes" in resultado[0]

    def test_sanduiche_retorna_lista(self):
        """Verifica que a função sempre retorna uma lista."""
        resultado = fazer_sanduiche(["pão", "manteiga"])
        assert isinstance(resultado, list)


# ============================================================ 
# TESTES PARA calcular_media() 
# ============================================================ 

class TestCalcularMedia:
    """Agrupa todos os testes da função calcular_media."""

    def test_media_de_lista_simples(self):
        """Caso normal: média de cinco números."""
        numeros = [7, 3, 9, 4, 5]

        resultado = calcular_media(numeros)

        # A média de [7, 3, 9, 4, 5] é 28/5 = 5.6
        assert resultado == 5.6

    def test_media_de_lista_com_um_elemento(self):
        """Caso extremo: média de uma lista com um único elemento."""
        numeros = [42]

        resultado = calcular_media(numeros)

        # A média de uma lista com um único elemento é o próprio elemento
        assert resultado == 42.0

    def test_media_de_lista_vazia(self):
        """Caso extremo: lista vazia deve retornar None."""
        numeros = []

        resultado = calcular_media(numeros)

        # Uma lista vazia não tem média — retornamos None
        assert resultado is None

    def test_media_com_numeros_decimais(self):
        """Caso com números decimais (float)."""
        numeros = [1.5, 2.5, 3.0]

        resultado = calcular_media(numeros)

        # (1.5 + 2.5 + 3.0) / 3 = 7.0 / 3 ≈ 2.333...
        # Usamos pytest.approx para comparar floats com tolerância
        import pytest
        assert resultado == pytest.approx(2.333, rel=1e-2)

    def test_media_com_numeros_negativos(self):
        """Caso com números negativos."""
        numeros = [-10, 0, 10]

        resultado = calcular_media(numeros)

        # (-10 + 0 + 10) / 3 = 0
        assert resultado == 0.0

    def test_media_retorna_float(self):
        """Verifica que a função retorna um número (int ou float)."""
        resultado = calcular_media([1, 2, 3])
        assert isinstance(resultado, (int, float))


# ============================================================ 
# TESTES PARA e_maior_de_idade() 
# ============================================================ 

class TestEMaiorDeIdade:
    """Agrupa todos os testes da função e_maior_de_idade."""

    def test_adulto_e_maior_de_idade(self):
        """Caso normal: adulto com 25 anos."""
        assert e_maior_de_idade(25) is True

    def test_crianca_nao_e_maior_de_idade(self):
        """Caso normal: criança com 10 anos."""
        assert e_maior_de_idade(10) is False

    def test_exatamente_18_anos_e_maior(self):
        """Caso limite: exatamente 18 anos deve ser maior de idade."""
        # Este é o caso mais importante — o limite exato
        assert e_maior_de_idade(18) is True

    def test_17_anos_nao_e_maior(self):
        """Caso limite: 17 anos ainda é menor de idade."""
        assert e_maior_de_idade(17) is False

    def test_idade_zero(self):
        """Caso extremo: recém-nascido com idade 0."""
        assert e_maior_de_idade(0) is False

    def test_idade_negativa(self):
        """Caso extremo: idade negativa é inválida, retorna False."""
        assert e_maior_de_idade(-5) is False

    def test_idade_muito_alta(self):
        """Caso extremo: pessoa com 100 anos é maior de idade."""
        assert e_maior_de_idade(100) is True

    def test_retorna_booleano(self):
        """Verifica que a função sempre retorna um booleano."""
        assert isinstance(e_maior_de_idade(20), bool)
        assert isinstance(e_maior_de_idade(10), bool)

class TestEhPar:

    def test_numero_par_positivo(self):
        assert e_par(4) is True

    def test_numero_impar_positivo(self):
        assert e_par(7) is False

    def test_zero_e_par(self):
        # Zero é divisível por 2 sem resto — portanto é par
        assert e_par(0) is True

    def test_numero_par_negativo(self):
        # Números negativos pares também têm resto zero
        assert e_par(-6) is True