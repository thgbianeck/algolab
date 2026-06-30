# calculadora_basica.py
# Aula 02: Variáveis, Tipos de Dados e Operadores em Python
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa cinco funções que demonstram o uso de
# variáveis, tipos de dados e operadores em Python.
# Cada função é autocontida e independente das demais.


def somar(a, b):
    """
    Soma dois números e retorna o resultado.

    ENTRADA: a — primeiro número (int ou float)
             b — segundo número (int ou float)
    SAÍDA: a soma de a e b (int se ambos forem int, float caso contrário)

    Demonstra: operador aritmético +, tipagem dinâmica do Python.

    Exemplos:
        somar(3, 4)     → 7
        somar(1.5, 2.5) → 4.0
        somar(-5, 5)    → 0
    """

    # O operador + realiza adição entre dois números
    # Se ambos forem int, o resultado é int
    # Se pelo menos um for float, o resultado é float
    resultado = a + b

    # Retornamos o resultado da soma
    return resultado


def dividir(a, b):
    """
    Divide o primeiro número pelo segundo e retorna o resultado.

    ENTRADA: a — numerador (int ou float)
             b — denominador (int ou float)
    SAÍDA: o resultado da divisão como float,
           ou None se b for zero (divisão por zero não é permitida)

    Demonstra: operador /, tratamento de caso inválido, retorno de None.

    Exemplos:
        dividir(10, 2)  → 5.0
        dividir(7, 2)   → 3.5
        dividir(5, 0)   → None
    """

    # PASSO 1: Verificar se o denominador é zero
    # Divisão por zero não é matematicamente definida
    # Sem esta verificação, Python lançaria ZeroDivisionError
    if b == 0:
        # Retornamos None para indicar que a operação é impossível
        return None

    # PASSO 2: Realizar a divisão
    # O operador / em Python 3 SEMPRE retorna float, mesmo que o resultado
    # seja um número inteiro — 10 / 2 retorna 5.0, não 5
    resultado = a / b

    # Retornamos o resultado da divisão
    return resultado


def e_positivo(numero):
    """
    Verifica se um número é estritamente positivo (maior que zero).

    ENTRADA: numero — um número inteiro ou decimal
    SAÍDA: True se numero > 0, False caso contrário

    Demonstra: operador de comparação >, tipo bool como saída.

    Exemplos:
        e_positivo(5)    → True
        e_positivo(-3)   → False
        e_positivo(0)    → False  (zero NÃO é positivo)
        e_positivo(0.1)  → True
    """

    # O operador > retorna True se numero for maior que zero
    # e False caso contrário — isso é um valor booleano direto
    # Podemos retornar a comparação diretamente sem usar if
    return numero > 0


def concatenar_nome(nome, sobrenome):
    """
    Combina nome e sobrenome em uma string formatada.

    ENTRADA: nome      — string com o primeiro nome
             sobrenome — string com o sobrenome
    SAÍDA: string no formato "Nome Sobrenome" com as primeiras letras
           maiúsculas e um espaço entre as partes

    Demonstra: tipo str, operador + para concatenação, método .strip(),
               método .capitalize() e f-strings.

    Exemplos:
        concatenar_nome("ana", "silva")     → "Ana Silva"
        concatenar_nome("  João  ", "SOUZA") → "João Souza"
        concatenar_nome("", "Silva")         → "Silva"
    """

    # PASSO 1: Remover espaços extras nas bordas de cada string
    # O método .strip() remove espaços, tabs e quebras de linha
    # das extremidades esquerda e direita da string
    nome_limpo = nome.strip()
    sobrenome_limpo = sobrenome.strip()

    # PASSO 2: Capitalizar cada parte
    # O método .capitalize() coloca a primeira letra maiúscula
    # e o restante minúsculo — "ANA" vira "Ana", "silva" vira "Silva"
    nome_formatado = nome_limpo.capitalize()
    sobrenome_formatado = sobrenome_limpo.capitalize()

    # PASSO 3: Combinar as partes
    # Se o nome estiver vazio após o strip, retornamos apenas o sobrenome
    # O operador .strip() em nome_formatado remove espaço extra se nome vazio
    # Usamos f-string para combinar as partes com um espaço entre elas
    nome_completo = f"{nome_formatado} {sobrenome_formatado}".strip()

    # Retornamos o nome completo formatado
    return nome_completo


