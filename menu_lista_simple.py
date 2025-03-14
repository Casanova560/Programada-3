from single_linked_list import ListaEnlazadaOrdenada
from persona import Persona

lista = ListaEnlazadaOrdenada()

while True:
    print("\n1. Agregar persona")
    print("2. Listar personas")
    print("3. Borrar persona")
    print("4. Buscar persona por edad")
    print("5. Buscar persona por nombre o apellido")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        lista.insertar(persona)

    elif opcion == "2":
        lista.imprimir()

    elif opcion == "3":
        pos = int(input("Ingrese la posición de la persona que desea eliminar: "))
        lista.eliminar_por_posicion(pos)

    elif opcion == "4":
        edad = int(input("Ingrese la edad que desea buscar: "))
        lista.buscar_por_edad(edad)

    elif opcion == "5":
        texto = input("Ingrese un nombre o apellido para buscar: ")
        lista.buscar_por_nombre_o_apellido(texto)

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida, intente de nuevo.")
