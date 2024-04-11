altura=float(input("Qual sua altura: "))
sexo=input("Qual seu Sexo: M-masculino, F-feminino: ")

if sexo == "m":
    pesoI = (72.7*altura) - 58
    print("Seu sexo é masculino")
    print("Seu peso ideal é: ",pesoI,"KG")   
elif sexo == "f":
    pesoI = (62.1*altura)-44.7
    print("Seu sexo é feminino")
    print("Seu peso ideal é: ",pesoI,"KG")


