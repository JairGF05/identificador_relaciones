# this program raises a set to the power n
#set = [(2,1),(2,3),(3,1),(3,4),(4,1),(4,3)]
set = [(1,2),(2,1),(2,3),(3,4),(4,1)]
unionsets = [(1,2),(2,1),(2,3),(3,4),(4,1)]
showunion = False
n = 7
print("R^1 =")
print(set)
rn = set
temparray = []
for i in range(1,n):
    for y in range(0,len(set)):
        pair = set[y]
        for j in range(0,len(rn)):
            rn_pair = rn[j]
            if pair[1] == rn_pair[0]:
                temparray.append((pair[0],rn_pair[1]))
    
# remove duplicate
    auxarray = []
    for r1 in range(0,len(temparray)):
        foundelement = False
        for r2 in range(0,len(auxarray)):
            if (temparray[r1] == auxarray[r2]):
                foundelement = True
        if (not foundelement):
            auxarray.append(temparray[r1])


    rn = auxarray
    temparray = []
# this part add union sets
    for t1 in range(0,len(rn)):
        foundpair = False
        for t2 in range(0,len(unionsets)):
            if (rn[t1] == unionsets[t2]):
                foundpair = True
        if (not foundpair):
            unionsets.append(rn[t1])

    print("R^"+ str(i + 1) +" =")
    print(rn)
    if (showunion):
        print("the union of elements is: ")
        print(unionsets)
