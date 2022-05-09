"""
Tipos de dados
str - textos
int- inteiro (1234 ou 0 ou -1 -2)
float- real/ponto flutuante com decimail
bool- lógico - true /false
"""
print("Luiz", type("Luiz"))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
#Type casting
print("Luiz", type("Luiz"), bool("Luiz"))
print('10', type("10"), type(int("10")))

#exercicio
print("gerson", type("gerson"))
print("45", type(45))
print("minha altura é: 1,71", type(float(1.71)))
print("maior de idade:45", type(45), (45 > 18))