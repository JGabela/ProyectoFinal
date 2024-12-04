#El ahorcado

import funciones

print('EL AHORCADO')
jugar = True

while jugar is True:

    respuesta = funciones.bancopalarbras()
    espacio = '_____'
    print(espacio)



    #Al terminar la partida se le pregunta al usuario si quiere seguir jugando o no
    a = input('Quiere seguir jugando?')
    if a == 'si':
        jugar = True
    elif a == 'Si':
        jugar = True
    elif a == 'no':
        jugar = False
    elif a == 'No':
        jugar = False