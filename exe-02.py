nome = input("digite seu nome: ")
nota1 = float(input("digite a nota do seu primeiro bimestre: "))
nota2 = float(input("digite a nota do seu segundo bimestre: "))
nota3 = float(input("digite a nota do seu terceiro bimestre: "))
nota4 = float(input("digite a nota do seu quarto bimestre: "))

media = (nota1+nota2+nota3+nota4) / 4

print("o aluno: ",nome, "tem essas notas bismestrais")
print("Sua nota do 1° Bimestre: ",nota1)
print("Sua nota do 2° Bimestre: ",nota2)
print("Sua nota do 3° Bimestre: ",nota3)
print("Sua nota do 4° Bimestre: ",nota4)
print("A média final do aluno: ",nome, "é",media)

if(media >= 7):
    print("O aluno",nome,"foi APROVADO!!!")
else:
    print("o aluno ",nome,"Foi REPROVADO!!!")    
