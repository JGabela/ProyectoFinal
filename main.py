#El ahorcado

import funciones

print('EL AHORCADO')
jugar = True #La variable se la usa para el loop while que corre el juego
#Solo funciona como separadores para que se vea mejor la interfaz del juego
print('-----------------------------------------------')

while jugar is True: #El loop sirve para volver a jugar si el usuario lo desea

    fallos = 0 #Lleva cuenta de los fallos del usuario en el juego, se resetea al inicio de una partida nueva
    respuesta = funciones.bancopalarbras() #Extrae un palabra random para la partida, es la respuesta correcta
    palabra = ['_', '_', '_', '_', '_']

    print('Palabra: _ _ _ _ _')
    print('Tiene 5 intentos')
    print('')
    funciones.visuales(0) #Siempre va a mostrar la visual de la ahorca vacia al inicio del juego

    while fallos < 6:

        print('-----------------------------------------------')

        resp_usuario = input('Ingrese una letra: ')
        fallos = funciones.intentos(resp_usuario,fallos, respuesta)
        funciones.marcador(resp_usuario, respuesta, palabra)

        print('Intentos:', 6 - fallos)

        funciones.visuales(fallos)

    if fallos == 6:
        print('La respuesta es:' ,respuesta)

    print('')

    #Al terminar la partida se le pregunta al usuario si quiere seguir jugando o no
    jugar = funciones.denuevo(jugar)
    print('-----------------------------------------------')