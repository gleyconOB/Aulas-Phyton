precoPr = float(input("Digite o preço do produto: R$"))
descont = (precoPr * 10)/100
novoP = precoPr - descont

print("Preço do produto:R$ ", precoPr)
print("Desconto de (10%): R$",descont)
print("O preço novo do produto é de: R$",novoP)