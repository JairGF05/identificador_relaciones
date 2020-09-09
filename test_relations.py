from graphviz import Digraph
from functions import *
from graph2 import *

def run():
    #set = [1, 2, 3, 4, 5]
    set = ['a', 'b', 'c', 'd']
    #set = [1,2,3,4,5]
    #relation =((1,1), (2,2), (3,3),(4,4),(10,10), (20,20),(1,2) )
    relation =(('a','a'),('a','d'),('d','d'),('d','a'),('b','b'),('b','c'),('c','c'),('c','b'))
    #relation = [(1,1),(2,2),(3,3),(4,4),(5,5),(1,3),(2,4),(3,5),(3,1),(4,2),(5,3)]
    print("comprueba tipo de relaciones")
    print("reflexiva: ", is_reflexive(relation,set))
    print("simétrica: ",is_symmetric(relation))
    print("antisimétrica: ",is_antisymmetric(relation))
    print("transitiva: ", is_transitive(relation))
    print("relación de quivalencia: ",is_equivalence_relation(set,relation))
    print("relación de orden parcial: ",is_parcial_order_relation(set, relation))
    print(" ")
    
    print("Justificaciones")
    print(print_reflexive(relation,set))
    print(print_symmetric(relation))
    print(print_transitive(relation))
    print(print_equivalence_relation(set,relation))
    print(print_parcial_order_relation(set, relation))
    
    #funcion para dibujado de grafo, cambiar a que imprima grafo solo si es de equivalencia
    draw_graph(relation)

if __name__ == '__main__':
    run()
