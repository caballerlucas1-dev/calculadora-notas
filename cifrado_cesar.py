# cifrado_cesar.py
def cifrar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

def menu():
    print("=== Cifrado César ===")
    while True:
        print("\n1. Cifrar mensaje\n2. Descifrar mensaje\n3. Fuerza bruta (descifrar sin clave)\n4. Salir")
        op = input("Opción: ")

        if op == "1":
            msg = input("Mensaje: ")
            d = int(input("Desplazamiento (1-25): "))
            print(f"Cifrado: {cifrar(msg, d)}")

        elif op == "2":
            msg = input("Mensaje cifrado: ")
            d = int(input("Desplazamiento: "))
            print(f"Descifrado: {descifrar(msg, d)}")

        elif op == "3":
            msg = input("Mensaje cifrado: ")
            print("\n--- Todas las posibilidades ---")
            for i in range(1, 26):
                print(f"  Desplazamiento {i:2}: {descifrar(msg, i)}")

        elif op == "4":
            break

if __name__ == "__main__":
    menu()
