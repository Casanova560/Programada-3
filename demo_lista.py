from single_linked_list import single_linked
from nodo import nodo

mi_lista = single_linked()
nodo1 = nodo(44)
mi_lista.imprimir()
mi_lista.insert(nodo1)
print("---")
mi_lista.imprimir()
nodo2 = nodo(33)
mi_lista.insert(nodo2)
nodo3 = nodo(25)
mi_lista.insert(nodo3)
nodo4 = nodo(66)
mi_lista.insert(nodo4)
print("---")
mi_lista.imprimir()
print("----+++++++")
mi_lista.delete(nodo3)
mi_lista.imprimir()