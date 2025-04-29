import random

def determinar_ganador(usuario, programa):
    """Determina quién gana: 1=usuario, 0=empate, -1=programa"""
    usuario = usuario.lower()
    programa = programa.lower()
    
    if usuario == programa:
        return 0
    
    if (usuario == "piedra" and programa == "tijera") or \
       (usuario == "tijera" and programa == "papel") or \
       (usuario == "papel" and programa == "piedra"):
        return 1
    else:
        return -1

def jugar():
    print("Juguemos Piedra, Papel o Tijeras (3 rondas)")
    
    # Pedir jugadas al usuario
    usuario = []
    for i in range(3):
        while True:
            jugada = input(f"Ronda {i+1}: Elige piedra, papel o tijera: ").lower()
            if jugada in ["piedra", "papel", "tijera"]:
                usuario.append(jugada)
                break
            print("¡Opción no válida! Intenta otra vez.")

    # Generar jugadas del programa
    programa = [random.choice(["piedra", "papel", "tijera"]) for _ in range(3)]
    print(f"\nEl programa eligió: {', '.join(programa)}")
    
    # Comparar jugadas
    puntos_usuario = 0
    puntos_programa = 0
    
    for u, p in zip(usuario, programa):
        resultado = determinar_ganador(u, p)
        if resultado == 1:
            puntos_usuario += 1
        elif resultado == -1:
            puntos_programa += 1
    
    # Mostrar resultados
    print(f"\nPuntuación final - Usuario: {puntos_usuario} | Programa: {puntos_programa}")
    
    if puntos_usuario > puntos_programa:
        print("¡Ganaste! 🎉")
    elif puntos_programa > puntos_usuario:
        print("¡Ganó el programa! 🤖")
    else:
        print("¡Empate! 😐")

# Iniciar el juego
if __name__ == "__main__":
    jugar()