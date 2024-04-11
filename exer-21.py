salarioF= float(input("Digite o salário do funcionario: R$"))
quantiaV= float(input("Digite o valor das vendas: R$"))

comissV= (quantiaV *4)/100
salarioFinal= salarioF + comissV

print("A Comissão foi de: R$", comissV)
print("O salário final foi de: R$", salarioFinal)