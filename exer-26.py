valorAd = float(input("Valor da roupa usada comprada: R$"))
valor45= (valorAd * 45)/100
valor30=(valorAd * 30)/100
if(valorAd <=50):
    valorvend = valorAd + valor45
    print("o valor de venda desse produto é de R$:",valorvend)
else:
    valorvend = valorAd + valor30
    print("o valor de venda desse produto é de R$:",valorvend)   