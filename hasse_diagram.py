
from graphviz import Graph
from functions import *

#crear un grafo vacio
#g = nx.Graph()

def draw_hasse(relation, set):
    #se usa graph ya que sera no dirigido
    g = Graph('G', filename='hasse.gv')
    
    #convertir los nodos a puntos
    #g.attr('node',shape = 'point')
    
    #hace el grafo mas pequeño
    g.attr(size = '.5')
    #modificando el tamaño de los nodos
    g.attr('node', width = '.2', height ='.2')
    
    print('relacion original')
    print(relation)
   
    
    #removiendo transitivos
    for a,b in relation:
        for c,d in relation:
            #if (a,b) in relation and (b,c) in relation and (a,c) in relation:
            if c == b and (c,d)in relation and (a,d) in relation:
            #if b == c and ([a,d]  in relation):
                relation.remove((a,d))     
    # print('relacion sin transitividad')
    # print(relation)   
    
    #removiendo reflexivos
    for element in set:
        if (element, element) in relation:
            relation.remove((element,element))
    print('relacion sin transitividad y sin reflexivos')
    print(relation)
    
    #invirtiendo lista de nodos
    new_rel = []
    for a,b in reversed(relation) :
       new_rel.append((b,a))
       
    print('relacion en reversa')   
    print(new_rel)
    
    
    # dibujando grafo
    for a,b in new_rel:
        g.edge(str(a), str(b))
    g.view()
    
    
        
        

    
   
    
def run():
    # set = [1,2,3,4,6,12]
    # relation = [(1,1),(2,2),(3,3),(4,4),(6,6),(12,12),(1,2),(1,3),(1,4),(1,6),(1,12),(2,3),(2,4),(2,6),(2,12)
    #         ,(3,4),(3,6),(3,12),(4,6),(4,12),(6,12)]
    set = ['a','b','c']
    relation = [('a','a'),('a','b'),('a','c'),('b','b'),('b','c'),('c','c')]
    draw_hasse(relation,set)
    
    

if __name__ == '__main__':
    run()
    
    

