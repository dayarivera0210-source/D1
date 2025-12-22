#-*coding:cp1252-* # Codificación para caracteres especiales en español

import random  # Importa el módulo random para generar elecciones aleatorias

def jugar():
    opciones = ["piedra", "papel", "tijera"]  # Lista de opciones válidas para el juego
    
    usuario = input("Elige piedra, papel o tijera: ").lower()  # Solicita entrada del jugador y la convierte a minúsculas
    
    if usuario not in opciones:  # Verifica si la opción ingresada es válida
        print("Opción no válida, inténtalo de nuevo.")  # Mensaje de error si la opción no está en la lista
        return  # Sale de la función sin continuar el juego
    
    computadora = random.choice(opciones)  # La computadora elige una opción aleatoria de la lista
    
    print(f"Computadora eligió: {computadora}")  # Muestra la elección de la computadora
    
    if usuario == computadora:  # Si ambas elecciones son iguales, es empate
        print("Empate.")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "papel" and computadora == "piedra"):  # Condiciones en las que el jugador gana
        print("Ganaste.")
    else:
        print("Perdiste.")  # Si no es empate ni victoria, entonces el jugador pierde

# Ciclo principal
while True:  # Bucle infinito para permitir múltiples partidas
    jugar()  # Llama a la función para iniciar una partida
    otra = input("¿Quieres jugar otra vez? (s/n): ").lower()  # Pregunta si el jugador quiere continuar
    if otra != "s":  # Si la respuesta no es "s", se termina el juego
        print("Gracias por jugar")  # Mensaje de despedida
        break  # Sale del bucle y finaliza el programa
