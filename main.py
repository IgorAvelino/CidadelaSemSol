import json

import arte
import faux
from time import sleep

if __name__ == "__main__":
    try:
        file = open('config.json', 'r') 
    
    except FileNotFoundError:
        print(f'\n{faux.LAYOUT["F_ERROR"]} Não foi possível encontrar o arquivo de configuração!')
        exit()
    
    else:
        try:
            cfg = json.load(file)
        except Exception as error: faux.generic_error(error)
    
    try:
        
        frase = f'\n\n{faux.LAYOUT["INF"]} Saudações Jogador, gostaria de ver as regras? [S]/[N]\n'
        faux.efeito_digitar(frase)
        sleep(.5)

        op = str(input('>> Digite aqui: ')).upper()

        if op == 'S':
            faux.efeito_digitar(cfg['CAPITULOS']['1']['Texto'])
            
            faux.enter()


        arte.mostrar_logo()
        input('Aperte qualquer tecla para continuar...')
        faux.limpar_terminal()



    except KeyboardInterrupt: faux.keyboard_brake()

    except Exception as error: faux.generic_error(error)
