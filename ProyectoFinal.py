#Proyecto Integrador, juego de memorama

import random
import sys

def crea_lista_inicial(num):
    """Crea lista inicial con número aleatorios iniciando en el número 1 hasta el número especificado,
        agrega 2 números iguales de cada número """
    lista_inicial = []
    for i in range(num):
        lista_inicial.append(i+1)
        lista_inicial.append(i+1)
    print(lista_inicial )
    random.shuffle(lista_inicial)
    print(lista_inicial )
    return lista_inicial

def crea_tablero(lista):
    # Crea tablero inicial a partir de una lista dada 
    matriz_inicial = []
    cont = 0
    sub_lista =[]
    for i in range(len(lista)):
        if (cont== 5):
            sub_lista.append(lista[i])
            matriz_inicial.append(sub_lista)
            sub_lista =[]
            cont = 0
        else:
            sub_lista.append(lista[i])
            cont = cont +1
    return matriz_inicial

def imprime_tablero(matriz):
    print('    {:^4} {:^4} {:^4} {:^4} {:^4} {:^4}'.format(0,1,2,3,4,5))
    print('  |______________________________\n')  
    for i in range(len(matriz)):
        print(i, '|', end=' ' )
        for j in range(len(matriz[i])):
            print('{0:^4}'.format(matriz[i][j]), end=' ')
        print('    \n')

def asteriscos(n):
    matriz=[]
    for  i in range (0,n):
        matrizsub=[]
        for  i in range (0,n):
            matrizsub.append('*')
        matriz.append(matrizsub)
    return (matriz)

def leer(Letrero):
    while True:
        num=input(Letrero)
        if num.isdecimal() and num in ('0', '1', '2', '3', '4', '5'):
            num=int(num)
            break
    return num
def main():
    print('* * * * * BIENVENIDO EL JUEGO DE MEMORIA * * * * *\n\n')
#Matriz de cartas
    lista = crea_lista_inicial(18)
#Tablero de numeros y Tablero de asteriscos

    tablero = crea_tablero(lista)
    tableroasteriscos=asteriscos(6)
#Imprimir los tableros de numeros y asteriscos
    imprime_tablero(tablero)
    imprime_tablero(tableroasteriscos)
#Variables de turno de jugador, cambiar de turno y puntos de jugador 1 y 2
    tj=1
    pj1=0
    pj2=0
    cambiarT='s'
    nom1=input('Nombre del jugador 1: ' )
    nom2=input('Nombre del jugador 2: ' )    
    while True:
        if tj == 1:
            print('\nToca turno a jugador 1 - ',nom1)
        else:
            print('\nToca turno a jugador 2 - ',nom2)  
        while True:
            rc1=leer('Inserta el Renglón, carta #1: ')
            cc1=leer('Inserta una Columna, carta #1: ')
            print('Elejiste: ',tablero[rc1][cc1])
            rc2=leer('Renglon, carta #2: ')
            cc2=leer('Columna, carta #2: ')
            print('Elejiste: ',tablero[rc2][cc2])
            if tablero[rc1][cc1]=='*' or tablero[rc2][cc2]=='*':
                print('Carta abierta')
                continue
            if rc1==rc2 and cc1==cc2:
                print('Carta repetida')
                continue
            else:
                break
        
        if tablero[rc1][cc1]==tablero[rc2][cc2]:
            tableroasteriscos[rc1][cc1]=tablero[rc1][cc1]
            tableroasteriscos[rc2][cc2]=tablero[rc2][cc2]
            tablero[rc1][cc1]='*'
            tablero[rc2][cc2]='*'
            if tj==1:
                pj1=pj1+1
                print('Punto para el jugador 1: ', pj1)
            else:
                pj2=pj2+1
                print('Punto para el jugador 2: ', pj2)
            cambiarT='n'
            imprime_tablero(tablero)
            imprime_tablero(tableroasteriscos)
        
        else:
            cambiarT='s'
        if cambiarT=='s':
            if tj==1:
                tj=2
            else:
                tj=1

        
        while True:
            
            if (pj1 + pj2) == 18:
                print('--  EL JUEGO TERMINO --')
                print('--  TABLERO COMPLETO -- ')
                sys.exit()
        
            sj=input('¿Deseas seguir jugando? s/n ')
            if sj in ('s','S','N','n'):
                break
            
        if sj == 'n':
            
            print('El jugador uno termino con', pj1, 'puntos')
            print('El jugador dos termino con', pj2, 'puntos')
            
            if pj1 > pj2:
                print('El ganador es el jugador 1,', nom1)
                
            elif pj2>pj1:
                print('El ganador es el jugador 2,', nom2)
                
            else:
                print('EMPATE')
            
            break
          
main()