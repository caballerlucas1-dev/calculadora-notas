# calculadora_notas.py
def calcular_promedio():
    print("=== Calculadora de Notas ===")
    materias = []
    while True:
        materia = input("Nombre de la materia (o 'fin' para terminar): ")
        if materia.lower() == "fin":
            break
        nota = float(input(f"Nota de {materia}: "))
        materias.append((materia, nota))

    if not materias:
        print("No ingresaste materias.")
        return

    print("\n--- Resumen ---")
    for m, n in materias:
        estado = "Aprobado" if n >= 6 else "Desaprobado"
        print(f"{m}: {n} → {estado}")

    promedio = sum(n for _, n in materias) / len(materias)
    print(f"\nPromedio general: {promedio:.2f}")

if __name__ == "__main__":
    calcular_promedio()
