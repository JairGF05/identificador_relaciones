from graphviz import Digraph

# g = Digraph('G', filename='hello.gv')
# g.edge('Hello', 'World')
# g.view()


def draw_graph(relation):
    
    g = Digraph('G', filename='grafo.gv')
    for a, b in relation:
        g.edge(str(a), str(b))
    g.view()


def run():
    
    relation = [('a', 'a'), ('a', 'd'), ('d', 'd'), ('d', 'a'),
                  ('b', 'b'), ('b', 'c'), ('c', 'c'), ('c', 'b')]
    relation2 = [(1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (20, 20), (1, 2)]
    draw_graph(relation2)

if __name__ == '__main__':
     run()
