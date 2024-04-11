nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade<=2):
    print(nome,"tem",idade,"ano de idade, e pela tabela é considerado um BEBÊ")
elif(idade>= 3 and idade<=11):
    print(nome,"tem",idade,"anos de idade, e pela tabela é considerado uma  CRIANÇA")
elif(idade>= 12 and idade<=21):
    print(nome,"tem",idade,"anos de idade, e pela tabela é considerado um  JOVEM")    
elif(idade>= 22 and idade<=64):
    print(nome,"tem",idade,"anos de idade, e pela tabela é considerado um  ADULTO")
elif(idade>= 65 and idade<=100):
    print(nome,"tem",idade,"anos de idade, e pela tabela é considerado um  IDOSO")
else:
    print(nome,"tem",idade,"anos de idade, e pela tabela é considerado um  MUITO VELHINHO")  