def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) de uma pessoa.

    Fórmula: IMC = peso / (altura ** 2)

    ENTRADA: peso   — peso em quilogramas (float ou int, deve ser > 0)
             altura — altura em metros (float ou int, deve ser > 0)
    SAÍDA: dicionário com 'imc' (float arredondado em 2 casas)
           e 'classificacao' (string com a categoria do IMC),
           ou None se os valores de entrada forem inválidos

    Demonstra: operador **, operador /, arredondamento com round(),
               operadores de comparação, dicionário como estrutura de saída.

    Exemplos:
        calcular_imc(70, 1.75)  → {'imc': 22.86, 'classificacao': 'Normal'}
        calcular_imc(0, 1.75)   → None
        calcular_imc(70, 0)     → None
    """

    # PASSO 1: Validar as entradas
    # Peso e altura devem ser maiores que zero para ter sentido biológico
    # O operador 'or' retorna True se pelo menos uma condição for verdadeira
    if peso <= 0 or altura <= 0:
        # Retornamos None para indicar entrada inválida
        return None

    # PASSO 2: Calcular o IMC
    # O operador ** realiza exponenciação: altura ** 2 é altura ao quadrado
    # O operador / realiza a divisão — resultado é sempre float
    imc = peso / (altura ** 2)

    # PASSO 3: Arredondar para 2 casas decimais
    # A função round(valor, casas) arredonda o float
    imc_arredondado = round(imc, 2)

    # PASSO 4: Classificar o IMC segundo a tabela da OMS
    # Usamos if-elif-else para verificar em qual faixa o IMC se enquadra
    if imc_arredondado < 18.5:
        # IMC abaixo do peso saudável
        classificacao = "Abaixo do peso"
    elif imc_arredondado < 25.0:
        # IMC dentro da faixa saudável
        classificacao = "Normal"
    elif imc_arredondado < 30.0:
        # IMC acima do ideal, mas não obeso
        classificacao = "Sobrepeso"
    else:
        # IMC acima de 30 — obesidade
        classificacao = "Obesidade"

    # PASSO 5: Montar e retornar o resultado como dicionário
    # Um dicionário permite retornar múltiplas informações organizadas
    return {
        "imc": imc_arredondado,
        "classificacao": classificacao
    }

def converter_temperatura(celsius):
    """
    Converte temperatura de Celsius para Fahrenheit e Kelvin.

    ENTRADA: celsius — temperatura em graus Celsius (int ou float)
    SAÍDA: dicionário com 'fahrenheit' e 'kelvin' arredondados em 2 casas,
           ou None se a temperatura for fisicamente impossível
    """

    # PASSO 1: Validar a entrada
    # O zero absoluto é -273.15°C — temperaturas abaixo disso são impossíveis
    if celsius < -273.15:
        return None

    # PASSO 2: Calcular Fahrenheit usando a fórmula de conversão
    # A ordem das operações importa: multiplicamos primeiro, depois somamos
    fahrenheit = celsius * 9 / 5 + 32

    # PASSO 3: Calcular Kelvin — simplesmente soma a constante 273.15
    kelvin = celsius + 273.15

    # PASSO 4: Arredondar ambos os resultados para 2 casas decimais
    fahrenheit_arredondado = round(fahrenheit, 2)
    kelvin_arredondado = round(kelvin, 2)

    # PASSO 5: Retornar o resultado como dicionário
    return {
        "fahrenheit": fahrenheit_arredondado,
        "kelvin": kelvin_arredondado
    }