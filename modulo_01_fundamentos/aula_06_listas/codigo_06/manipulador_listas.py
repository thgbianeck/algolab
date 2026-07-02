# manipulador_listas.py
# Aula 06: Listas em Python: Armazenando e Manipulando Coleções
# Curso: AlgoLab — Algoritmos do Básico ao Avançado com Python
#
# Este arquivo implementa quatro funções de manipulação de listas
# sem usar os métodos prontos do Python para as operações centrais.
# O objetivo é entender os algoritmos por trás das operações.
# Cada função é autocontida e independente das demais.


def inverter_lista(lista):
    """
    Inverte a ordem dos elementos de uma lista sem usar .reverse() ou [::-1].

    Implementa o algoritmo de dois ponteiros: um no início, outro no fim,
    trocando os elementos e avançando em direção ao centro.

    Demonstra: acesso por índice, troca de elementos, algoritmo de dois ponteiros,
               cópia de lista para não modificar o original.

    ENTRADA: lista — lista com qualquer número de elementos de qualquer tipo
    SAÍDA: nova lista com os elementos em ordem invertida
           (a lista original não é modificada)

    Exemplos:
        inverter_lista([1, 2, 3, 4, 5])  → [5, 4, 3, 2, 1]
        inverter_lista([1, 2])           → [2, 1]
        inverter_lista([42])             → [42]
        inverter_lista([])               → []
    """

    # PASSO 1: Criar uma cópia da lista original para não modificá-la
    # lista[:] é fatiamento completo — cria uma nova lista com os mesmos elementos
    # Modificar 'copia' não afetará 'lista'
    copia = lista[:]

    # PASSO 2: Inicializar os dois ponteiros
    # 'inicio' aponta para o primeiro elemento
    # 'fim' aponta para o último elemento
    inicio = 0
    fim = len(copia) - 1

    # PASSO 3: Executar o algoritmo de dois ponteiros
    # Enquanto 'inicio' não ultrapassar 'fim', trocamos os elementos
    # e aproximamos os ponteiros em direção ao centro
    while inicio < fim:
        # Trocar os elementos nas posições 'inicio' e 'fim'
        # Python permite trocar dois valores em uma linha com desempacotamento:
        # o lado direito é avaliado completamente antes das atribuições
        copia[inicio], copia[fim] = copia[fim], copia[inicio]

        # Avançar o ponteiro do início para a direita
        inicio += 1

        # Recuar o ponteiro do fim para a esquerda
        fim -= 1

    # PASSO 4: Retornar a cópia invertida
    # A lista original permanece inalterada
    return copia


def remover_duplicatas(lista):
    """
    Remove elementos duplicados de uma lista preservando a ordem de primeira aparição.

    Não usa set() diretamente para a operação central — implementa manualmente
    usando um conjunto auxiliar para rastrear elementos já vistos.

    Demonstra: uso de conjunto (set) como auxiliar, padrão de "já visto",
               preservação de ordem, laço com condição de inclusão.

    ENTRADA: lista — lista com qualquer número de elementos comparáveis
    SAÍDA: nova lista com cada elemento aparecendo apenas uma vez,
           na ordem em que apareceu pela primeira vez na lista original

    Exemplos:
        remover_duplicatas([1, 2, 3, 2, 1, 4])  → [1, 2, 3, 4]
        remover_duplicatas([3, 3, 3])            → [3]
        remover_duplicatas([1, 2, 3])            → [1, 2, 3]
        remover_duplicatas([])                   → []
    """

    # PASSO 1: Inicializar a lista de resultado (sem duplicatas)
    resultado = []

    # PASSO 2: Inicializar o conjunto auxiliar de elementos já vistos
    # Usamos um conjunto (set) porque verificar pertencimento em set é O(1)
    # enquanto verificar em uma lista é O(n)
    # O conjunto não precisa preservar ordem — só precisa responder "já vi isso?"
    ja_vistos = set()

    # PASSO 3: Percorrer cada elemento da lista original
    for elemento in lista:
        # Verificar se este elemento já foi visto antes
        if elemento not in ja_vistos:
            # Este elemento é novo — incluir no resultado
            resultado.append(elemento)

            # Registrar que já vimos este elemento
            # add() adiciona um elemento ao conjunto
            ja_vistos.add(elemento)

        # Se o elemento já foi visto (else implícito), simplesmente ignoramos
        # O continue é desnecessário aqui — o laço avança naturalmente

    # PASSO 4: Retornar a lista sem duplicatas
    return resultado


def mesclar_listas(lista_a, lista_b):
    """
    Une dois listas em uma única lista sem elementos duplicados.

    A ordem dos elementos é: primeiro os de lista_a (sem duplicatas),
    depois os de lista_b que ainda não apareceram em lista_a.

    Demonstra: composição de funções (usa remover_duplicatas internamente),
               concatenação de listas, reutilização de lógica existente.

    ENTRADA: lista_a — primeira lista de elementos
             lista_b — segunda lista de elementos
    SAÍDA: nova lista com todos os elementos únicos de ambas as listas,
           sem modificar as listas originais

    Exemplos:
        mesclar_listas([1, 2, 3], [3, 4, 5])     → [1, 2, 3, 4, 5]
        mesclar_listas([1, 2], [1, 2])             → [1, 2]
        mesclar_listas([], [1, 2])                 → [1, 2]
        mesclar_listas([1, 2], [])                 → [1, 2]
        mesclar_listas([], [])                     → []
        mesclar_listas([1, 1, 2], [2, 3, 3])      → [1, 2, 3]
    """

    # PASSO 1: Concatenar as duas listas em uma lista temporária
    # O operador + para listas cria uma NOVA lista com os elementos de ambas
    # As listas originais não são modificadas
    lista_combinada = lista_a + lista_b

    # PASSO 2: Remover duplicatas da lista combinada
    # Reutilizamos a função remover_duplicatas() que já implementamos
    # Isso demonstra o poder da composição de funções
    resultado = remover_duplicatas(lista_combinada)

    # PASSO 3: Retornar a lista mesclada sem duplicatas
    return resultado


