class TabelaSimbolos:
    """
    Gerenciador de Tabela de Simbolos com escopos aninhados.

    Estrutura utilizada:
    - Uma pilha de escopos.
    - Cada escopo e uma Hash Table, representada por um dicionario Python.
    - O topo da pilha representa o escopo atual.
    """

    def __init__(self):
        self.escopos = [{}]

    def entrar_escopo(self):
        self.escopos.append({})
        print(f"[OK] Novo escopo criado. Nivel atual: {self.nivel_atual()}")

    def sair_escopo(self):
        if len(self.escopos) == 1:
            print("[ERRO] Nao e permitido remover o escopo global.")
            return False

        nivel = self.nivel_atual()
        self.escopos.pop()
        print(f"[OK] Escopo de nivel {nivel} removido. Nivel atual: {self.nivel_atual()}")
        return True

    def declarar(self, variavel, tipo):
        escopo_atual = self.escopos[-1]

        if variavel in escopo_atual:
            print(f"[ERRO] Variavel '{variavel}' ja declarada neste escopo.")
            return False

        escopo_atual[variavel] = {
            "tipo": tipo,
            "nivel": self.nivel_atual()
        }
        print(f"[OK] Variavel '{variavel}' declarada como '{tipo}' no escopo {self.nivel_atual()}.")
        return True

    def buscar(self, variavel):
        for indice in range(len(self.escopos) - 1, -1, -1):
            escopo = self.escopos[indice]
            if variavel in escopo:
                simbolo = escopo[variavel]
                print(
                    f"[OK] Variavel '{variavel}' encontrada no escopo {indice}. "
                    f"Tipo: {simbolo['tipo']}"
                )
                return simbolo

        print(f"[ERRO] Variavel '{variavel}' nao foi declarada em nenhum escopo acessivel.")
        return None

    def nivel_atual(self):
        return len(self.escopos) - 1

    def mostrar(self):
        print("\n=== ESTADO ATUAL DA TABELA DE SIMBOLOS ===")
        for indice, escopo in enumerate(self.escopos):
            nome = "GLOBAL" if indice == 0 else f"ESCOPO {indice}"
            print(f"{nome}: {escopo}")
        print("==========================================\n")
