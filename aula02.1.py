#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input("Qual o nome do aluno? \n")
nota = float(input("Qual é a nota do {}? \n".format(nome)))

if nota == 10:
  print("{} você é bichão, mesmo...".format(nome))
elif nota >= 6 and nota < 10:
  print("{} você esta na media")
else:
  print(Burro)