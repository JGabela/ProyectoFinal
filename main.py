#El ahorcado

import funciones

print('EL AHORCADO')
jugar = True #La variable se la usa para el loop while que corre el juego
#Solo funciona como separadores para que se vea mejor la interfaz del juego
print('-----------------------------------------------')

while jugar is True: #El loop sirve para volver a jugar si el usuario lo desea

    respuesta = funciones.bancopalarbras() #Extrae un palabra random para la partida
    espacio = 'Palabra: _____'
    print(espacio)
    print('')






    #Al terminar la partida se le pregunta al usuario si quiere seguir jugando o no
    jugar = funciones.denuevo(jugar)
    print('-----------------------------------------------')