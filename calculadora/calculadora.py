saida = ''

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

while saida.lower() != 'n':
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação (+, -, *, / ou nome da operação): ')
        
        resultado = calculadora(numero1, numero2, operacao)
        print('Resultado da operação:', resultado)
        
        saida = input('Deseja continuar? (S/N): ')
    except ValueError:
        print('Erro: você precisa digitar números válidos.')
        saida = input('Deseja tentar novamente? (S/N): ')

print('Programa encerrado.')
