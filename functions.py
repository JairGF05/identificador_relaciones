from graphviz import Digraph
from graph2 import *

def orden_o_equivalencia(Conjunto,Relación,elementosAB):
    print(print_parcial_order_relation(Conjunto, Relación, elementosAB))
    print("")
    if (is_equivalence_relation(Conjunto,Relación)):
        print(print_equivalence_relation(Conjunto,Relación))
        draw_graph(Relación)
    if (is_parcial_order_relation(Conjunto,Relación)):
        print("########## Reticula: ##########")
        elementosAB = [2,9] #Conjunto para determinar cotas inferiores y superiores 
        if (is_parcial_order_relation(Conjunto,Relación)):
            print_maxima_cota_inferior(Conjunto,elementosAB)
            print_minima_cota_superior(Conjunto,elementosAB)
            print_is_lattice(Conjunto,elementosAB)

def comprobar_relaciones(Relación,Conjunto):
    print("########## La relación es: ##########")
    print("Reflexiva: ", "Si" if is_reflexive(Relación,Conjunto) else "No")
    print("Simétrica: ", "Si" if is_symmetric(Relación) else "No")
    print("Antisimétrica: ", "Si" if is_antisymmetric(Relación) else "No")
    print("Transitiva: ", "Si" if  is_transitive(Relación) else "No")
    print("Relación de equivalencia: ", "Si" if is_equivalence_relation(Conjunto,Relación) else "No")
    print("Relación de orden parcial: ", "Si" if is_parcial_order_relation(Conjunto, Relación) else "No")
    print("")
    print("########## Justificación: ##########")
    print(print_reflexive(Relación,Conjunto))
    print(print_symmetric(Relación))
    print(print_transitive(Relación))

def print_is_lattice(poset,conjunto):
    cs = cotas_superiores(poset,conjunto)
    ci = cotas_inferiores(poset,conjunto)
    if cs:
        if ci:
            print("Es reticula")
        else:
          print("No es reticula, porque no tiene cotas inferiores")  
    else:
        print("No es reticula, porque no tiene cotas superiores")
        
def print_minima_cota_superior(poset, conjunto):
    cs = cotas_superiores(poset,conjunto)
    if cs:
        print("Cotas superiores: " ,cs)
        mcs = minima_cota_superior(cs)
        print ("Minima cota superior: ",mcs)

def print_maxima_cota_inferior(poset, conjunto):
    ci = cotas_inferiores(poset,conjunto)
    if ci:
        print("Cotas inferiores: " ,ci)
        mci = maxima_cota_inferior(ci)
        print ("Maxima cota inferior: ",mci)

def cotas_superiores(poset,conjunto):
    cs = []
    for number in poset:
        isCotaSuperior = True
        for element in conjunto:
            if (number > element):
                if (number % element != 0):
                    isCotaSuperior = False
            else:
                isCotaSuperior = False
        if (isCotaSuperior):
            cs.append(number)
            isCotaSuperior = True
    return cs

def cotas_inferiores(poset,conjunto):
    ci = []
    for number in poset:
        isCotaInferior = True
        for element in conjunto:
            if (number < element):
                if (element % number != 0):
                    isCotaInferior = False
            else:
                isCotaInferior = False
        if (isCotaInferior):
            ci.append(number)
            isCotaInferior = True
    return ci

def minima_cota_superior(cotas_superiores):
    return cotas_superiores[0]

def maxima_cota_inferior(cotas_inferiores):
    return cotas_inferiores[len(cotas_inferiores)- 1]


def transitive_missing_elements(relation):
    missingElements = []
    for a,b in relation:
        for c,d in relation:
            if b == c and ((a,d) not in relation):
                missingElements.append((a,d))
                #print (a,b),(c,d) # solo para probar
    return missingElements

def is_transitive(relation):
    if (transitive_missing_elements(relation)):
        return False
    else:
        return True

def print_transitive(relation):
    missingElements = transitive_missing_elements(relation)
    if (missingElements):
        if (len(transitive_missing_elements(relation)) > 1):
            return "Hace faltan estos pares para que la relación sea transitiva:" + str(missingElements)
        else:
            return "Hace falta este par para que la relación sea transitiva" + str(missingElements)
    else:
        return "La relación es transitiva, para todos los pares (a,b) y (b,c) existe un par (a,c)"

