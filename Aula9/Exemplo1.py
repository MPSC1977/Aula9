import os

os.system('cls')

try:
    n = int(input('Digite um número: '))
except:
    print('Erro')


try:
    n = input('Digite uma letra: ')
except (ValueError, KeyboardInterrupt, IndexError) as e:
    print(f'Erro: {e}')
else:
    print(f'Você informou {n}')

try:
    txt = input('Informe o nome: ')[0]
except IndexError as e:
    print(f'{e} Precisa digitar algo')
else:
    print('Acertou!')
finally:
    print('Sempre executado')