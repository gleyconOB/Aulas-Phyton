nome = input("digite seu nome: ")
disciplina = (input("Qual sua disciplina: "))
nota1 = float(input("digite a nota da prova 1: "))
nota2 = float(input("digite a nota da prova 2: "))
nota3 = float(input("digite a nota da prova 3: "))

media = (nota1+nota2+nota3) / 3

print("o aluno: ",nome, "cursa", disciplina)
print("Sua nota na 1 prova: ",nota1)
print("Sua nota na 2 prova: ",nota2)
print("Sua nota na 3 prova: ",nota3)
print("A média final do aluno: ",nome, "é",media)

if(media >= 6):
    print("O aluno",nome,"foi APROVADO!!!")
else:
    print("o aluno ",nome,"Foi REPROVADO!!!")    
