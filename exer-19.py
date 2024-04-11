lado1 = float(input("Lado 1 do triângulo:"))
lado2 = float(input("Lado 2 do triângulo:"))
lado3 = float(input("Lado 3 do triângulo:"))

if (lado1 == lado2 == lado3):
    print("Este triângulo tem 3 lados iguais: ele é um triângulo equilátero")
else:
    igual = lado1   

    if(lado2 == igual):
        print("Este triângulo tem 2 lados iguais: ele é um triângulo isósceles")
    elif(lado3 == igual or lado3 == lado2):
        print("Este triângulo tem 2 lados iguais: ele é um triângulo isósceles")
    else:
        print("Este triângulo tem 3 lados diferentes: ele é um triângulo escaleno")    