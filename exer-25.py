camisaP = int(input("Quantia de camisetas 'P' compradas: "))
camisaM = int(input("Quantia de camisetas 'M' compradas: "))
camisaG = int(input("Quantia de camisetas 'G' compradas: "))

precoP= camisaP*10.00
precoM= camisaM*12.00
precoG= camisaG*15.0

valorTC = precoP+precoM+precoG

print("Total da compra é de R$: ",valorTC,"em peças de camisetas 'P','M' e 'G'")