def is_reflexive(relation, set):
    if (reflexive_missing_elements(relation, set)):
        return False
    else:
        return True

def print_reflexive(relation, set):
    """Returns message if is reflexive or not"""
    missingElements = reflexive_missing_elements(relation, set)
    reflexive_pairs = []
    if (missingElements):
        return "La relación no es reflexiva, porque faltan los siguientes pares: " + str(missingElements)
    else:
        for element in set:
            reflexive_pairs.append("("+str(element)+","+ str (element)+")")
        return "La relacion es reflexiva, porque los siguientes pares estan incluidos:" + str(reflexive_pairs)

def reflexive_missing_elements(relation, set):
    """Returns missing elements to a reflexive relation"""
    missingElements = []
    for element in set:
        if (element, element) not in relation:
            missingElements.append((element,element))
    return missingElements

def is_symmetric(Relation):
    if (symmetric_missing_elements(Relation)):
        return False
    else:
        return True

def print_symmetric(Relation):
    """Returns message if is symmetric or not"""
    missingElements = symmetric_missing_elements(Relation)
    result = ""
    if (missingElements):
        if (len(missingElements) > 1):
            result = result + "La relación no es simetrica porque hacen falta los pares : " + str(missingElements) +'\n'
        else:
            result = result + "La relación no es simetrica porque hacen falta el par : " + str(missingElements) +'\n'
        if (is_antisymmetric(Relation)) :
            result = result + "La relación es antisimétrica "
    else:
        result = result + '\n'"La relación es simetrica para cada par (a,b) existe un par (b,a)" +'\n' + "Por lo tanto la relación no es antisimétrica ni asimétrica"
    return result

    
def symmetric_missing_elements(Relation):
    """Returns missing elements to a symmetric relation"""
    aux =[]
    for tup in Relation:
        if not tup[::-1] in Relation:
            aux.append(tup[::-1])
    return aux


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

def print_equivalence_relation(set, relation):
    if (is_reflexive(relation, set) == True) and (is_symmetric(relation) == True) and (is_transitive(relation) == True):
        print_partitions_classes_equivalence(set, relation)
        return "Las relación es reflexiva, simétrica y transitiva por lo tanto es de equivalencia."
    result = "La relación no es "
    if (is_transitive(relation) == False):
        result = result + "transitiva, "
    if (is_symmetric(relation) == False):
        result = result + "simétrica, "
    if (is_reflexive(relation, set) == False):
        result = result + "reflexiva, "
    return result + "por lo tanto no es de equivalencia"

def print_parcial_order_relation(set, relation,conjunto):
    if (is_parcial_order_relation(set,relation)):
        return "Las relación es reflexiva, antisimétrica y transitiva por lo tanto es de orden parcial"
    result = "La relación no es "
    if (is_transitive(relation) == False):
        result = result + "transitiva, "
    if (is_antisymmetric(relation) == False):
        result = result + "antisimétrica, "
    if (is_reflexive(relation, set) == False):
        result = result + "reflexiva, "
    return result + "por lo tanto no es de orden parcial"

def print_partitions_classes_equivalence(set, relation):
    print ("Las clases de equivalencia son: ")
    partitions = []
    classes = []
    for element in set:
        for pair in relation:
            if element in pair:
                for x in pair:
                    if (x not in classes):
                        classes.append(x)
        print ("["+ str(element) +"] = " + "{"+ str(classes) + "}")
        classes = order(classes)
        if (classes not in partitions):
            partitions.append(classes)
        classes = []
    print("Las particiones son:")
    print(partitions)


def order(vector):
    for i in range(1, len(vector)):
        x = vector[i]
        j = i - 1
        while(x < vector[j] and j >= 1):     
            vector[j + 1] = vector[j]
            j = j - 1
        if vector[j] <= x:
            vector[j + 1] = x
        else:
            vector[j + 1] = vector[j]
            vector[j] = x
    return vector

            
        

