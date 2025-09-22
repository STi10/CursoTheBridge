def mostrar_menu():
    print("\n" + "="*40)
    print("           CALCULADORA BÁSICA")
    print("="*40)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Ver historial")
    print("7. Salir")
    print("="*40)

historial = []  # Lista para almacenar el historial de operaciones

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-7): ")
    
    if opcion == "7":
        print("\n¡Gracias por usar la calculadora!")
        break
    elif opcion == "6":
        print("\nHistorial de operaciones:")
        if not historial:
            print("No hay operaciones registradas")
        else:
            for operacion in historial:
                print(operacion)
    elif opcion in ["1", "2", "3", "4", "5"]:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
            continue
        
        if opcion == "1":
            resultado = num1 + num2
            operacion = f"{num1} + {num2} = {resultado}"
            print(f"\nResultado: {operacion}")
            historial.append(operacion)  # Guardar la operación en el historial
        elif opcion == "2":
            resultado = num1 - num2
            operacion = f"{num1} - {num2} = {resultado}"
            print(f"\nResultado: {operacion}")
            historial.append(operacion)  # Guardar la operación en el historial
        elif opcion == "3":
            resultado = num1 * num2
            operacion = f"{num1} × {num2} = {resultado}"
            print(f"\nResultado: {operacion}")
            historial.append(operacion)  # Guardar la operación en el historial
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                operacion = f"{num1} ÷ {num2} = {resultado}"
                print(f"\nResultado: {operacion}")
                historial.append(operacion)  # Guardar la operación en el historial
            else:
                print("\nError: No se puede dividir por cero")
                continue
        elif opcion == "5":
            resultado = num1 ** num2
            operacion = f"{num1} ^ {num2} = {resultado}"
        
            print(f"\nResultado: {operacion}")
            historial.append(operacion)  # Guardar la operación en el historial
    else:
        print("\nOpción no válida. Por favor, elija una opción del 1 al 7.")