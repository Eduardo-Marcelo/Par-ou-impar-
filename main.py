num = 1
contagem = 1


while num != 0 and contagem <= 3:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')    
    contagem = contagem + 1    