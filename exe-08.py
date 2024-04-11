destV = input("Qual o destino da sua viagem: ")
distan = float(input("Qual a distância a ser percorrida na viagem km: "))
kmLitro = float(input("Quantos km por litro faz seu carro: "))
precGas = float(input("Qual o preço por L da Gasolina R$: ")) 

custo = (distan / kmLitro) * precGas

print("você vai para", destV)
print(f"O custo da viagem foi de: R${custo:.2f} ")