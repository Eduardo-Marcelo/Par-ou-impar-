num = 1
contagem = 1

print('Aviso: Caro usuário, você poderá verificar até 3 números, caso queira verificar mais alguns deverá rodar o código novamente')

while num != 0 and contagem <= 3:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')    
    contagem = contagem + 1    