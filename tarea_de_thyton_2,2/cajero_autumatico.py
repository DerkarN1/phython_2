#Fecha:14/06/2026
#Autor:Bryan Adriano Nazareno Quiñonez
#Tema:Diseña un programa que simule un cajero automático básico mediante un menú en pantalla. 
# Debe mostrar las opciones: 1. Consultar Saldo, 2. Depositar Dinero, 3. Retirar Dinero y 4. Salir.
# El programa debe repetirse continuamente usando un bucle WHILE hasta que el usuario digite la opción 4. 
# Si ingresa un número inválido, debe avisar del error.

saldo = 1000.00  # Saldo inicial de prueba
opcion = 0

while opcion != 4:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción (1-4): "))
    
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo:.2f}")
    elif opcion == 2:
        deposito = float(input("Monto a depositar: $"))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Error: El monto a depositar debe ser mayor a 0.")
    elif opcion == 3:
        retiro = float(input("Monto a retirar: $"))
        if retiro > 0 and retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
        elif retiro > saldo:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: El monto a retirar debe ser mayor a 0.")
    elif opcion == 4:
        print("Gracias por usar nuestros servicios. ¡Hasta luego!")
    else:
        print("Error: Opción inválida. Por favor, intente nuevamente.")