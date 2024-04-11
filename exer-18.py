valorH = float(input("Qual o valor da sua hora trabalhada: R$"))
quantH = int(input("Qauntidade de hora trabalhada no mês: "))

salarioBru = valorH * quantH

if(salarioBru <= 900):
    ir = 0
elif(salarioBru > 900 and salarioBru <= 1500):
    ir = 5    
elif(salarioBru > 1500 and salarioBru <= 2500):
    ir = 10  
else:
    ir = 20
inss= (salarioBru*10)/100
fgts=(salarioBru*11)/100
sindicato =(salarioBru*3)/100
descontoIR = (salarioBru * ir)/100
descontTotal= descontoIR + inss + sindicato
salarioLiqu = salarioBru - descontTotal

print("Salário Bruto: R$", salarioBru)
print("IR(%)",ir)
print("IR(R$)",descontoIR)
print("INSS(10%): R$",inss)
print("FGTS(11%): R$",fgts)
print("Sindicato(3%): R$",sindicato)
print("Total de descontos", descontTotal)
print("Salário Liquido: R$",salarioLiqu)