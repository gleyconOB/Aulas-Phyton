numero1= float(input("Digite o primeiro numero: "))
numero2= float(input("Digite o segundo numero: "))
operacao = input("Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    print("Operação inválida")

if resultado % 2 == 0:
    parImp = "par"
else:
    parImp = "ímpar"

if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"  

if resultado % 1 == 0:
    tipoNum = "inteiro"
else:
    tipoNum = "decimal"      

print("O resultado da operação é:", resultado)
print("O resultado é", parImp)
print("O resultado é", sinal)
print("O resultado é", tipoNum)