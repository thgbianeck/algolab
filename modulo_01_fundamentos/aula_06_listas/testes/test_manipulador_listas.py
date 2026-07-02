# test_manipulador_listas.py
# Testes automatizados para a Aula 06: Listas em Python
# Execute com: pytest testes/ -v
#
# Filosofia dos testes:
# - Casos normais: entradas típicas com resultado esperado claro
# - Casos extremos: lista vazia, lista com um elemento
# - Imutabilidade: verificar que a lista original nunca é modificada
# - Casos de borda: duplicatas consecutivas, k maior que o tamanho

import pytest

# Importamos as quatro funções que vamos testar
from codigo_06.manipulador_listas import (
    inverter_lista,
    remover_duplicatas,
    mesclar_listas,
    rotacionar,
    achatar_lista,
    estatisticas_lista,
)


# ============================================================
# TESTES PARA inverter_lista()
# ============================================================

class TestInverterlista:
    """
    Testa todos os comportamentos da função inverter_lista.
    Verifica: inversão correta, lista vazia, um elemento, imutabilidade.
    """

    def test_inverter_lista_simples(self):
        """Caso normal: inverter lista com cinco elementos."""
        assert inverter_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_inverter_lista_dois_elementos(self):
        """Caso mínimo com troca: dois elementos trocam de posição."""
        assert inverter_lista([1, 2]) == [2, 1]

    def test_inverter_lista_um_elemento(self):
        """Caso extremo: lista com um único elemento não muda."""
        assert inverter_lista([42]) == [42]

    def test_inverter_lista_vazia(self):
        """Caso extremo: lista vazia invertida é lista vazia."""
        assert inverter_lista([]) == []

    def test_inverter_lista_com_repetidos(self):
        """Caso com elementos repetidos — inversão ainda funciona."""
        assert inverter_lista([1, 1, 2, 2, 3]) == [3, 2, 2, 1, 1]

    def test_inverter_lista_com_strings(self):
        """Listas de strings também devem ser invertidas corretamente."""
        assert inverter_lista(["a", "b", "c"]) == ["c", "b", "a"]

    def test_inverter_lista_par_de_elementos(self):
        """Lista com número par de elementos."""
        assert inverter_lista([1, 2, 3, 4]) == [4, 3, 2, 1]

    def test_inverter_nao_modifica_original(self):
        """A lista original NÃO deve ser modificada pela função."""
        original = [1, 2, 3, 4, 5]
        copia_antes = original.copy()
        inverter_lista(original)
        # A lista original deve ser idêntica à cópia feita antes da chamada
        assert original == copia_antes

    def test_retorna_nova_lista(self):
        """A função deve retornar uma nova lista, não a mesma referência."""
        original = [1, 2, 3]
        resultado = inverter_lista(original)
        # Verificar que são objetos diferentes na memória
        assert resultado is not original

    def test_inverter_duas_vezes_retorna_original(self):
        """Inverter duas vezes deve retornar a lista na ordem original."""
        original = [1, 2, 3, 4, 5]
        assert inverter_lista(inverter_lista(original)) == original


# ============================================================
# TESTES PARA remover_duplicatas()
# ============================================================

