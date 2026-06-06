from tabela_simbolos import TabelaSimbolos


def executar_teste_automatico():
    print("=== GERENCIADOR DE TABELA DE SIMBOLOS ===")
    print("Simulacao de escopos aninhados usados na analise semantica.\n")

    tabela = TabelaSimbolos()

    print("--- Teste 1: declaracoes no escopo global ---")
    tabela.declarar("x", "int")
    tabela.declarar("nome", "string")
    tabela.buscar("x")
    tabela.mostrar()

    print("--- Teste 2: entrada em novo escopo ---")
    tabela.entrar_escopo()
    tabela.declarar("y", "float")
    tabela.buscar("y")
    tabela.buscar("nome")
    tabela.mostrar()

    print("--- Teste 3: sombreamento de variavel ---")
    tabela.declarar("x", "float")
    tabela.buscar("x")
    tabela.mostrar()

    print("--- Teste 4: erro de redeclaracao no mesmo escopo ---")
    tabela.declarar("x", "boolean")
    tabela.mostrar()

    print("--- Teste 5: saida de escopo e busca ---")
    tabela.sair_escopo()
    tabela.buscar("x")
    tabela.buscar("y")
    tabela.mostrar()

    print("--- Teste 6: tentativa de remover escopo global ---")
    tabela.sair_escopo()


def executar_menu():
    tabela = TabelaSimbolos()

    while True:
        print("\n=== MENU - TABELA DE SIMBOLOS ===")
        print("1 - Declarar variavel")
        print("2 - Buscar variavel")
        print("3 - Entrar em novo escopo")
        print("4 - Sair do escopo atual")
        print("5 - Mostrar tabela")
        print("0 - Encerrar")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            variavel = input("Nome da variavel: ").strip()
            tipo = input("Tipo da variavel: ").strip()
            tabela.declarar(variavel, tipo)
        elif opcao == "2":
            variavel = input("Nome da variavel: ").strip()
            tabela.buscar(variavel)
        elif opcao == "3":
            tabela.entrar_escopo()
        elif opcao == "4":
            tabela.sair_escopo()
        elif opcao == "5":
            tabela.mostrar()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("[ERRO] Opcao invalida.")


if __name__ == "__main__":
    print("Escolha o modo de execucao:")
    print("1 - Executar testes automaticos")
    print("2 - Usar menu interativo")
    modo = input("Opcao: ").strip()

    if modo == "2":
        executar_menu()
    else:
        executar_teste_automatico()
