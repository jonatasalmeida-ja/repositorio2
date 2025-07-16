def impar_par(num):
    if num % 2 == 0:
        print(f'O Número {num} é par')
    else:
        print(f'O Número {num} é impar')

num = int(input('Digite um número: '))

impar_par(num)