import datetime 

nome = 'João'
sobrenome = 'da Silva'
ano_nascimento = 1972
idade = datetime.datetime.now().year - ano_nascimento
maior_de_idade = idade >= 18
altura_metros = 1.79

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade? ', 'Sim' if maior_de_idade else 'Não')
print('Altura em metros: ', altura_metros)
