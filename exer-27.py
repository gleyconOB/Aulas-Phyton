alunaF170= 0
alunoM= 0
alunoMBom= 0
for contAlu in range(50):
    matricula = input("Matrícula do aluno:")
    sexo = input("Digite 'F' para feminino ou 'M' para masculino: ")
    altura = float(input("Altura do aluno em (cm): "))
    fisicoAlu=int(input("status físico (1–bom, 2–regular, 3–ruim)"))

    if (sexo.upper() == 'F' and altura > 170):
        alunaF170 += 1
    elif (sexo.upper() == 'M'):
        alunoM += 1
        if (fisicoAlu == 1):
            alunoMBom += 1

porcAluno=(alunoMBom / alunoM )* 100

print("A quantidade de alunas do sexo feminino com altura maior que 170cm: ",alunaF170)
print("A porcentagem de alunos do sexo masculino com o status físico bom é de:",porcAluno,"%")