from nodo import nodo

class Cola_Prioridad_Personas:
    def __init__(self):
        self.__list = None

    def encolar(self, persona):
        nuevo_nodo = nodo(persona)

        if self.__list is None:
            self.__list = nuevo_nodo
            return

        if persona.edad >= 65:
            last_senior = None
            current = self.__list

            while current and current.getData().edad >= 65:
                last_senior = current
                current = current.getNext()

            if last_senior:
                nuevo_nodo.setNext(last_senior.getNext())
                last_senior.setNext(nuevo_nodo)
            else:
                nuevo_nodo.setNext(self.__list)
                self.__list = nuevo_nodo

            return


        current = self.__list
        while current.getNext():
            current = current.getNext()
        current.setNext(nuevo_nodo)

    def desencolar(self):
        if self.__list:
            persona_eliminada = self.__list.getData()
            self.__list = self.__list.getNext()
            print(f"🗑 Se eliminó de la cola: {persona_eliminada}")
            return persona_eliminada
        else:
            print("⚠ La cola está vacía.")
            return None









