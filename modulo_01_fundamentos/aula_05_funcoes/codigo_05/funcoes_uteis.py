# funcoes_uteis.py
# Aula 05: Funções: Reutilizando e Organizando Algoritmos
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa quatro funções que demonstram:
# - Parâmetros com valores padrão
# - Retorno múltiplo
# - Verificação de primo encapsulada em função
# - Funções como argumentos (higher-order functions)
# Cada função é autocontida e independente das demais.


def saudar(nome, saudacao="Olá"):
    """
    Gera uma mensagem de saudação personalizada.

    Demonstra: parâmetro com valor padrão, f-string, parâmetro opcional.

    ENTRADA: nome     — string com o nome da pessoa a ser saudada
             saudacao — string com a saudação desejada (padrão: "Olá")
    SAÍDA: string formatada no padrão "Saudação, Nome!"

    Exemplos:
        saudar("Ana")                → "Olá, Ana!"
        saudar("Carlos", "Bom dia") → "Bom dia, Carlos!"
        saudar("  Maria  ")         → "Olá, Maria!"  (espaços removidos)
        saudar("pedro", "Oi")       → "Oi, Pedro!"   (nome capitalizado)
    """

    # PASSO 1: Normalizar o nome — remover espaços e capitalizar
    # .strip() remove espaços nas bordas
    # .capitalize() coloca a primeira letra maiúscula e o restante minúsculo
    nome_formatado = nome.strip().capitalize()

    # PASSO 2: Normalizar a saudação — remover espaços nas bordas
    saudacao_formatada = saudacao.strip()

    # PASSO 3: Montar e retornar a mensagem usando f-string
    # f-strings permitem inserir expressões dentro de strings com {}
    return f"{saudacao_formatada}, {nome_formatado}!"


def calcular_estatisticas(numeros):
    """
    Calcula o mínimo, máximo e média de uma lista de números.

    Demonstra: retorno múltiplo com tupla, funções auxiliares internas,
               tratamento de lista vazia com None.

    ENTRADA: numeros — lista de números inteiros ou decimais
    SAÍDA: tupla (minimo, maximo, media) com os três valores calculados,
           ou (None, None, None) se a lista estiver vazia

    Exemplos:
        calcular_estatisticas([7, 3, 9, 4, 5])  → (3, 9, 5.6)
        calcular_estatisticas([42])              → (42, 42, 42.0)
        calcular_estatisticas([])               → (None, None, None)
    """

    # PASSO 1: Tratar o caso de lista vazia
    # Uma lista vazia não tem mínimo, máximo nem média
    # Retornamos três None como tupla para manter a assinatura consistente
    if not numeros:
        return None, None, None

    # PASSO 2: Calcular o mínimo manualmente com laço
    # Iniciamos assumindo que o primeiro elemento é o menor
    minimo = numeros[0]

    # Percorremos os demais elementos procurando um menor
    for numero in numeros:
        if numero < minimo:
            # Encontramos um valor menor — atualizamos o mínimo
            minimo = numero

    # PASSO 3: Calcular o máximo manualmente com laço
    # Iniciamos assumindo que o primeiro elemento é o maior
    maximo = numeros[0]

    # Percorremos os demais elementos procurando um maior
    for numero in numeros:
        if numero > maximo:
            # Encontramos um valor maior — atualizamos o máximo
            maximo = numero

    # PASSO 4: Calcular a média
    # Somamos todos os elementos e dividimos pela quantidade
    total = 0
    for numero in numeros:
        total += numero

    # A divisão com / sempre retorna float em Python 3
    media = total / len(numeros)

    # PASSO 5: Retornar os três valores como tupla
    # Python empacota automaticamente múltiplos valores em uma tupla
    # O chamador pode desempacotá-los: mn, mx, med = calcular_estatisticas(lista)
    return minimo, maximo, media


