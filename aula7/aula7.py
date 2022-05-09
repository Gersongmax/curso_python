nome = "Luiz"
print(nome, type(nome))
idade =45
altura =1.71
maioridade = idade > 18
peso = 72
imc = (peso/altura**2)
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print ("Maioridade:", maioridade)
data_1 = True  #variavel booleana explicita
print(nome, " tem ", idade, "e seu imc é de :", peso/(altura ** 2))
print(f"{nome} tem {idade} anos de idade e seu imc é:{peso/altura**2: .2f}")
print("{}tem {} de idade e seu imc é {:.2f}".format(nome, idade, imc))
print("{a}tem {b} de idade e seu imc é {c}".format(a=nome, b=idade, c=imc))
"""
Desafio
"""
nome = "Luiz"
print(nome, type(nome))
idade =45
altura =1.71
maioridade = idade > 18
peso = 72
imc = (peso/altura**2)
ano_atual =2022
print("desafio")
print("{a} tem {b} de idade e sua altura é:{c} e seu peso é de: {d}".format(a=nome, b=idade, c=altura, d=peso))
print("o imc de {} é de: {:.2f}".format(nome, imc))
print(f"Luiz nasceu em: {ano_atual - idade}")