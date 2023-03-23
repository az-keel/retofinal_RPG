import random

# Definimos las palabras base para cada nivel
palabras_faciles = ['tina', 'piso', 'ropa', 'mesa']
palabras_intermedias = ['ambulante', 'alfombras', 'biologico', 'computado']
palabras_avanzadas = ['microondas', 'perpendicular', 'revolucionario', 'trascendencia']

# Definimos una función que mostrará la palabra base con las letras adivinadas por el usuario
def mostrar_palabra(palabra_base, letras_adivinadas):
    palabra_mostrada = ''
    for letra in palabra_base:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += '-'
    return palabra_mostrada

# Definimos una función que valida que la letra ingresada por el usuario sea única
def validar_letra(letra, letras_adivinadas):
    if letra in letras_adivinadas:
        print('Ya ingresaste esa letra, intenta con otra.')
        return False
    else:
        return True

# Definimos la función principal del juego
def jugar_ahorcado():
    # Pedimos al usuario que elija el nivel a jugar
    nivel = ''
    while nivel not in ['facil', 'intermedio', 'avanzado']:
        nivel = input('Elige un nivel para jugar (facil, intermedio, avanzado): ').lower()
    if nivel == 'facil':
        palabra_base = random.choice(palabras_faciles)
    elif nivel == 'intermedio':
        palabra_base = random.choice(palabras_intermedias)
    else:
        palabra_base = random.choice(palabras_avanzadas)
    letras_adivinadas = []
    print('La palabra base tiene', len(palabra_base), 'letras.')
    while True:
        letra = input('Ingresa una letra (o 0 para salir): ').lower()
        if letra == '0':
            break
        if not letra.isalpha() or len(letra) > 1:
            print('Ingresa una letra valida.')
            continue
        if not validar_letra(letra, letras_adivinadas):
            continue
        letras_adivinadas.append(letra)
        palabra_mostrada = mostrar_palabra(palabra_base, letras_adivinadas)
        print(palabra_mostrada)
        if '-' not in palabra_mostrada:
            print('¡Ganaste!')
            break
    print('Fin del juego.')

# Ejecutamos el juego
jugar_ahorcado()
