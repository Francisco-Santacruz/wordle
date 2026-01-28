import random

def elegir_palabra():
    palabras = [
        "perro", "gatos", "silla", "mesas", "plaza",
        "lunas", "soles", "nubes", "llave", "fuego",
        "aguaa", "arbol", "flota", "rueda", "pluma",
        "papel", "carta", "raton", "tecla", "reloj",
        "libro", "pared", "suelo", "vapor", "cable",
        "radio", "piano", "botas", "coche", "playa"
    ]
    return random.choice(palabras)

def palabra_valida(palabra):
    if len(palabra) != 5:
        return False
    if not palabra.isalpha():
        return False
    return True

def evaluar_intento(palabra, wordle):
    aciertos = 0
    resultado = []

    for i in range(5):
        if palabra[i] == wordle[i]:
            resultado.append("SIII")
            aciertos += 1
        elif palabra[i] in wordle:
            resultado.append("CASI")
        else:
            resultado.append("NOOO")

    return aciertos, resultado

def jugar_wordle():
    wordle = elegir_palabra()
    oportunidades = 0

    print("Bienvenidos a WORDLE")

    while oportunidades < 6:
        print(f"Oportunidad #{oportunidades + 1}")
        palabra = input("Ingrese una palabra: ").lower()

        if not palabra_valida(palabra):
            print("La palabra no es válida (5 letras, solo letras)")
            continue

        aciertos, resultado = evaluar_intento(palabra, wordle)

        for i in range(5):
            print(palabra[i], "-", resultado[i])

        print(f"Tenés {aciertos} aciertos")

        if aciertos == 5:
            print("...::: ¡¡¡FELICIDADES GANASTE!!! :::...")
            return

        oportunidades += 1

    print("PERDISTE")
    print("La palabra era:", wordle)

# Ejecutar el juego
jugar_wordle()
