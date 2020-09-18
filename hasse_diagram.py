
from graphviz import Digraph
from functions import *

#crear un grafo vacio
#g = nx.Graph()

def draw_hasse(relation, set):
    g = Digraph('G', filename='hasse.gv')
    
    #convertir los nodos a puntos
    #g.attr('node',shape = 'point')
    
    #hace el grafo mas pequeño
    g.attr(size = '0.8')
    #modificando el tamaño de los nodos
    g.attr('node', width = '0.4', height ='0.4')
    
    #aqui quitaremos los pares transitivos
    new_relation = []
    for a,b in relation:
        for c,d in relation:
            if b == c and ([a,d] in relation):
                new_relation.append((a,d))
    
    #tenemos que hacer que pase de los reflexivos y transitivos
    for a, b in new_relation :
        #if a != b :
        g.edge(str(a), str(b))
            
                    
        
    
    #cambiando de color los nodos del grafo g
    
    g.view()
    
def run():
    set = [1,2,3,4,6,12]
    relation = [(1,1),(2,2),(3,3),(4,4),(6,6),(12,12),(1,2),(1,3),(1,4),(1,6),(1,12),(2,3),(2,4),(2,6),(2,12)
            ,(3,4),(3,6),(3,12),(4,6),(4,12),(6,12)]
    draw_hasse(relation,set)
    
    

if __name__ == '__main__':
    run()
    
    

