# test_calculadora_basica.py
# Testes automatizados para a Aula 02: Variáveis, Tipos de Dados e Operadores
# Execute com: pytest testes/ -v

import pytest

# Importamos as cinco funções que vamos testar
from codigo_02.calculadora_basica import (
    somar,
    dividir,
    e_positivo,
    concatenar_nome,
    calcular_imc,
    converter_temperatura,
)


# ============================================================
# TESTES PARA somar()
# ============================================================

class TestSomar:
    """Agrupa todos os testes da função somar."""

    def test_soma_dois_inteiros_positivos(self):
        """Caso normal: soma de dois inteiros positivos."""
        assert somar(3, 4) == 7

    def test_soma_com_numero_negativo(self):
        """Caso com número negativo."""
        assert somar(-5, 10) == 5

    def test_soma_dois_negativos(self):
        """Caso com dois números negativos."""
        assert somar(-3, -7) == -10

    def test_soma_com_zero(self):
        """Caso extremo: somar com zero não altera o valor."""
        assert somar(42, 0) == 42

    def test_soma_dois_floats(self):
        """Caso com dois floats — usa pytest.approx para precisão."""
        assert somar(1.5, 2.5) == pytest.approx(4.0)

    def test_soma_int_e_float(self):
        """Caso com int e float — resultado deve ser float."""
        resultado = somar(3, 0.5)
        assert resultado == pytest.approx(3.5)
        # Verifica que o resultado é float quando um dos operandos é float
        assert isinstance(resultado, float)

    def test_soma_retorna_int_quando_ambos_int(self):
        """Verifica que int + int retorna int em Python."""
        resultado = somar(10, 20)
        assert isinstance(resultado, int)


# ============================================================
# TESTES PARA dividir()
# ============================================================

class TestDividir:
    """Agrupa todos os testes da função dividir."""

    def test_divisao_exata(self):
        """Caso normal: divisão com resultado inteiro."""
        # Em Python 3, / sempre retorna float
        assert dividir(10, 2) == pytest.approx(5.0)

    def test_divisao_com_resultado_decimal(self):
        """Caso com resultado decimal."""
        assert dividir(7, 2) == pytest.approx(3.5)

    def test_divisao_por_zero_retorna_none(self):
        """Caso crítico: divisão por zero deve retornar None."""
        resultado = dividir(5, 0)
        assert resultado is None

    def test_divisao_com_numerador_zero(self):
        """Caso: zero dividido por qualquer número é zero."""
        assert dividir(0, 5) == pytest.approx(0.0)

    def test_divisao_com_negativos(self):
        """Caso com número negativo no numerador."""
        assert dividir(-10, 2) == pytest.approx(-5.0)

    def test_divisao_retorna_float(self):
        """Verifica que a função sempre retorna float (ou None)."""
        resultado = dividir(6, 3)
        # 6/3 = 2.0 — mesmo sendo divisão exata, retorna float
        assert isinstance(resultado, float)


# ============================================================
# TESTES PARA e_positivo()
# ============================================================

class TestEPositivo:
    """Agrupa todos os testes da função e_positivo."""

    def test_numero_positivo_grande(self):
        """Caso normal: número claramente positivo."""
        assert e_positivo(100) is True

    def test_numero_negativo(self):
        """Caso normal: número negativo não é positivo."""
        assert e_positivo(-7) is False

    def test_zero_nao_e_positivo(self):
        """Caso limite crítico: zero NÃO é estritamente positivo."""
        assert e_positivo(0) is False

    def test_float_positivo_pequeno(self):
        """Caso com float muito pequeno mas positivo."""
        assert e_positivo(0.001) is True

    def test_float_negativo(self):
        """Caso com float negativo."""
        assert e_positivo(-0.5) is False

    def test_retorna_booleano(self):
        """Verifica que a função retorna booleano puro."""
        assert isinstance(e_positivo(5), bool)
        assert isinstance(e_positivo(-5), bool)


# ============================================================
# TESTES PARA concatenar_nome()
# ============================================================

