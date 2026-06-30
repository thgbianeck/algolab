# classificador.py
# Aula 03: Estruturas de Decisão: if, elif e else
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa quatro funções que demonstram o uso de
# estruturas de decisão para classificar e tomar decisões.
# Cada função é autocontida e independente das demais.


def classificar_nota(nota):
    """
    Classifica uma nota escolar em três categorias.

    Regras de classificação:
        - Aprovado:     nota >= 7.0
        - Recuperação:  5.0 <= nota < 7.0
        - Reprovado:    nota < 5.0

    ENTRADA: nota — número (int ou float) entre 0 e 10
    SAÍDA: string com a classificação ('Aprovado', 'Recuperação' ou 'Reprovado'),
           ou 'Nota inválida' se a nota estiver fora do intervalo [0, 10]

    Exemplos:
        classificar_nota(8.5)  → 'Aprovado'
        classificar_nota(6.0)  → 'Recuperação'
        classificar_nota(3.0)  → 'Reprovado'
        classificar_nota(7.0)  → 'Aprovado'   (limite exato é aprovado)
        classificar_nota(11)   → 'Nota inválida'
    """

    # PASSO 1: Validar se a nota está dentro do intervalo permitido [0, 10]
    # Usamos a sintaxe encadeada do Python: 0 <= nota <= 10
    # que é equivalente a: nota >= 0 and nota <= 10
    if not (0 <= nota <= 10):
        # A nota está fora do intervalo válido — retornamos uma mensagem de erro
        return "Nota inválida"

    # PASSO 2: Verificar o critério de aprovação
    # A condição mais restritiva (maior limiar) vem primeiro
    if nota >= 7.0:
        # Nota suficiente para aprovação direta
        return "Aprovado"

    # PASSO 3: Verificar o critério de recuperação
    # Só chegamos aqui se nota < 7.0 (o if anterior foi False)
    elif nota >= 5.0:
        # Nota entre 5.0 (inclusive) e 7.0 (exclusive) — recuperação
        return "Recuperação"

    # PASSO 4: Caso padrão — nota abaixo de 5.0
    # Só chegamos aqui se nota < 5.0 (todos os elif anteriores foram False)
    else:
        return "Reprovado"


def classificar_idade(idade):
    """
    Classifica uma pessoa em faixas etárias.

    Faixas etárias:
        - Criança:     0 a 12 anos (inclusive)
        - Adolescente: 13 a 17 anos (inclusive)
        - Adulto:      18 a 59 anos (inclusive)
        - Idoso:       60 anos ou mais

    ENTRADA: idade — número inteiro representando a idade em anos
    SAÍDA: string com a faixa etária, ou 'Idade inválida' se negativa

    Exemplos:
        classificar_idade(8)   → 'Criança'
        classificar_idade(15)  → 'Adolescente'
        classificar_idade(30)  → 'Adulto'
        classificar_idade(65)  → 'Idoso'
        classificar_idade(-1)  → 'Idade inválida'
    """

    # PASSO 1: Validar que a idade não é negativa
    # Uma idade negativa é biologicamente impossível
    if idade < 0:
        return "Idade inválida"

    # PASSO 2: Verificar cada faixa etária em ordem crescente de limite
    # Começamos pelo limite mais baixo e avançamos para os maiores
    if idade <= 12:
        # De 0 a 12 anos — fase da infância
        return "Criança"

    elif idade <= 17:
        # De 13 a 17 anos — chegamos aqui porque idade > 12
        # então não precisamos verificar idade >= 13 explicitamente
        return "Adolescente"

    elif idade <= 59:
        # De 18 a 59 anos — chegamos aqui porque idade > 17
        return "Adulto"

    else:
        # 60 anos ou mais — todos os elif anteriores foram False
        # portanto idade >= 60
        return "Idoso"


def dia_e_util(dia_semana):
    """
    Verifica se um dia da semana é um dia útil de trabalho.

    Dias úteis: segunda, terça, quarta, quinta e sexta.
    Dias não úteis: sábado e domingo.

    ENTRADA: dia_semana — string com o nome do dia em português
             (aceita maiúsculas, minúsculas ou misto)
    SAÍDA: True se for dia útil, False se for fim de semana,
           None se o dia não for reconhecido

    Exemplos:
        dia_e_util("segunda")   → True
        dia_e_util("Sábado")    → False
        dia_e_util("DOMINGO")   → False
        dia_e_util("segunda")   → True
        dia_e_util("feriado")   → None
    """

    # PASSO 1: Normalizar o texto para minúsculas
    # Isso permite aceitar "Segunda", "SEGUNDA", "segunda" da mesma forma
    # O método .lower() retorna uma nova string com todos os caracteres
    # convertidos para minúsculas — a string original não é modificada
    dia_normalizado = dia_semana.lower().strip()

    # PASSO 2: Verificar se é um dia de fim de semana
    # Usamos o operador 'or' para combinar as duas condições em uma linha
    if dia_normalizado == "sábado" or dia_normalizado == "sabado":
        # Sábado não é dia útil — com ou sem acento
        return False

    elif dia_normalizado == "domingo":
        # Domingo não é dia útil
        return False

    # PASSO 3: Verificar se é um dia útil conhecido
    # Usamos o operador 'in' para verificar se o dia está na lista de úteis
    elif dia_normalizado in ["segunda", "terça", "terca", "quarta",
                              "quinta", "sexta"]:
        # O dia está na lista de dias úteis
        return True

    # PASSO 4: Dia não reconhecido
    else:
        # O texto não corresponde a nenhum dia da semana conhecido
        # Retornamos None para distinguir "não é dia útil" de "não reconhecido"
        return None


