from functions import *

##El conjunto a analizar es:
#Conjunto = [2,4,6,9,12,18,27,36,48,60,72]


#Prueba de que no cumple ningun orden
Conjunto = [0,1,2,3]
Relación =[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,2),(3,3)]

#Prueba relacion de equivalencia
#Conjunto =['a','b','c','d']
#Relación =[('a','a'),('a','d'),('d','d'),('d','a'),('b','b'),('b','c'),('c','c'),('c','b')]


#Prueba de Orden parcial
#Conjunto = [2,4,6,9,12,18,27,36,48,60,72]
#Relación = [(2, 2), (4,4), (6,6),(9,9),(12,12), (18,18), (27,27),(36,36), (48,48), (60,60), (72,72), (72,2)]

#tambien es de orden parcial
# Relación = [(2,2),(2,4),(2,6),(2,12),(2,18),(2,36),(2,48),(2,60),(2,72),(4,4),(4,12),(4,36),(4,48), 
# (4,60),(4,72),(6,6),(6,12),(6,18),(6,36),(6,48),(6,60),(6,72),(9,9),(9,18),(9,36),(9,72),(12,12),(12,36), 
# (12,48),(12,60),(12,72),(18,18),(18,36),(18,72),(27,27),(36,36),(36,72),(48,48),(60,60),(72,72)]


comprobar_relaciones(Relación,Conjunto)
## Se imprimen los resultados si la relación es de orden o de equivalencia
## Si la relación es de equivalencia se obtendra las cotas de los elementos AB
elementosAB = [2,9]
orden_o_equivalencia(Conjunto,Relación,elementosAB)
