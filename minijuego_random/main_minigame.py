# Minijuego: Adivina el número (Nivel principiante)

# 🧠 Objetivo del juego:
# La computadora elige un número aleatorio entre 1 y 20.
# El usuario tiene 5 intentos para adivinar el número.

# 🔁 Reglas del juego:

# Después de cada intento, la computadora dirá si el número ingresado es mayor o menor que el número secreto.

# Si el usuario adivina correctamente, el juego termina con un mensaje de victoria.

# Si se acaban los 5 intentos sin adivinar, se muestra un mensaje de derrota con el número correcto.

# 💡 Pistas:

# Necesitarás importar el módulo random.

# Usa un bucle para los intentos.

# Usa condicionales if, elif, else para comparar los números.

from os import system
system("cls")
import random


print("Bienvenido al juego de adivinanza de numeros\n")
print("Ingresa un numero limite en el que pensare y tu trataras de adivinar\n")

limite_usuario = int(input("Ingresa Un numero limite para jugar: "))

    
def pensar_numero(limite_usuario):
    numero_secreto = random.randint(1, limite_usuario)
    intentos = 0
    adivino = False
    
    print("Tienes 10 Intentos Para Adivinar, o sino PERDERAS!")
    print(f"\nmmm, ya pense en un numero entre el 1 y {limite_usuario}")
    
    while intentos < 10:
        try:
            numero_ingresado = int(input("\n\tIntenta adivinar: "))

        except:
            print("Lo que ingresaste no es un numero, intenta devuelta. ")
            continue
        if numero_ingresado > numero_secreto:
            print("\nEl numero secreto es Menor.")
            print("Hazlo nuevamente :)")
            intentos += 1
            continue
        elif numero_ingresado < numero_secreto:
            print("\nEl Numero Secreto es Mayor.")
            print("Hazlo nuevamente :)")
            intentos += 1
            continue
        else:
            print("\nSIII, Felicidades Haz Ganado!!!")
            print(f"El Numero Secreto Es: {numero_secreto} ;)\nLo Conseguiste en{intentos + 1} intentos.\n")
            adivino = True
            break
    
    if not adivino:   
        print(f"\nLo siento, te quedaste sin intentos 😢 El número era  {numero_secreto}\n")

pensar_numero(limite_usuario)