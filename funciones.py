import random #Se usa para hacer la seleccion de palabras aleatoria

def bancopalarbras(): #Escoge una palabra para el juego de manera aleatoria
    banco = {
        1: 'banco',
        2: 'pasta',
        3: 'perro',
        4: 'puerta',
        5: 'letra'
    }
    palabra = banco.get(random.randint(1, 5)) #
    return palabra

def intentos(fallos, respuesta):
    resp_usuario = input('Ingrese una letra: ')
    if resp_usuario in respuesta:
        print(resp_usuario)
        return fallos
    else:
        fallos += 1
        return fallos

#Imprime visuales para representar los fallos del usuario
#Al llegar a 6 fallos pierde
def visuales(fallos):
    if fallos == 0:
        print(' +_____+')
        print(' |     |')
        print(' |    ')
        print(' |    ')
        print(' |    ')
        print(' |    ')
        print(' |     ')
        print(' ---------')
    elif fallos == 1:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |    ')
        print(' |     ')
        print(' |    ')
        print(' |     ')
        print(' ---------')
    elif fallos == 2:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |     |')
        print(' |     |')
        print(' |    ')
        print(' |     ')
        print(' ---------')
    elif fallos == 3:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |    /|')
        print(' |     |')
        print(' |    ')
        print(' |     ')
        print(' ---------')
    elif fallos == 4:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |    /|\\')
        print(' |     |')
        print(' |    ')
        print(' |     ')
        print(' ---------')
    elif fallos == 5:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |    /|\\')
        print(' |     |')
        print(' |    / ')
        print(' |     ')
        print(' ---------')
    elif fallos == 6:
        print(' +_____+')
        print(' |     |')
        print(' |     0')
        print(' |    /|\\')
        print(' |     |')
        print(' |    / \\')
        print(' |     ')
        print(' ---------')
        print('PERDISTE')

def denuevo(jugar): #Pregunta si el usuario quiere seguir jugando o no
    a = input('Quiere seguir jugando?: ')
    if a == 'si':
        jugar = True
    elif a == 'Si':
        jugar = True
    else:
        jugar = False
    return jugar

