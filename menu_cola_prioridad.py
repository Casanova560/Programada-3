from cola_prioridad import Cola_Prioridad_Personas
from persona import Persona

cola = Cola_Prioridad_Personas()

while True:
    print("\n1. Agregar persona a la cola")
    print("2. Mostrar cola")
    print("3. Desencolar (eliminar el primero)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        cola.encolar(persona)

    elif opcion == "2":
        current = cola._Cola_Prioridad_Personas__list
        if current is None:
            print("⚠ La cola está vacía.")
        else:
            print("\n📌 Estado actual de la cola:")
            while current:
                print(current.getData())
                current = current.getNext()

    elif opcion == "3":
        cola.desencolar()

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
