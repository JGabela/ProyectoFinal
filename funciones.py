import random #Se usa para hacer la seleccion de palabras aleatoria

def bancopalarbras(): #Escoge una palabra para el juego de manera aleatoria
    banco = {
        1: 'banco',
        2: 'pasto',
        3: 'clero',
        4: 'clase',
        5: 'letra'
    }
    palabra = banco.get(random.randint(1, 5)) #
    return palabra

#Esta funcion revisa si la respuesta del usuario esta en la palabra respuesta, y lleva la cuenta de los fallos
def intentos(resp_usuario,fallos, respuesta):
    if resp_usuario in respuesta:
        return fallos
    else:
        fallos += 1
        return fallos

#Esta funcion revisa si la repsuesta del usuario esta en la palabra respuesta
#si es asi la anade a una lista para mostrar el progreso del usuario
def marcador(resp_usuario, respuesta, palabra):
    respuesta = list(respuesta)
    if resp_usuario in respuesta:
        indice_letra = respuesta.index(resp_usuario)
        palabra[indice_letra] = resp_usuario
        marc = ' '.join(palabra)
        return marc
    else:
        marc = ' '.join(palabra)
        return marc

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

