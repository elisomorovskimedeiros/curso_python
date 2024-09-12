# comentários em python são com #
"""
DocString
É algo que é lido pelo interpretador, porém pode ser
utilizado como comentário multilinhas
"""

#/r/n -> CRLF fim de linha utilizado no windows
#/n -> LF fim de linha utilizado no linux ou mac
print(12, 34) #imprime algo no terminal
print(56, 78) #imprime algo no terminal
print(56, 78, sep="-") #configura o separador entre argumentos
print(56, 78, sep='-') #pode ser usado com aspas simples ou duplas

print(12, 34, 1011, sep='-', end='##') #não irá quebrar a linha e irá exibir as cerquilhas
print(310, 1112, sep='-', end='\r\n') #quebra padrão CRLF
print(56, 78, sep='-', end='\n') #quebra padrão LF

#imprimindo texto:
print('Eli')
#ou
print("Eli")
#tanto faz
#para imprimir aspas dentro da string utilize um caractere de escape
print("\"Eli\"")
#se quizer mostrar o escape utilie r antes da string:
print(r"\"Eli\"")
#ou coloque aspas duplas dentro aspas simples
print('"Eli"')
print('Explícito', 'é','melhor-que-implícito.',sep='-')


print(123)#número inteiro
print(1.1)#float

#exibir o tipo de dado:
print(type('Eli'))# => <class 'str'>
print(type(-123))# => <class 'int'>
print(type(123.1))# => <class 'float'>
print(type(True))# => <class 'bool'>

#concatenar string
print('a' + 'b')

#typecasting do tipo de dado
print(int('1') + 1)

print(bool(10 == 10))




