import random

def modulo_do_jogo():
    number_to_be_found = random.randrange(0,15,1)
    loop = 1
    primeira_tentativa = int(input('chute um número entre 0 e 15: '))
    tentativas_restantes = 3
    while loop < 2:
        if (primeira_tentativa == number_to_be_found):
            print('voce acertou! ')
            print('sobraram: ', tentativas_restantes, " tentativas_restantes")
            break
        else:
            if tentativas_restantes == 0:
                    jogar_novamente = input('deseja jogar novamente?(s/n) ')
                    if jogar_novamente == 's':
                        deseja_jogar = 's'
                    elif jogar_novamente == 'n':
                        return
                    else:
                        print('digite s ou n: ')
            hint = int(number_to_be_found - primeira_tentativa)
            tentativas_restantes -= 1
            print('voce possui ', tentativas_restantes, " tentativas")
            print('a diferenca entre seu chute e a resposta e: ', hint)
            primeira_tentativa = int(input('tente novamente: '))


def guessingNumber():
    deseja_jogar = input('deseja jogar?(s/n)')
    while deseja_jogar == 's':
            modulo_do_jogo()
        






if __name__ == '__main__':
    guessingNumber()