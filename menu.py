from container import avaliar

# Função para limpar a tela do terminal
def limpar_tela():
    print("\033c", end="")

# Função do cabeçalho do menu
def cabecalho():
    print("\033[1m" + "*" * 30)
    print("         Calculadora")
    print("*" * 30 + "\033[0m")

# Função das opções do menu
def opcoes():
    print("\nEscolha uma opção:")
    print("\033[34m1. Calcular\033[0m")
    print("\033[34m2. Exemplo\033[0m")
    print("\033[34m3. Sair\033[0m")

# Função para calcular
def calcular():
    limpar_tela()
    cabecalho()
    cal = input("\nDigite a expressão matemática: ")
    try:
        result = avaliar(cal)
        print("\n\033[32mResultado:\033[0m", result)
    except Exception as e:
        print("\n\033[31mErro ao calcular a expressão:\033[0m", e)
    input("\nPressione Enter para continuar...")
    limpar_tela()
    menu()

# Função de um exemplo
def exemplo():
    limpar_tela()
    cabecalho()
    cal = "25 - (2 + 6 / 3) * 5 - 1"
    print("\nExemplo de expressão:", cal)
    try:
        result = avaliar(cal)
        print("\n\033[32mResultado do exemplo:\033[0m", result)
    except Exception as e:
        print("\n\033[31mErro ao calcular o exemplo:\033[0m", e)
    input("\nPressione Enter para continuar...")
    limpar_tela()
    menu()

# Função para sair
def sair():
    limpar_tela()
    print("\033[32mEncerrando o programa...\033[0m")
    exit()

# Função principal
def menu():
    limpar_tela()
    cabecalho()
    opcoes()
    opc = input("\nDigite a opção desejada: ")

    if opc == '1':
        calcular()
    elif opc == '2':
        exemplo()
    elif opc == '3':
        sair()
    else:
        print("\n\033[31mOpção inválida!\033[0m")
        input("\nPressione Enter para continuar...")
        menu()

# Iniciar o programa
menu()
