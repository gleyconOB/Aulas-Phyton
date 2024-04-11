pesoP = float(input("Quantos KG de peixe foram pescados: "))

valorMulta = 4
pesoExc = pesoP - 50

if pesoP > 50:
    excMulta = pesoExc * valorMulta
    print("Você pescou: ",pesoP,"KG de peixe")
    print("o KG excedente é: ",pesoExc,"KG de peixe")
    print("O peso de peixe pescado excedeu o limite permitido")
    print("Sua multa é de R$:",excMulta)

elif pesoP <= 50:
    print("Você pescou: ",pesoP,"KG de peixe")
    print("O peso de peixe pescado não excedeu o limite permitido - NÃO TEVE MULTA")    