def calcular_desconto(valor, tipo_cliente):
    """
    Calcula o preço final após aplicar desconto baseado no tipo de cliente.

    Tabela de descontos:
        - 'vip':     30% de desconto
        - 'regular': 10% de desconto
        - 'novo':     5% de desconto
        - outros:     sem desconto (0%)

    ENTRADA: valor        — preço original (int ou float, deve ser >= 0)
             tipo_cliente — string com o tipo do cliente
    SAÍDA: dicionário com 'desconto_percentual', 'valor_desconto'
           e 'valor_final', todos arredondados em 2 casas decimais,
           ou None se o valor for negativo

    Exemplos:
        calcular_desconto(100.0, 'vip')     → {'desconto_percentual': 30, ...}
        calcular_desconto(100.0, 'regular') → {'desconto_percentual': 10, ...}
        calcular_desconto(100.0, 'novo')    → {'desconto_percentual': 5, ...}
        calcular_desconto(100.0, 'outro')   → {'desconto_percentual': 0, ...}
        calcular_desconto(-50.0, 'vip')     → None
    """

    # PASSO 1: Validar que o valor não é negativo
    # Um preço negativo não faz sentido comercialmente
    if valor < 0:
        return None

    # PASSO 2: Normalizar o tipo de cliente para minúsculas
    # Garante que 'VIP', 'Vip' e 'vip' sejam tratados da mesma forma
    tipo_normalizado = tipo_cliente.lower().strip()

    # PASSO 3: Determinar o percentual de desconto com base no tipo
    # Cada ramo do if-elif-else atribui um valor diferente a 'percentual'
    if tipo_normalizado == "vip":
        # Clientes VIP recebem o maior desconto: 30%
        percentual = 30

    elif tipo_normalizado == "regular":
        # Clientes regulares recebem desconto intermediário: 10%
        percentual = 10

    elif tipo_normalizado == "novo":
        # Novos clientes recebem um desconto de boas-vindas: 5%
        percentual = 5

    else:
        # Qualquer outro tipo não recebe desconto
        percentual = 0

    # PASSO 4: Calcular o valor do desconto em reais
    # Dividimos o percentual por 100 para obter a fração decimal
    # Ex: 30% de R$100 = 100 * (30/100) = 100 * 0.30 = R$30
    valor_desconto = valor * (percentual / 100)

    # PASSO 5: Calcular o valor final após o desconto
    valor_final = valor - valor_desconto

    # PASSO 6: Montar e retornar o dicionário com os resultados
    # Arredondamos os valores monetários para 2 casas decimais
    return {
        "desconto_percentual": percentual,
        "valor_desconto": round(valor_desconto, 2),
        "valor_final": round(valor_final, 2)
    }

def calcular_imposto(salario):
    """
    Calcula o imposto de renda mensal com base em faixas progressivas.

    ENTRADA: salario — salário bruto mensal (int ou float)
    SAÍDA: dicionário com aliquota, imposto e salario_liquido,
           ou None se o salário for negativo
    """

    # PASSO 1: Validar que o salário não é negativo
    if salario < 0:
        return None

    # PASSO 2: Determinar a alíquota com base na faixa salarial
    # As condições estão ordenadas do maior para o menor limiar
    if salario <= 2000.0:
        # Faixa de isenção — sem imposto
        aliquota = 0

    elif salario <= 3000.0:
        # Faixa de 7,5% — chegamos aqui porque salario > 2000
        aliquota = 7.5

    elif salario <= 4500.0:
        # Faixa de 15% — chegamos aqui porque salario > 3000
        aliquota = 15

    else:
        # Faixa de 22,5% — salario > 4500
        aliquota = 22.5

    # PASSO 3: Calcular o valor do imposto
    imposto = salario * (aliquota / 100)

    # PASSO 4: Calcular o salário líquido
    salario_liquido = salario - imposto

    # PASSO 5: Retornar o dicionário com os resultados
    return {
        "aliquota": aliquota,
        "imposto": round(imposto, 2),
        "salario_liquido": round(salario_liquido, 2)
    }
