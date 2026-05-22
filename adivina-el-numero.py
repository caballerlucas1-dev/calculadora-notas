# adivina_el_numero.py
import random

def jugar():
    print("=== Adivina el Número ===")
    dificultad = input("Dificultad (1=Fácil 1-50, 2=Medio 1-100, 3=Difícil 1-200): ")
    limites = {"1": 50, "2": 100, "3": 200}
    limite = limites.get(dificultad, 100)
    numero = random.randint(1, limite)
    intentos = 0

    while True:
        try:
            guess = int(input(f"Adiviná (1-{limite}): "))
        except ValueError:
            print("Ingresá un número válido.")
            continue
        intentos += 1
        if guess < numero:
            print("Muy bajo ↑")
        elif guess > numero:
            print("Muy alto ↓")
        else:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar()
