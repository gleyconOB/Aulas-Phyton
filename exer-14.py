numeroC = int(input("Digite o numero da sua conta: "))
saldo = float(input("Digite seu saldo: R$"))
debitos= float(input("Digite o saldo devedor: R$"))
credito =float(input("Digite seu crédito: R$"))

saldoA= (saldo - debitos)+ credito

if(saldoA >=0):
    print("Saldo positivo")
else:
    print("Saldo negativo")    