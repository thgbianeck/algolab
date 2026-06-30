# test_classificador.py
# Testes automatizados para a Aula 03: Estruturas de Decisão
# Execute com: pytest testes/ -v
#
# Filosofia dos testes: cada ramo de cada função tem pelo menos um teste.
# Para condições de limite, testamos o valor exato, um abaixo e um acima.

import pytest

# Importamos as quatro funções que vamos testar
from codigo_03.classificador import (
    classificar_nota,
    classificar_idade,
    dia_e_util,
    calcular_desconto,
    calcular_imposto,
)


# ============================================================
# TESTES PARA classificar_nota()
# ============================================================

class TestClassificarNota:
    """
    Testa todos os ramos da função classificar_nota.
    Ramos: Aprovado | Recuperação | Reprovado | Nota inválida
    """

    # --- Ramo: Aprovado ---

    def test_nota_alta_aprovado(self):
        """Nota claramente dentro da faixa de aprovação."""
        assert classificar_nota(9.0) == "Aprovado"

    def test_nota_limite_aprovado(self):
        """Nota exatamente no limite de aprovação — 7.0 deve aprovar."""
        # Este é o caso de limite mais importante: 7.0 deve ser Aprovado
        assert classificar_nota(7.0) == "Aprovado"

    def test_nota_maxima(self):
        """Nota máxima possível (10) deve ser Aprovado."""
        assert classificar_nota(10) == "Aprovado"

    # --- Ramo: Recuperação ---

    def test_nota_media_recuperacao(self):
        """Nota no meio da faixa de recuperação."""
        assert classificar_nota(6.0) == "Recuperação"

    def test_nota_limite_inferior_recuperacao(self):
        """Nota exatamente em 5.0 — limite inferior da recuperação."""
        # 5.0 deve ser Recuperação, não Reprovado
        assert classificar_nota(5.0) == "Recuperação"

    def test_nota_logo_abaixo_do_aprovado(self):
        """Nota ligeiramente abaixo de 7.0 deve ser Recuperação."""
        assert classificar_nota(6.9) == "Recuperação"

    # --- Ramo: Reprovado ---

    def test_nota_baixa_reprovado(self):
        """Nota claramente dentro da faixa de reprovação."""
        assert classificar_nota(2.0) == "Reprovado"

    def test_nota_zero_reprovado(self):
        """Nota zero deve ser Reprovado."""
        assert classificar_nota(0) == "Reprovado"

    def test_nota_logo_abaixo_da_recuperacao(self):
        """Nota ligeiramente abaixo de 5.0 deve ser Reprovado."""
        assert classificar_nota(4.9) == "Reprovado"

    # --- Ramo: Nota inválida ---

    def test_nota_acima_de_dez(self):
        """Nota acima de 10 é inválida."""
        assert classificar_nota(11) == "Nota inválida"

    def test_nota_negativa(self):
        """Nota negativa é inválida."""
        assert classificar_nota(-1) == "Nota inválida"

    def test_nota_muito_alta(self):
        """Nota muito acima do máximo é inválida."""
        assert classificar_nota(100) == "Nota inválida"

    # --- Verificação de tipo ---

    def test_retorna_string(self):
        """A função deve sempre retornar uma string."""
        assert isinstance(classificar_nota(8.0), str)
        assert isinstance(classificar_nota(0), str)


# ============================================================
# TESTES PARA classificar_idade()
# ============================================================

