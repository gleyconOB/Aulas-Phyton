litrosVend = float(input("Quantos Litros de combustivel vendidos: "))
tipoComb = (input("tipo do combustivel G-gasolina, A- alcool: "))

precoGa= 2.50
precoAl=1.90


if tipoComb =="a":
    
    if litrosVend <= 20:
        desconA = (litrosVend *precoAl)*0.03
        valorPagoT = (precoAl * litrosVend) - desconA
    else:
        desconA = (litrosVend *precoAl)*0.05
        valorPagoT = (precoAl * litrosVend) - desconA

elif tipoComb =="g": 
    
    if litrosVend <= 20:
        desconG = (litrosVend * precoGa)*0.04
        valorPagoT = (precoGa * litrosVend) - desconG
    else:
        desconG = (litrosVend * precoGa)*0.06
        valorPagoT = (precoGa * litrosVend) - desconG


print("O valor pago pelo cliente R$: ",valorPagoT)
