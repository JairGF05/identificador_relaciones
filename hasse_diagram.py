
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
    # for a,b in relation:
    #     for c,d in relation:
    #         if b == c and (a,d) in relation:
    #             relation.remove((a,d))     
    
    #removiendo transitivos 2
    for a,b in relation:
        for c,d in relation:
            if b == c and ((a,d) in relation):
                relation.remove((a,d))
                    
    #removiendo reflexivos
    for element in set:
        if (element, element) in relation:
            relation.remove((element,element))
    print('relacion sin transitividad y sin reflexivos')
    print(relation)
    
    #relation = [(1, 2),(1,3),(2,6),(2, 12),(3,6), (3, 12), (6, 24),(6,36),(12,24),(12, 36)]
    
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
    
    
    #set = ['a','b','c']
    #relation = [('a','a'),('a','b'),('a','c'),('b','b'),('b','c'),('c','c')]
    
    #set = ['a','b','c','d','e']
    #relation = [('a','a'),('a','b'),('a','c'),('a','d'),('a','e'),('b','b'),('b','c'),('b','e'),('c','c'),('c','e'),('d','d'),('d','e'),('e','e')]
    
    # set =[1,2,3,5,6,10,15,30]
    # relation = [(1,1),(1,2),(1,3),(1,5),(1,6),(1,10),(1,15),(1,30),
    #             (2,2),(2,6),(2,10),(2,30),(3,3),(3,6),(3,15),(3,30),
    #             (5,5),(5,10),(5,15),(5,30),(6,6),(6,30),(10,10),(10,30),
    #             (15,15),(15,30),(30,30)] 
    
    set = [1,2,3,6,12,24,36,48]
    relation = [(1,1),(1,2),(1,3),(1,6),(1,12),(1,24),(1,36),(1,48),
                (2,2),(2,6),(2,12),(2,24),(2,36),(2,48),
                (3,3),(3,6),(3,12),(3,24),(3,36),(3,48),
                (6,6),(6,12),(6,24),(6,36),(6,48),
                (12,12),(12,24),(12,36),(12,48),(24,24),
                (24,48),(36,36),(48,48)]
    
   
    draw_hasse(relation,set)
    
    

if __name__ == '__main__':
    run()
    
    