class TestConcatenarNome:
    """Agrupa todos os testes da função concatenar_nome."""

    def test_nome_e_sobrenome_minusculos(self):
        """Caso normal: ambos em minúsculo devem ser capitalizados."""
        assert concatenar_nome("ana", "silva") == "Ana Silva"

    def test_nome_e_sobrenome_maiusculos(self):
        """Caso: maiúsculas devem ser normalizadas para capitalize."""
        assert concatenar_nome("JOAO", "SOUZA") == "Joao Souza"

    def test_nome_com_espacos_extras(self):
        """Caso: espaços extras nas bordas devem ser removidos."""
        assert concatenar_nome("  Maria  ", "  Santos  ") == "Maria Santos"

    def test_nome_vazio_retorna_apenas_sobrenome(self):
        """Caso extremo: nome vazio — retorna apenas o sobrenome."""
        resultado = concatenar_nome("", "Silva")
        # O resultado não deve ter espaço extra no início
        assert resultado == "Silva"

    def test_retorna_string(self):
        """Verifica que a função sempre retorna uma string."""
        resultado = concatenar_nome("Carlos", "Lima")
        assert isinstance(resultado, str)

    def test_nome_ja_capitalizado(self):
        """Caso: nome já capitalizado corretamente."""
        assert concatenar_nome("Pedro", "Alves") == "Pedro Alves"


# ============================================================
# TESTES PARA calcular_imc()
# ============================================================

class TestCalcularImc:
    """Agrupa todos os testes da função calcular_imc."""

    def test_imc_normal(self):
        """Caso normal: IMC dentro da faixa saudável."""
        resultado = calcular_imc(70, 1.75)
        # 70 / (1.75²) = 70 / 3.0625 ≈ 22.86
        assert resultado["imc"] == pytest.approx(22.86, rel=1e-2)
        assert resultado["classificacao"] == "Normal"

    def test_imc_abaixo_do_peso(self):
        """Caso: IMC abaixo de 18.5."""
        resultado = calcular_imc(45, 1.70)
        # 45 / (1.70²) = 45 / 2.89 ≈ 15.57
        assert resultado["classificacao"] == "Abaixo do peso"

    def test_imc_sobrepeso(self):
        """Caso: IMC entre 25 e 30."""
        resultado = calcular_imc(85, 1.75)
        # 85 / (1.75²) = 85 / 3.0625 ≈ 27.76
        assert resultado["classificacao"] == "Sobrepeso"

    def test_imc_obesidade(self):
        """Caso: IMC acima de 30."""
        resultado = calcular_imc(100, 1.70)
        # 100 / (1.70²) = 100 / 2.89 ≈ 34.6
        assert resultado["classificacao"] == "Obesidade"

    def test_peso_zero_retorna_none(self):
        """Caso extremo: peso zero é inválido."""
        assert calcular_imc(0, 1.75) is None

    def test_altura_zero_retorna_none(self):
        """Caso extremo: altura zero causaria divisão por zero."""
        assert calcular_imc(70, 0) is None

    def test_peso_negativo_retorna_none(self):
        """Caso extremo: peso negativo é biologicamente impossível."""
        assert calcular_imc(-10, 1.75) is None

    def test_resultado_e_dicionario(self):
        """Verifica que o resultado é um dicionário com as chaves corretas."""
        resultado = calcular_imc(70, 1.75)
        assert isinstance(resultado, dict)
        assert "imc" in resultado
        assert "classificacao" in resultado

    def test_imc_e_float(self):
        """Verifica que o campo imc é um número (int ou float)."""
        resultado = calcular_imc(70, 1.75)
        assert isinstance(resultado["imc"], (int, float))

# ============================================================
# TESTES PARA converter_temperatura()
# ============================================================

class TestConverterTemperatura:

    def test_zero_celsius(self):
        resultado = converter_temperatura(0)
        # 0°C = 32°F = 273.15K
        assert resultado["fahrenheit"] == pytest.approx(32.0)
        assert resultado["kelvin"] == pytest.approx(273.15)

    def test_cem_celsius(self):
        resultado = converter_temperatura(100)
        # 100°C = 212°F = 373.15K
        assert resultado["fahrenheit"] == pytest.approx(212.0)
        assert resultado["kelvin"] == pytest.approx(373.15)

    def test_temperatura_impossivel(self):
        # Abaixo do zero absoluto — fisicamente impossível
        assert converter_temperatura(-300) is None

    def test_zero_absoluto(self):
        # Exatamente o zero absoluto é válido (o limite)
        resultado = converter_temperatura(-273.15)
        assert resultado is not None
        assert resultado["kelvin"] == pytest.approx(0.0)