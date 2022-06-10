import capitulos
import arte
import faux
from time import sleep

if __name__ == "__main__":

    try:
        
        frase = f'\n\n{faux.LAYOUT["INF"]} Saudações Jogador, gostaria de ver as regras? [S]/[N]\n'
        faux.efeito_digitar(frase)
        sleep(.5)

        op = str(input('>> Digite aqui: ')).upper()

        if op == 'S':
            faux.efeito_digitar(capitulos.CAPITULOS['1']['texto'])
            
            faux.enter()


        arte.mostrar_logo()
        input('Aperte qualquer tecla para continuar...')
        faux.limpar_terminal()



    except KeyboardInterrupt: faux.keyboard_brake()

    except Exception as error: faux.generic_error(error)
