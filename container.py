from pilha import Pilhas

def avaliar(calculo):
    operandos = Pilhas()
    operadores = Pilhas()

    tamanho = 0
    while tamanho < len(calculo):
        number = calculo[tamanho]
        if number.isdigit():
            num, tamanho = extrair_numero(calculo, tamanho)
            operandos.empilhar(num)
        elif number in '+-*/':
            resolver_operadores(operandos, operadores, number) # Avalia todo o calculo e ja resolve ele
            operadores.empilhar(number)
            tamanho += 1
        elif number == '(':
            operadores.empilhar(number)
            tamanho += 1
        elif number == ')':
            resolver_parenteses(operandos, operadores)
            tamanho += 1
        else:
            tamanho += 1
    
    resolver_restantes(operandos, operadores)

    return operandos.desempilhar()

def extrair_numero(calculo, tamanho):
    num = ""
    while tamanho < len(calculo) and (calculo[tamanho].isdigit() or calculo[tamanho] == '.'): # verifica se é um numero inteiro ou decimal
        num += calculo[tamanho]
        tamanho += 1
    return float(num), tamanho

def resolver_operadores(operandos, operadores, number):
    while not operadores.vazia() and prioridade(operadores.topo()) >= prioridade(number): # verifica a prioridade dos operadores e ja calcula 
        operador = operadores.desempilhar()
        op2 = operandos.desempilhar()
        op1 = operandos.desempilhar()
        operandos.empilhar(calcular(op1, op2, operador))

def resolver_parenteses(operandos, operadores): 
    while operadores.topo() != '(':
        operador = operadores.desempilhar()
        if operador is None:
            raise ValueError("Parênteses desbalanceados") # Resolve a questao dos parenteses e verifica se nao tem nem um parentes a mais.
        op2 = operandos.desempilhar()
        op1 = operandos.desempilhar()
        operandos.empilhar(calcular(op1, op2, operador))
    operadores.desempilhar()

def resolver_restantes(operandos, operadores):
    while not operadores.vazia():
        operador = operadores.desempilhar()
        if operador is None:
            raise ValueError("Parênteses desbalanceados")  # Resolve o restante do calculo 
        op2 = operandos.desempilhar()
        op1 = operandos.desempilhar()
        operandos.empilhar(calcular(op1, op2, operador))

def prioridade(op):
    ordem = {'+': 1, '-': 1, '*': 2, '/': 2} # Nome ja diz verifica a prioridade 
    return ordem.get(op, 0)

def calcular(op1, op2, operador):  # Nome ja diz, calcula os valores
    if operador == '+':
        return op1 + op2
    elif operador == '-':
        return op1 - op2
    elif operador == '*':
        return op1 * op2
    elif operador == '/':
        if op2 == 0:
            raise ZeroDivisionError("Divisão por zero")
        return op1 / op2
