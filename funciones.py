import random #Se usa para hacer la seleccion de palabras aleatoria

def bancopalarbras(): #Escoge una palabra para el juego de manera aleatoria
    banco = {
        1: 'banco',
        2: 'pasta',
        3: 'perro',
        4: 'puerta',
        5: 'letra'
    }
    palabra = banco.get(random.randint(1, 5))
    return palabra

print(bancopalarbras())
