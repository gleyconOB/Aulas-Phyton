numero1 = int(input("Digite o 1° número: "))
numero2 = int(input("Digite o 2° número: "))
numero3 = int(input("Digite o 3° número: "))

if (numero1 == numero2 == numero3):
    print("Os três números são iguais:")
else:
    maior = numero1
    menor = numero1

    if(numero2> maior):
        maior = numero2
    elif(numero2<menor):
        menor= numero2
    if(numero3> maior):
        maior = numero3
    elif(numero3<menor):
        menor= numero3

    print("O maior número é:",maior) 
    print("O menor número é:",menor)             
