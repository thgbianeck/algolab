# repeticoes.py
# Aula 04: Estruturas de Repetição: for e while
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa quatro funções que demonstram o uso de
# laços for e while com break, continue e range().
# Cada função é autocontida e independente das demais.


def somar_lista(numeros):
    """
    Soma todos os elementos de uma lista usando um laço for.

    Demonstra: padrão acumulador com for, iteração sobre lista.

    ENTRADA: numeros — lista de números inteiros ou decimais
    SAÍDA: a soma de todos os elementos como número (int ou float),
           ou 0 se a lista estiver vazia

    Exemplos:
        somar_lista([1, 2, 3, 4, 5])  → 15
        somar_lista([])               → 0
        somar_lista([-3, 3])          → 0
        somar_lista([7])              → 7
    """

    # PASSO 1: Inicializar o acumulador com o elemento neutro da adição
    # O elemento neutro da soma é 0 — somar 0 não altera o resultado
    # Esta variável acumulará a soma de todos os elementos
    total = 0

    # PASSO 2: Iterar sobre cada número da lista com for
    # A cada iteração, 'numero' assume o valor do próximo elemento
    # Na primeira iteração: numero = numeros[0]
    # Na segunda iteração:  numero = numeros[1]
    # ... e assim por diante até o último elemento
    for numero in numeros:
        # Adicionar o elemento atual ao acumulador
        # total += numero é equivalente a total = total + numero
        total += numero

    # PASSO 3: Retornar o total acumulado
    # Se a lista estava vazia, o for não executou nenhuma iteração
    # e total permanece 0 — o valor correto para uma soma vazia
    return total


def contar_ate(limite):
    """
    Conta de 1 até o limite (inclusive) usando um laço while.

    Demonstra: laço while com contador, condição de parada, acumulador de lista.

    ENTRADA: limite — número inteiro positivo até onde contar
    SAÍDA: lista com todos os inteiros de 1 até limite (inclusive),
           ou lista vazia se limite for menor que 1

    Exemplos:
        contar_ate(5)  → [1, 2, 3, 4, 5]
        contar_ate(1)  → [1]
        contar_ate(0)  → []
        contar_ate(-3) → []
    """

    # PASSO 1: Inicializar o acumulador de resultado como lista vazia
    # Esta lista receberá cada número conforme contamos
    resultado = []

    # PASSO 2: Inicializar o contador — começamos em 1
    # O contador é a variável que controla o laço while
    contador = 1

    # PASSO 3: Executar o laço while enquanto o contador não ultrapassar o limite
    # A condição é verificada ANTES de cada iteração
    # Se limite < 1, a condição já começa False e o laço não executa
    while contador <= limite:
        # Adicionar o valor atual do contador à lista de resultado
        # O método append() adiciona um elemento ao final da lista
        resultado.append(contador)

        # CRÍTICO: incrementar o contador a cada iteração
        # Sem esta linha, o while executaria infinitamente
        # contador += 1 é equivalente a contador = contador + 1
        contador += 1

    # PASSO 4: Retornar a lista com os números contados
    return resultado


def encontrar_primeiro_par(numeros):
    """
    Encontra e retorna o primeiro número par de uma lista usando break.

    Demonstra: laço for com break para parada antecipada.

    ENTRADA: numeros — lista de números inteiros
    SAÍDA: o primeiro número par encontrado,
           ou None se não houver nenhum número par na lista

    Exemplos:
        encontrar_primeiro_par([3, 7, 4, 9, 2])  → 4
        encontrar_primeiro_par([1, 3, 5, 7])      → None
        encontrar_primeiro_par([2, 4, 6])          → 2
        encontrar_primeiro_par([])                 → None
    """

    # PASSO 1: Inicializar o resultado como None
    # None representa "nenhum par encontrado ainda"
    # Se o laço terminar sem encontrar nenhum par, retornamos None
    primeiro_par = None

    # PASSO 2: Iterar sobre cada número da lista
    for numero in numeros:
        # Verificar se o número atual é par
        # O operador % (módulo) retorna o resto da divisão por 2
        # Um número é par quando o resto da divisão por 2 é zero
        if numero % 2 == 0:
            # Encontramos o primeiro número par!
            # Guardamos o valor encontrado no resultado
            primeiro_par = numero

            # BREAK: interrompemos o laço imediatamente
            # Não precisamos continuar verificando os próximos elementos
            # pois já encontramos o que procurávamos
            break

        # Se o número não for par, o laço avança automaticamente
        # para o próximo elemento sem precisar de nenhuma instrução extra

    # PASSO 3: Retornar o resultado
    # Será o primeiro par encontrado, ou None se nenhum foi encontrado
    return primeiro_par


def filtrar_positivos(numeros):
    """
    Retorna uma nova lista contendo apenas os números positivos da lista original.

    Demonstra: laço for com continue para pular elementos indesejados.

    ENTRADA: numeros — lista de números inteiros ou decimais
    SAÍDA: nova lista com apenas os números estritamente positivos (> 0),
           preservando a ordem original

    Exemplos:
        filtrar_positivos([3, -1, 5, 0, -7, 2])  → [3, 5, 2]
        filtrar_positivos([-1, -2, -3])           → []
        filtrar_positivos([1, 2, 3])               → [1, 2, 3]
        filtrar_positivos([])                      → []
        filtrar_positivos([0, 0, 0])               → []  (0 não é positivo)
    """

    # PASSO 1: Inicializar a lista de resultado como vazia
    # Os números positivos serão adicionados aqui conforme os encontrarmos
    positivos = []

    # PASSO 2: Iterar sobre cada número da lista original
    for numero in numeros:
        # Verificar se o número NÃO é positivo (é zero ou negativo)
        # Usamos a condição negada para identificar os elementos a PULAR
        if numero <= 0:
            # CONTINUE: pula o restante do bloco para ESTA iteração
            # O laço avança imediatamente para o próximo elemento
            # sem executar o append() abaixo
            continue

        # Se chegamos aqui, o número é positivo (passou pelo filtro do continue)
        # Adicionamos à lista de resultados
        positivos.append(numero)

    # PASSO 3: Retornar a lista com apenas os positivos
    return positivos

def tabuada(numero):
    """
    Retorna os dez primeiros múltiplos de um número.

    ENTRADA: numero — inteiro qualquer
    SAÍDA: lista com numero*1, numero*2, ..., numero*10
    """

    # Inicializar a lista de múltiplos
    multiplos = []

    # range(1, 11) gera os valores 1, 2, 3, ..., 10
    # Multiplicador começa em 1 (não em 0) e vai até 10 (inclusive)
    for multiplicador in range(1, 11):
        # Calcular o múltiplo atual e adicionar à lista
        multiplos.append(numero * multiplicador)

    return multiplos


def tabuada_formatada(numero):
    """
    Retorna a tabuada de um número como lista de strings formatadas.

    ENTRADA: numero — inteiro qualquer
    SAÍDA: lista de strings no formato 'N x M = R'
    """

    # Inicializar a lista de linhas formatadas
    linhas = []

    # range(1, 11) gera os multiplicadores de 1 a 10
    for multiplicador in range(1, 11):
        # Calcular o resultado da multiplicação
        resultado = numero * multiplicador

        # Formatar a linha usando f-string
        # Exemplo: "7 x 3 = 21"
        linha = f"{numero} x {multiplicador} = {resultado}"

        # Adicionar a linha formatada à lista
        linhas.append(linha)

    return linhas