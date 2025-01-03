#Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#El juego comienza proponiendo una palabra aleatoria incompleta
#- Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#la palabra a adivinar)
#- Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
# -uno al número de intentos
#- Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  al número de intentos
# -Si el contador de intentos llega a 0, el jugador pierde
#-La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#- Puedes utilizar las palabras que quieras y el número de intentos que consideres

import random

print("Programa para que adivines la palabra secreta")
print("")

# Ponemos el número de intentos
intentos = 7

# Hacemos una lista de palabras
palabras_secretas = ["INGENIERO", "PROGRAMACION", "COMPUTADORAS", "LAPTOPS", "PYTHON", "SISTEMA", "JUGAR"]

# Usamos esta función para elegir una palabra aleatoria de la lista
palabra_secreta = random.choice(palabras_secretas)

# Hacemos la palabra secreta en forma de lista (oculta inicialmente será igual a la palabra secreta)
oculta = list(palabra_secreta)

# Creamos una función que genere la palabra secreta y oculte letras aleatoriamente
def generar():
    for i in range(int(len(palabra_secreta) * 0.6)):
        # Se elige una posición aleatoria en la lista y se reemplaza el carácter por '_'
        while True:
            index = random.randrange(len(palabra_secreta))
            if oculta[index] != '_':  # Aseguramos que no reemplazamos un '_' existente
                oculta[index] = '_'
                break

# Función para comprobar las letras que el usuario ingresa
def comprobar():
    global intentos, oculta
    introducir = input("Ingrese una letra o la palabra completa: ").upper()

    if len(introducir) == 1 and introducir in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if introducir == palabra_secreta[i]:
                oculta[i] = introducir
    elif introducir == palabra_secreta:
        oculta = list(palabra_secreta)  # Si acierta la palabra completa, mostramos la palabra completa
    else:
        intentos -= 1

def main():
    generar()

    while intentos > 0 and oculta != list(palabra_secreta):
        print(''.join(oculta), f' - Te quedan {intentos} intentos.')
        comprobar()

    final = 'Ganado' if oculta == list(palabra_secreta) else 'Perdido'
    print(f'¡Has {final}! La palabra completa era "{palabra_secreta}".')

if __name__ == '__main__':
    main()