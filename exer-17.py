salarioAnt = float(input("Digite o salário do colaborador: "))

if(salarioAnt <=280):
    percentual = 20
    valorAUM = (salarioAnt * percentual)/100
elif(salarioAnt >=280 and salarioAnt <=700):
    percentual = 15
    valorAUM = (salarioAnt * percentual)/100    
elif(salarioAnt >=700 and salarioAnt <=1500):
    percentual = 10
    valorAUM = (salarioAnt * percentual)/100
else:
    percentual = 5
    valorAUM =(salarioAnt*percentual)/100

novoSalario=salarioAnt + valorAUM    

print("O seu salário antes:R$ ",salarioAnt)
print("O percentual de aumento aplicado:", percentual,"%")
print("Valor do aumento:R$ ",valorAUM)
print("O Novo salário:R$ ",novoSalario)