def rotacionar(lista, k):
    """
    Rotaciona os elementos da lista k posições para a direita.

    Rotacionar para a direita significa que os últimos k elementos
    vão para o início da lista e os demais se deslocam para a direita.

    Demonstra: fatiamento para dividir e recombinar lista,
               tratamento de k maior que o tamanho (módulo),
               imutabilidade da lista original.

    ENTRADA: lista — lista com qualquer número de elementos
             k     — número de posições para rotacionar (inteiro >= 0)
    SAÍDA: nova lista com os elementos rotacionados k posições à direita
           (a lista original não é modificada)

    Exemplos:
        rotacionar([1, 2, 3, 4, 5], 2)   → [4, 5, 1, 2, 3]
        rotacionar([1, 2, 3, 4, 5], 5)   → [1, 2, 3, 4, 5]  (volta ao início)
        rotacionar([1, 2, 3, 4, 5], 7)   → [4, 5, 1, 2, 3]  (7 % 5 = 2)
        rotacionar([1, 2, 3], 0)          → [1, 2, 3]
        rotacionar([], 3)                  → []
        rotacionar([42], 100)              → [42]
    """

    # PASSO 1: Tratar casos especiais
    # Se a lista está vazia ou tem um único elemento, não há nada a rotacionar
    if len(lista) <= 1:
        return lista[:]  # Retornamos uma cópia para manter consistência

    # PASSO 2: Calcular o deslocamento efetivo usando módulo
    # Se k >= len(lista), rotacionar k vezes é equivalente a rotacionar k % len(lista) vezes
    # Exemplo: rotacionar [1,2,3,4,5] por 5 posições volta ao estado original
    # Exemplo: rotacionar por 7 é igual a rotacionar por 7 % 5 = 2
    tamanho = len(lista)
    k_efetivo = k % tamanho

    # PASSO 3: Tratar o caso onde k_efetivo é zero (sem rotação)
    if k_efetivo == 0:
        return lista[:]  # Retornamos uma cópia sem modificação

    # PASSO 4: Dividir a lista em duas partes usando fatiamento
    # Para rotação à direita de k posições:
    # - Os últimos k elementos vão para o início
    # - Os primeiros (n-k) elementos vão para o final
    #
    # Exemplo: [1, 2, 3, 4, 5] com k=2
    # ponto_de_corte = 5 - 2 = 3
    # parte_final  = lista[3:]  → [4, 5]  (os últimos 2 elementos)
    # parte_inicio = lista[:3]  → [1, 2, 3]  (os primeiros 3 elementos)
    ponto_de_corte = tamanho - k_efetivo
    parte_final = lista[ponto_de_corte:]   # Últimos k elementos
    parte_inicio = lista[:ponto_de_corte]  # Primeiros (n-k) elementos

    # PASSO 5: Recombinar as partes na nova ordem
    # Os últimos k elementos vêm primeiro, seguidos pelos primeiros (n-k)
    resultado = parte_final + parte_inicio

    # PASSO 6: Retornar a lista rotacionada
    # A lista original não foi modificada
    return resultado

def achatar_lista(lista_aninhada):
    """
    Converte uma lista de listas em uma única lista plana.

    ENTRADA: lista_aninhada — lista onde cada elemento é uma lista
    SAÍDA: lista plana com todos os elementos em ordem
    """

    # Inicializar a lista plana de resultado
    resultado = []

    # Percorrer cada sublista da lista aninhada
    for sublista in lista_aninhada:
        # Percorrer cada elemento da sublista atual
        for elemento in sublista:
            # Adicionar o elemento à lista plana de resultado
            resultado.append(elemento)

    return resultado


def estatisticas_lista(lista_aninhada):
    """
    Calcula estatísticas de uma lista de listas.

    ENTRADA: lista_aninhada — lista onde cada elemento é uma lista de números
    SAÍDA: dicionário com soma, minimo, maximo e quantidade
    """

    # PASSO 1: Achatar a lista aninhada em uma lista plana
    plana = achatar_lista(lista_aninhada)

    # PASSO 2: Verificar se há elementos para calcular
    if not plana:
        return {"soma": 0, "minimo": None, "maximo": None, "quantidade": 0}

    # PASSO 3: Calcular as estatísticas manualmente
    soma = 0
    minimo = plana[0]
    maximo = plana[0]

    for numero in plana:
        soma += numero
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    # PASSO 4: Retornar o dicionário com as estatísticas
    return {
        "soma": soma,
        "minimo": minimo,
        "maximo": maximo,
        "quantidade": len(plana)
    }