def e_primo(numero):
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que só é divisível por 1 e por si mesmo.

    Demonstra: encapsulamento de lógica complexa em função reutilizável,
               laço for com break, retorno booleano, casos especiais.

    ENTRADA: numero — inteiro qualquer
    SAÍDA: True se o número for primo, False caso contrário

    Exemplos:
        e_primo(2)   → True   (o menor número primo)
        e_primo(3)   → True
        e_primo(4)   → False  (4 = 2 * 2)
        e_primo(17)  → True
        e_primo(1)   → False  (por definição, 1 não é primo)
        e_primo(-5)  → False  (negativos não são primos)
        e_primo(0)   → False
    """

    # PASSO 1: Tratar os casos especiais que não são primos por definição
    # Números menores ou iguais a 1 nunca são primos
    if numero <= 1:
        return False

    # PASSO 2: O número 2 é o único primo par — tratamos separadamente
    # Isso evita que o laço abaixo precise verificar 2 como divisor
    if numero == 2:
        return True

    # PASSO 3: Números pares maiores que 2 nunca são primos
    # (são divisíveis por 2)
    if numero % 2 == 0:
        return False

    # PASSO 4: Verificar divisibilidade por ímpares de 3 até sqrt(numero)
    # Se numero tem um divisor maior que sua raiz quadrada,
    # então também tem um divisor menor que a raiz — já teríamos encontrado.
    # Portanto, só precisamos verificar até a raiz quadrada.
    # Usamos numero ** 0.5 para calcular a raiz quadrada sem importar math
    divisor = 3
    while divisor <= numero ** 0.5:
        if numero % divisor == 0:
            # Encontramos um divisor — o número não é primo
            return False
        # Avançamos de dois em dois (apenas ímpares, pois pares já foram descartados)
        divisor += 2

    # PASSO 5: Se chegamos aqui, nenhum divisor foi encontrado — é primo!
    return True


def aplicar_operacao(numero, operacao):
    """
    Aplica uma função (operação) a um número e retorna o resultado.

    Demonstra: função como argumento (higher-order function),
               separação entre COMO fazer (operação) e O QUE fazer (aplicar).

    ENTRADA: numero   — número inteiro ou decimal a ser processado
             operacao — função que recebe um número e retorna um número
    SAÍDA: o resultado de chamar operacao(numero)

    Exemplos (assumindo as funções dobrar e triplicar definidas fora):
        aplicar_operacao(5, dobrar)     → 10
        aplicar_operacao(5, triplicar)  → 15
        aplicar_operacao(4, quadrado)   → 16
    """

    # PASSO 1: Chamar a função recebida como argumento, passando o número
    # 'operacao' é uma variável que aponta para uma função
    # 'operacao(numero)' chama essa função com 'numero' como argumento
    # Não usamos 'operacao()' com parênteses na definição — apenas no momento de chamar
    resultado = operacao(numero)

    # PASSO 2: Retornar o resultado da operação aplicada
    return resultado


# --- Funções auxiliares para demonstrar aplicar_operacao() ---
# Estas funções são simples transformações numéricas
# que serão passadas como argumento para aplicar_operacao()

def dobrar(numero):
    """Retorna o dobro do número recebido."""
    # Multiplica o número por 2 e retorna o resultado
    return numero * 2


def triplicar(numero):
    """Retorna o triplo do número recebido."""
    # Multiplica o número por 3 e retorna o resultado
    return numero * 3


def quadrado(numero):
    """Retorna o quadrado do número recebido (numero elevado a 2)."""
    # Usa o operador de exponenciação ** para elevar ao quadrado
    return numero ** 2


def inverter_sinal(numero):
    """Retorna o número com o sinal invertido."""
    # Multiplica por -1 para inverter o sinal
    return numero * -1

def contar_vogais(texto):
    """
    Conta vogais em uma string, retornando total e contagem por vogal.

    ENTRADA: texto — string qualquer
    SAÍDA: dicionário com 'total' e 'por_vogal'
    """

    # Definir o conjunto de vogais que queremos contar
    vogais = "aeiou"

    # Inicializar o dicionário de contagem por vogal
    # Cada vogal começa com contagem zero
    por_vogal = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    # Inicializar o contador total
    total = 0

    # Percorrer cada caractere do texto
    for caractere in texto.lower():  # .lower() para ignorar maiúsculas
        # Verificar se o caractere é uma vogal
        if caractere in vogais:
            # Incrementar a contagem desta vogal específica
            por_vogal[caractere] += 1
            # Incrementar o total de vogais
            total += 1

    # Retornar dicionário com as duas informações
    return {"total": total, "por_vogal": por_vogal}


def aplicar_e_filtrar(numeros, operacao, minimo):
    """
    Aplica uma operação a cada número e retorna apenas os resultados >= minimo.

    ENTRADA: numeros   — lista de números
             operacao  — função a aplicar a cada número
             minimo    — valor mínimo para incluir no resultado
    SAÍDA: lista com os resultados da operação que são >= minimo
    """

    # Inicializar a lista de resultados filtrados
    resultados = []

    # Percorrer cada número da lista
    for numero in numeros:
        # Aplicar a operação ao número atual
        resultado = operacao(numero)

        # Verificar se o resultado atende ao critério mínimo
        if resultado >= minimo:
            # Incluir no resultado apenas se passar pelo filtro
            resultados.append(resultado)

    return resultados