class TestClassificarIdade:
    """
    Testa todos os ramos da função classificar_idade.
    Ramos: Criança | Adolescente | Adulto | Idoso | Idade inválida
    """

    # --- Ramo: Criança ---

    def test_crianca_tipica(self):
        """Criança com idade claramente na faixa."""
        assert classificar_idade(8) == "Criança"

    def test_recem_nascido(self):
        """Recém-nascido com idade zero deve ser Criança."""
        assert classificar_idade(0) == "Criança"

    def test_limite_superior_crianca(self):
        """12 anos é o limite superior da infância."""
        assert classificar_idade(12) == "Criança"

    # --- Ramo: Adolescente ---

    def test_adolescente_tipico(self):
        """Adolescente com idade claramente na faixa."""
        assert classificar_idade(15) == "Adolescente"

    def test_limite_inferior_adolescente(self):
        """13 anos é o primeiro ano da adolescência."""
        assert classificar_idade(13) == "Adolescente"

    def test_limite_superior_adolescente(self):
        """17 anos é o último ano da adolescência."""
        assert classificar_idade(17) == "Adolescente"

    # --- Ramo: Adulto ---

    def test_adulto_tipico(self):
        """Adulto com idade claramente na faixa."""
        assert classificar_idade(35) == "Adulto"

    def test_limite_inferior_adulto(self):
        """18 anos é o primeiro ano da vida adulta."""
        assert classificar_idade(18) == "Adulto"

    def test_limite_superior_adulto(self):
        """59 anos é o último ano antes da terceira idade."""
        assert classificar_idade(59) == "Adulto"

    # --- Ramo: Idoso ---

    def test_idoso_tipico(self):
        """Idoso com idade claramente na faixa."""
        assert classificar_idade(70) == "Idoso"

    def test_limite_inferior_idoso(self):
        """60 anos é o primeiro ano da terceira idade."""
        assert classificar_idade(60) == "Idoso"

    def test_idoso_muito_velho(self):
        """Idade muito alta ainda deve ser Idoso."""
        assert classificar_idade(110) == "Idoso"

    # --- Ramo: Idade inválida ---

    def test_idade_negativa(self):
        """Idade negativa é biologicamente impossível."""
        assert classificar_idade(-1) == "Idade inválida"

    def test_retorna_string(self):
        """A função deve sempre retornar uma string."""
        assert isinstance(classificar_idade(25), str)


# ============================================================
# TESTES PARA dia_e_util()
# ============================================================

class TestDiaEUtil:
    """
    Testa todos os ramos da função dia_e_util.
    Ramos: True (dia útil) | False (fim de semana) | None (não reconhecido)
    """

    # --- Ramo: True (dias úteis) ---

    def test_segunda_e_util(self):
        """Segunda-feira é dia útil."""
        assert dia_e_util("segunda") is True

    def test_terca_e_util(self):
        """Terça-feira é dia útil."""
        assert dia_e_util("terça") is True

    def test_quarta_e_util(self):
        """Quarta-feira é dia útil."""
        assert dia_e_util("quarta") is True

    def test_quinta_e_util(self):
        """Quinta-feira é dia útil."""
        assert dia_e_util("quinta") is True

    def test_sexta_e_util(self):
        """Sexta-feira é dia útil."""
        assert dia_e_util("sexta") is True

    # --- Ramo: False (fim de semana) ---

    def test_sabado_nao_e_util(self):
        """Sábado não é dia útil."""
        assert dia_e_util("sábado") is False

    def test_sabado_sem_acento(self):
        """Sábado sem acento também deve ser reconhecido."""
        assert dia_e_util("sabado") is False

    def test_domingo_nao_e_util(self):
        """Domingo não é dia útil."""
        assert dia_e_util("domingo") is False

    # --- Normalização de entrada ---

    def test_aceita_maiusculas(self):
        """A função deve aceitar dias escritos em maiúsculas."""
        assert dia_e_util("SEGUNDA") is True
        assert dia_e_util("DOMINGO") is False

    def test_aceita_misto(self):
        """A função deve aceitar capitalização mista."""
        assert dia_e_util("Quarta") is True

    def test_aceita_espacos_extras(self):
        """A função deve ignorar espaços extras nas bordas."""
        assert dia_e_util("  sexta  ") is True

    # --- Ramo: None (dia não reconhecido) ---

    def test_dia_invalido_retorna_none(self):
        """Texto que não é um dia da semana retorna None."""
        assert dia_e_util("feriado") is None

    def test_string_vazia_retorna_none(self):
        """String vazia retorna None."""
        assert dia_e_util("") is None

    def test_numero_como_dia_retorna_none(self):
        """Número como string retorna None."""
        assert dia_e_util("1") is None


