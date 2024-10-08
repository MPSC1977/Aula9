import os

os.system('cls')

try:
    n = int(input('Digite um número: '))
except:
    print('Erro')


try:
    n = int(input('Digite um número: '))
except ValueError as e:
    print(f'{e}')
except KeyboardInterrupt:
    print(f'\nO usuário cancelou a operação...')
