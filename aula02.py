# comando input()
nome = input("Digite seu nome: ")

print(f"Boa noite, seu nome é {nome}")

idade = int(input("Digite sua idade: "))
print(f"Sua idade é {idade}")

dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

# Estrutura condicional - SE (if)

if idade >= 18:
  print("Você é maior de idade, já pode beber ou dirigir")
else:
  print("Você é menor de idade!")


genero = input("Qual é o seu genero? M = masculino, F = feminino e 0 = outros: ")

if idade >= 18 and genero == 'M':
  print("e você também precisa/precisou prestar o serviço militar obrigatório")