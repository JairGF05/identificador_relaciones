def is_transitive(relation):
    for a,b in relation:
        for c,d in relation:
            if b == c and ((a,d) not in relation):
                #print (a,b),(c,d) # solo para probar
                return False
    return True


def is_reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        if (a, a) not in R:
            return False
    return True

def is_symmetric(Relation):
    if all(tup[::-1] in Relation for tup in Relation):
        return True  


    return False


def is_antisymmetric(relation):
    for a, b in relation:
        if (a,b) in relation and (b,a) in relation and a != b:
            return False
    return True

def is_equivalence_relation(set, relation):
    if (is_reflexive(relation, set) == True) and (is_symmetric(relation) == True) and (is_transitive(relation) == True):
        return True
    
    return False


def is_parcial_order_relation(set, relation):
    if (is_reflexive(relation, set) == True) and (is_antisymmetric(relation) == True) and (is_transitive(relation) == True):
        return True
    
    return False
    