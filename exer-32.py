valoS= int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))

if valoS < 10 or valoS > 600:
    print("Valor inválido. O valor do saque deve estar entre 10 e 600 reais.")
else:
    notas = [100, 50, 10, 5, 1]  

    for nota in notas:
        quantN = valoS // nota
        valoS %= nota

        
        if quantN > 0:
            print(quantN, "notas de", nota, "reais")    
