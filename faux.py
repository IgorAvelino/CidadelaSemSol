# Arquivo de funções auxiliares do sistema
import sys
from time import sleep    


############# CORES E LAYOUT #############


FCORES = {
    'Branco': '\033[0;0;0m',
    'Vermelho': '\033[31m',
    'verde': '\033[32m',
    'Amarelo': '\033[33m',
    'Azul': '\033[34m',
    'Roxo': '\033[35m',
    'Ciano': '\033[36m',
    'Preto': '\033[7;37m'
}


BCORES = {
    'Branco': '\033[0;0;0m',
    'Vermelho': '\033[41m',
    'verde': '\033[42m',
    'Amarelo': '\033[43m',
    'Azul': '\033[44m',
    'Roxo': '\033[45m',
    'Ciano': '\033[46m',
    'Cinza': '\033[47m'
}


LAYOUT = {
    'INF': f'{FCORES["Azul"]}[i]{FCORES["Branco"]}',
    'HIS': f'{FCORES["Roxo"]}[h]{FCORES["Branco"]}',
    'USU': f'{FCORES["Vermelho"]}[{FCORES["Branco"]}{FCORES["Amarelo"]}>>{FCORES["Vermelho"]}]{FCORES["Branco"]}',
    'SAVE': f'{FCORES["verde"]}[S]{FCORES["Branco"]}'
}


############# SISTEMA #############
def limpar_terminal():
    import os
    print('\n' * os.get_terminal_size().lines)
    

def efeito_digitar(capitulo: dict):    
    for frase in capitulo:
        for letra in frase:
            sys.stdout.write(letra)
            sys.stdout.flush()
            
            if letra == ',' or letra == '.':
                sleep(.2)
            else:
                sleep(.02)
        

def enter(): input(f'\n{FCORES["Amarelo"]}[ENTER]{FCORES["Branco"]}')


def digite():
    op = input(f'{LAYOUT["USU"]}: ')
    return op


################ ERROS ################
def generic_error(error):
    print(f'\n Um erro ocorreu: {error}\nCLASSE DE ERRO: {error.__class__}\nCAUSA: {error.__cause__} \n')


def keyboard_brake():
    print('>>> O Jogador fechou o jogo em execução <<<')
