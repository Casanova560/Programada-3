from lista_doble_enlace import lista_doble_enlace
from nodo_doble_enlace import nodo_doble

lista = enlace_lista_doble()

node1 = nodo_doble(99)
node2 = nodo_doble(21)
node3 = nodo_doble("hola")

lista.imprimir()
lista.insert(node1)
print("----")
lista.insert(node2)
lista.imprimir()
print("+++++")
lista.insert(node3)
lista.imprimir()
print("=====")
lista.delete(node2)
lista.imprimir()