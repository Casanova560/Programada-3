from nodo import nodo

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.__list = None

    def insertar(self, persona):
        nuevo_nodo = nodo(persona)

        if self.__list is None or self.__list.getData().edad > persona.edad:
            nuevo_nodo.setNext(self.__list)
            self.__list = nuevo_nodo
            return

        current = self.__list
        while current.getNext() and current.getNext().getData().edad < persona.edad:
            current = current.getNext()

        nuevo_nodo.setNext(current.getNext())
        current.setNext(nuevo_nodo)


    def imprimir(self):
        if self.__list is None:
            print("La lista está vacía.")
            return

        current = self.__list
        contador = 0
        while current:
            print(current.getData())
            current = current.getNext()
            contador += 1
        print(f"Total de personas en la lista: {contador}")

    def eliminar_por_posicion(self, posicion):
        if self.__list is None:
            print("Lista vacía.")
            return

        if posicion == 0:
            self.__list = self.__list.getNext()
            return

        prev = None
        current = self.__list
        index = 0
        while current and index < posicion:
            prev = current
            current = current.getNext()
            index += 1

        if current is None:
            print(f"No existe la posición {posicion}. La lista tiene {index} elementos.")
        else:
            prev.setNext(current.getNext())
            print(f"Se ha eliminado la persona en la posición {posicion}.")

    def buscar_por_edad(self, edad):
        current = self.__list
        encontrados = []

        while current:
            if current.getData().edad == edad:
                encontrados.append(current.getData())
            current = current.getNext()

        if encontrados:
            print(f"\nPersonas encontradas con edad {edad}:")
            for persona in encontrados:
                print(persona)
        else:
            print("No hay personas con esa edad.")

    def buscar_por_nombre_o_apellido(self, texto):
        current = self.__list
        encontrados = []

        while current:
            persona = current.getData()
            if (texto.lower() in persona.nombre.lower() or
                    texto.lower() in persona.apellido1.lower() or
                    texto.lower() in persona.apellido2.lower()):
                encontrados.append(persona)
            current = current.getNext()

        if encontrados:
            print(f"\nPersonas encontradas con '{texto}':")
            for persona in encontrados:
                print(persona)
        else:
            print("No hay coincidencias con el criterio de búsqueda.")

