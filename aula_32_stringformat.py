a = 'AAAAAAA'
b = 'BBBBBBB'
c = 1.1
#os números nas chaves indicam a posição do parâmetro no string.format
string = 'b = {1} a = {0} a = {0} a = {0} c = {2:.2f}'
formato = string.format(a, b, c);
print(formato)

#parâmetros nomeados
string = 'b = {nome2} a = {nome1} a = {nome1} a = {nome1} c = {nome3:.2f}'
formato = string.format(nome1 = a, nome2 = b, nome3 = c)
print(formato)
