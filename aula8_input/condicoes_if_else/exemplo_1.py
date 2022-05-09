"""
Operadores relacionais
== > >= < <= !=
"""
print(2 == 2)  # dois iguais soa como uma pergunta
print(2 == 1)
print(2 =='2')

#num_1 = 2
#num_2 = 2
#expressao= (num_1 == num_2)
#print(expressao)
#expressao= (num_1 <= num_2)
#print(expressao)
#expressao=(num_1 != num_2)
#print(expressao)

nome = input('Qual seu nome?: ')
idade = input('Qual a sua idade?: ')
idade_lim =18
idade =int(idade)

idade_menor = 20
idade_maior = 19
if idade >= idade_lim:
    print(f' {nome}pode pegar o emprestimo. ')
else:
    print (f'{nome} Nao pode pegar o emprestimo.')

if idade >= idade_menor and idade <= idade_maior:
    print(f' {nome}pode pegar o emprestimo. ')
else:
    print (f'{nome} Nao pode pegar o emprestimo.')