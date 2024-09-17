primeiro_valor = input('Digite um número qualquer:')
segundo_valor = input('Digite algum outro número:')

if(primeiro_valor == segundo_valor):
    print('Safadinho, você informou valores iguais, não vale.')
elif(primeiro_valor > segundo_valor):
    print(f'O {primeiro_valor=} valor é maior que o {segundo_valor=}.')
else:
    print(f'O {segundo_valor=} é maior que o {primeiro_valor=}.')