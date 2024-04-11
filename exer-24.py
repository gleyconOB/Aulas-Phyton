quantS=int(input("Quantidade de sanduíches a serem produzidas: "))



Q = 50*2
P = 50
H = 100
sanduiche = Q + P + H
kgQ = (quantS * Q)/1000
kgP = (quantS * P)/1000
kgH= (quantS * H)/1000
KgSandu = (quantS * sanduiche) /1000

print("Você vai produzir: ",quantS,"sanduíches")
print("Você vai precisar de: ",kgQ,"KG de queijo")
print("Você vai precisar de: ",kgP,"KG de Presunto")
print("Você vai precisar de: ",kgH,"KG de hamburguer")
print("Total de KG necessário:",KgSandu,"KG")