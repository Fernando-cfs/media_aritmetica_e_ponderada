entrada = input("Media aritmetica digite: 'a' Media ponderada digite: 'p': ")

if entrada == 'a':
    valor_1 = input('Digite o primeiro valor_1: ')
    valor_2 = input('Digite o primeiro valor_2: ')
    valor_3 = input('Digite o primeiro valor_3: ')

    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    valor_3 = int(valor_3)
    media_aritmetica =   (valor_1 + valor_2 + valor_3)  / 3

    print(f'A media aretmedica é: {media_aritmetica:.2f} ')
elif entrada == 'p':

    valor_1 = input('Digite o primeiro valor1: ')
    valor_2 = input('Digite o primeiro valor2: ')
    valor_3 = input('Digite o primeiro valor3: ')

    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    valor_3 = int(valor_3)
    media_ponderada =   (valor_1 * 3 + valor_2 * 3 + valor_3 * 5)  / 3

    print(f'A media ponderada é: {media_ponderada:.2f} ')

else:
    print('Comando invalido')