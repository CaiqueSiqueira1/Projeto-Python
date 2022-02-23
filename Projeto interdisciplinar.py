print('''------- Conversão para decimal para as bases binário, hexadecimal -------
''')


opc = 0

while opc != '3' :
        print(''' Escolha uma das bases para conversão :
[1] Binario
[2] Hexadecimal
[3] Encerrar programa
''')
        num = int(input('Digite um numero inteiro: '))
        opc= int(input('Digite a opçao desejada: '))
        if opc == 1:
            print('O numero {} Convertido para BINARIO é igual a {}' .format(num, bin(num)[2:]))
        if opc == 2:
            print('O numero {} Convertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
        elif opc == 3:
                break
