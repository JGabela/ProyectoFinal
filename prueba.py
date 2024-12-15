respuesta = 'puerta'
#respuesta = 'perro'
palabra = ['_', '_', '_', '_', '_']
resp_usuario = input('Ingrese una letra: ')

def marcador(resp_usuario, respuesta, palabra):
    respuesta = list(respuesta)
    if resp_usuario in respuesta:
        indice_letra = respuesta.index(resp_usuario)
        print(indice_letra)
        #palabra[indice_letra] = resp_usuario
        #print(' '.join(palabra))
    else:
        print(' '.join(palabra))

print(marcador(resp_usuario, respuesta, palabra))

p = 'j k'
print(p.replace(' ', ''))