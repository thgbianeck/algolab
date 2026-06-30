# algoritmo_intro.py
# Aula 01: O que é um Algoritmo? Pensamento Computacional e Lógica
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa três funções que representam algoritmos do cotidiano.
# Cada função demonstra os três pilares de qualquer algoritmo:
# ENTRADA → PROCESSAMENTO → SAÍDA


def fazer_sanduiche(ingredientes):
    """
    Algoritmo para montar um sanduíche com base nos ingredientes disponíveis.

    ENTRADA: ingredientes — uma lista de strings com os ingredientes disponíveis
    SAÍDA: uma lista de strings com os passos de montagem do sanduíche

    Exemplo:
        fazer_sanduiche(["pão", "queijo", "presunto"])
        → ["1. Pegue o pão", "2. Adicione queijo", "3. Adicione presunto", "4. Feche o sanduíche"]
    """

    # PASSO 1: Verificar se a lista de ingredientes está vazia
    # Se não há ingredientes, não há sanduíche a ser feito
    if not ingredientes:
        # Retornamos uma lista com uma única mensagem de aviso
        return ["Sem ingredientes disponíveis para montar o sanduíche."]

    # PASSO 2: Inicializar a lista de passos com uma lista vazia
    # Esta lista vai crescer conforme adicionarmos cada passo
    passos = []

    # PASSO 3: O primeiro passo é sempre pegar o pão (o primeiro ingrediente)
    # Usamos f-string para criar uma string formatada com o número do passo
    passos.append(f"1. Pegue o {ingredientes[0]}")

    # PASSO 4: Para cada ingrediente restante (a partir do segundo),
    # adicionamos um passo de "Adicione [ingrediente]"
    # Usamos range começando em 1 para pular o primeiro ingrediente (já usado)
    for i in range(1, len(ingredientes)):
        # len(passos) + 1 garante que o número do passo seja sequencial
        numero_passo = len(passos) + 1
        passos.append(f"{numero_passo}. Adicione {ingredientes[i]}")

    # PASSO 5: O último passo é sempre fechar o sanduíche
    numero_final = len(passos) + 1
    passos.append(f"{numero_final}. Feche o sanduíche")

    # SAÍDA: retornamos a lista completa de passos
    return passos


def calcular_media(numeros):
    """
    Algoritmo para calcular a média aritmética de uma lista de números.

    ENTRADA: numeros — uma lista de números inteiros ou decimais
    SAÍDA: a média aritmética como um número decimal (float),
           ou None se a lista estiver vazia

    Exemplo:
        calcular_media([7, 3, 9, 4, 5]) → 5.6
        calcular_media([]) → None
    """

    # PASSO 1: Verificar se a lista está vazia
    # Dividir por zero causaria um erro, então tratamos este caso antes
    if not numeros:
        # Retornamos None para indicar que a operação não é possível
        return None

    # PASSO 2: Calcular o total somando todos os elementos da lista
    # Inicializamos o acumulador com zero
    total = 0

    # Percorremos cada número da lista e somamos ao acumulador
    for numero in numeros:
        total = total + numero  # equivalente a: total += numero

    # PASSO 3: Contar quantos elementos existem na lista
    # A função len() retorna o número de elementos
    quantidade = len(numeros)

    # PASSO 4: Calcular a média dividindo o total pela quantidade
    # Em Python 3, a divisão com / sempre retorna float
    media = total / quantidade

    # SAÍDA: retornamos a média calculada
    return media


def e_maior_de_idade(idade):
    """
    Algoritmo para verificar se uma pessoa é maior de idade.

    ENTRADA: idade — um número inteiro representando a idade da pessoa
    SAÍDA: True se a pessoa tem 18 anos ou mais, False caso contrário

    Exemplo:
        e_maior_de_idade(20) → True
        e_maior_de_idade(16) → False
        e_maior_de_idade(18) → True  (exatamente 18 já é maior de idade)
    """

    # PASSO 1: Validar a entrada — idade não pode ser negativa
    # Uma idade negativa não faz sentido no mundo real
    if idade < 0:
        # Retornamos False, pois uma idade inválida não pode ser maior de idade
        return False

    # PASSO 2: Comparar a idade com o limite legal de maioridade (18 anos)
    # O operador >= verifica se a idade é maior OU igual a 18
    if idade >= 18:
        # SAÍDA caso verdadeiro: a pessoa é maior de idade
        return True
    else:
        # SAÍDA caso falso: a pessoa é menor de idade
        return False

def e_par(numero):
    """
    Verifica se um número inteiro é par.

    ENTRADA: numero — um inteiro (positivo, negativo ou zero)
    SAÍDA: True se o número for par, False se for ímpar

    O operador % (módulo) retorna o resto da divisão.
    Um número é par quando o resto da divisão por 2 é zero.
    """

    # O operador % calcula o resto da divisão
    # Se numero % 2 == 0, não há resto — o número é par
    if numero % 2 == 0:
        return True   # Par
    else:
        return False  # Ímpar