# ============================================================
# TESTES PARA calcular_desconto()
# ============================================================

class TestCalcularDesconto:
    """
    Testa todos os ramos da função calcular_desconto.
    Ramos: vip (30%) | regular (10%) | novo (5%) | outros (0%) | inválido
    """

    # --- Ramo: cliente vip ---

    def test_desconto_vip(self):
        """Cliente VIP recebe 30% de desconto."""
        resultado = calcular_desconto(100.0, "vip")
        assert resultado["desconto_percentual"] == 30
        assert resultado["valor_desconto"] == 30.0
        assert resultado["valor_final"] == 70.0

    def test_desconto_vip_maiusculo(self):
        """'VIP' em maiúsculas deve ser aceito."""
        resultado = calcular_desconto(100.0, "VIP")
        assert resultado["desconto_percentual"] == 30

    # --- Ramo: cliente regular ---

    def test_desconto_regular(self):
        """Cliente regular recebe 10% de desconto."""
        resultado = calcular_desconto(200.0, "regular")
        assert resultado["desconto_percentual"] == 10
        assert resultado["valor_desconto"] == 20.0
        assert resultado["valor_final"] == 180.0

    # --- Ramo: cliente novo ---

    def test_desconto_novo(self):
        """Novo cliente recebe 5% de desconto."""
        resultado = calcular_desconto(100.0, "novo")
        assert resultado["desconto_percentual"] == 5
        assert resultado["valor_desconto"] == 5.0
        assert resultado["valor_final"] == 95.0

    # --- Ramo: outros clientes (sem desconto) ---

    def test_sem_desconto_para_tipo_desconhecido(self):
        """Tipo de cliente desconhecido não recebe desconto."""
        resultado = calcular_desconto(100.0, "funcionario")
        assert resultado["desconto_percentual"] == 0
        assert resultado["valor_desconto"] == 0.0
        assert resultado["valor_final"] == 100.0

    # --- Casos extremos de valor ---

    def test_valor_zero(self):
        """Desconto sobre valor zero resulta em zero."""
        resultado = calcular_desconto(0.0, "vip")
        assert resultado["valor_final"] == 0.0

    def test_valor_negativo_retorna_none(self):
        """Valor negativo é inválido e deve retornar None."""
        assert calcular_desconto(-50.0, "vip") is None

    # --- Verificação da estrutura do retorno ---

    def test_resultado_e_dicionario_com_chaves_corretas(self):
        """O retorno deve ser um dicionário com as três chaves esperadas."""
        resultado = calcular_desconto(100.0, "regular")
        assert isinstance(resultado, dict)
        assert "desconto_percentual" in resultado
        assert "valor_desconto" in resultado
        assert "valor_final" in resultado

    def test_valores_arredondados_em_duas_casas(self):
        """Os valores monetários devem ter no máximo 2 casas decimais."""
        resultado = calcular_desconto(99.99, "novo")
        # 5% de 99.99 = 4.9995 — deve ser arredondado para 5.0
        assert resultado["valor_desconto"] == pytest.approx(5.0, rel=1e-2)

class TestCalcularImposto:

    def test_isento(self):
        resultado = calcular_imposto(1500.0)
        assert resultado["aliquota"] == 0
        assert resultado["imposto"] == 0.0
        assert resultado["salario_liquido"] == 1500.0

    def test_limite_isencao(self):
        resultado = calcular_imposto(2000.0)
        assert resultado["aliquota"] == 0

    def test_faixa_sete_e_meio(self):
        resultado = calcular_imposto(2500.0)
        assert resultado["aliquota"] == 7.5

    def test_faixa_quinze(self):
        resultado = calcular_imposto(4000.0)
        assert resultado["aliquota"] == 15

    def test_faixa_vinte_dois_e_meio(self):
        resultado = calcular_imposto(6000.0)
        assert resultado["aliquota"] == 22.5

    def test_salario_negativo(self):
        assert calcular_imposto(-100.0) is None