class TestRemoverDuplicatas:
    """
    Testa todos os comportamentos da função remover_duplicatas.
    Verifica: remoção correta, preservação de ordem, casos extremos.
    """

    def test_remover_duplicatas_simples(self):
        """Caso normal: lista com algumas duplicatas."""
        assert remover_duplicatas([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

    def test_preserva_primeira_ocorrencia(self):
        """A primeira ocorrência de cada elemento deve ser preservada."""
        # O 3 aparece primeiro, depois o 1 — a ordem de primeira aparição é [3,1,2]
        resultado = remover_duplicatas([3, 1, 2, 1, 3])
        assert resultado == [3, 1, 2]

    def test_sem_duplicatas_retorna_igual(self):
        """Lista sem duplicatas deve retornar lista equivalente à original."""
        assert remover_duplicatas([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_todos_duplicados(self):
        """Lista com todos os elementos iguais deve retornar lista com um elemento."""
        assert remover_duplicatas([5, 5, 5, 5, 5]) == [5]

    def test_lista_vazia(self):
        """Lista vazia deve retornar lista vazia."""
        assert remover_duplicatas([]) == []

    def test_lista_um_elemento(self):
        """Lista com um elemento não tem duplicatas."""
        assert remover_duplicatas([7]) == [7]

    def test_duplicatas_consecutivas(self):
        """Duplicatas consecutivas devem ser removidas corretamente."""
        assert remover_duplicatas([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

    def test_duplicatas_intercaladas(self):
        """Duplicatas intercaladas devem ser removidas corretamente."""
        assert remover_duplicatas([1, 2, 1, 2, 1, 2]) == [1, 2]

    def test_com_strings(self):
        """Deve funcionar com listas de strings."""
        assert remover_duplicatas(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]

    def test_nao_modifica_original(self):
        """A lista original NÃO deve ser modificada."""
        original = [1, 2, 3, 2, 1]
        copia_antes = original.copy()
        remover_duplicatas(original)
        assert original == copia_antes

    def test_retorna_lista(self):
        """A função deve sempre retornar uma lista."""
        assert isinstance(remover_duplicatas([1, 2, 3]), list)


# ============================================================
# TESTES PARA mesclar_listas()
# ============================================================

class TestMesclarListas:
    """
    Testa todos os comportamentos da função mesclar_listas.
    Verifica: mesclagem correta, tratamento de duplicatas, listas vazias.
    """

    def test_mesclar_sem_elementos_comuns(self):
        """Caso normal: listas sem elementos em comum."""
        assert mesclar_listas([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_mesclar_com_elementos_comuns(self):
        """Caso normal: listas com alguns elementos em comum."""
        assert mesclar_listas([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_mesclar_listas_identicas(self):
        """Listas idênticas mescladas devem resultar em uma sem duplicatas."""
        assert mesclar_listas([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

    def test_mesclar_com_lista_vazia_a(self):
        """Mesclar lista vazia com lista não vazia."""
        assert mesclar_listas([], [1, 2, 3]) == [1, 2, 3]

    def test_mesclar_com_lista_vazia_b(self):
        """Mesclar lista não vazia com lista vazia."""
        assert mesclar_listas([1, 2, 3], []) == [1, 2, 3]

    def test_mesclar_duas_listas_vazias(self):
        """Mesclar duas listas vazias deve resultar em lista vazia."""
        assert mesclar_listas([], []) == []

    def test_mesclar_preserva_ordem_de_a(self):
        """Elementos de lista_a devem aparecer antes dos de lista_b."""
        resultado = mesclar_listas([3, 1], [2, 4])
        # 3 e 1 vêm de lista_a — devem aparecer primeiro
        assert resultado.index(3) < resultado.index(2)
        assert resultado.index(1) < resultado.index(4)

    def test_mesclar_com_duplicatas_internas(self):
        """Duplicatas dentro de cada lista também devem ser removidas."""
        assert mesclar_listas([1, 1, 2], [2, 3, 3]) == [1, 2, 3]

    def test_nao_modifica_lista_a(self):
        """A lista_a original NÃO deve ser modificada."""
        lista_a = [1, 2, 3]
        copia_antes = lista_a.copy()
        mesclar_listas(lista_a, [4, 5])
        assert lista_a == copia_antes

    def test_nao_modifica_lista_b(self):
        """A lista_b original NÃO deve ser modificada."""
        lista_b = [3, 4, 5]
        copia_antes = lista_b.copy()
        mesclar_listas([1, 2], lista_b)
        assert lista_b == copia_antes

    def test_retorna_lista(self):
        """A função deve sempre retornar uma lista."""
        assert isinstance(mesclar_listas([1], [2]), list)


# ============================================================
# TESTES PARA rotacionar()
# ============================================================

class TestRotacionar:
    """
    Testa todos os comportamentos da função rotacionar.
    Verifica: rotação correta, k=0, k igual ao tamanho, k maior que tamanho,
              lista vazia, lista com um elemento, imutabilidade.
    """

    def test_rotacionar_dois(self):
        """Caso normal: rotacionar 2 posições à direita."""
        # [1,2,3,4,5] com k=2 → os últimos 2 ([4,5]) vão para o início
        assert rotacionar([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_rotacionar_um(self):
        """Rotacionar 1 posição: apenas o último vai para o início."""
        assert rotacionar([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]

    def test_rotacionar_zero(self):
        """k=0: sem rotação, deve retornar cópia igual à original."""
        assert rotacionar([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

    def test_rotacionar_tamanho_completo(self):
        """k igual ao tamanho da lista: volta ao estado original."""
        assert rotacionar([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

    def test_rotacionar_maior_que_tamanho(self):
        """k maior que o tamanho: usa módulo para calcular k efetivo."""
        # k=7, tamanho=5: 7 % 5 = 2 → mesmo que rotacionar por 2
        assert rotacionar([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

    def test_rotacionar_multiplo_do_tamanho(self):
        """k múltiplo exato do tamanho: equivale a k=0."""
        assert rotacionar([1, 2, 3], 6) == [1, 2, 3]

    def test_rotacionar_lista_vazia(self):
        """Lista vazia rotacionada é lista vazia."""
        assert rotacionar([], 3) == []

    def test_rotacionar_um_elemento(self):
        """Lista com um elemento não muda independentemente de k."""
        assert rotacionar([42], 100) == [42]

    def test_rotacionar_dois_elementos(self):
        """Rotacionar dois elementos por 1 os troca de posição."""
        assert rotacionar([1, 2], 1) == [2, 1]

    def test_nao_modifica_original(self):
        """A lista original NÃO deve ser modificada."""
        original = [1, 2, 3, 4, 5]
        copia_antes = original.copy()
        rotacionar(original, 2)
        assert original == copia_antes

    def test_retorna_nova_lista(self):
        """A função deve retornar uma nova lista, não a mesma referência."""
        original = [1, 2, 3]
        resultado = rotacionar(original, 1)
        assert resultado is not original

    def test_rotacionar_com_strings(self):
        """Deve funcionar com listas de strings."""
        assert rotacionar(["a", "b", "c", "d"], 1) == ["d", "a", "b", "c"]

# ============================================================
# TESTES PARA achatar_lista
# ============================================================

class TestAchatarLista:
    
    def test_achatar_lista_simples(self):
        assert achatar_lista([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    def test_achatar_lista_vazia(self):
        assert achatar_lista([]) == []

    def test_achatar_sublista_vazia(self):
        assert achatar_lista([[], [1, 2], []]) == [1, 2]

    def test_estatisticas_basicas(self):
        resultado = estatisticas_lista([[1, 2], [3, 4], [5]])
        assert resultado["soma"] == 15
        assert resultado["minimo"] == 1
        assert resultado["maximo"] == 5
        assert resultado["quantidade"] == 5

    def test_estatisticas_lista_vazia(self):
        resultado = estatisticas_lista([])
        assert resultado["quantidade"] == 0
        assert resultado["minimo"] is None