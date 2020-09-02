from functions import *

def run():
    set = [1, 2, 3, 4, 5]
    #relation =((1,1), (2,2), (3,3),(4,4),(10,10), (20,20),(1,2) )
    #relation = ((1,2),(1,3),(1,4),(2,3),(2,4),(3,4))
    relation =((1,1),(2,2),(3,3),(4,4),(5,5),(1,2),(1,5),(2,5),(3,5),(4,5))
    print("reflexiva: ", is_reflexive(relation,set))
    print("simétrica: ",is_symmetric(relation))
    print("antisimétrica: ",is_antisymmetric(relation))
    print("transitiva: ", is_transitive(relation))
    print("relación de quivalencia: ",is_equivalence_relation(set,relation))
    print("relación de orden parcial: ",is_parcial_order_relation(set, relation))

if __name__ == '__main__':
    run()