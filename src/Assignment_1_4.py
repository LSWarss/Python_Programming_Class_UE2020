"""
Dane s¡ dwie listy. Napisz metod¦ Merge, która poa¡czy listy tak, »eby elementy
pojawiaay si¦ na zmian¦.
"""

import random

def mergeOnSecond(listA, listB):
    listC = []
    if len(listA) > len(listB):
        for i in range(len(listA)):
            if i >= len(listB):
                listC.append(listA)
            else:
                if i % 2 != 0:
                    listC.append(listA[i])
                else:
                    listC.append(listB[i])
    elif len(listA) < len(listB):
        for i in range(len(listB)):
            if i >= len(listA):
                listC.append(listB)
            else:
                if i % 2 != 0:
                    listC.append(listB[i])
                else:
                    listC.append(listA[i])
    else:
        randomBool = bool(random.randint(0,1))
        if randomBool is True:
            for i in range(len(listA)):
                if i >= len(listB):
                    listC.append(listA)
                else:
                    if i % 2 != 0:
                        listC.append(listA[i])
                    else:
                        listC.append(listB[i])
        if randomBool is False:
            for i in range(len(listB)):
                if i >= len(listA):
                    listC.append(listB)
                else:
                    if i % 2 != 0:
                        listC.append(listB[i])
                    else:
                        listC.append(listA[i])
    return listC

def mergeOnSecondVersionTwo(listA, listB):
    listC = []
    iteratorA = 0
    iteratorB = 0
    for i in range(len(listA) + len(listB)):
        if i % 2 != 0:
            listC.append(listB[iteratorB])
            iteratorB += 1
        else:
            listC.append(listA[iteratorA])
            iteratorA += 1
    return listC

print(mergeOnSecond([1,2,3,4,5],[6,7,8,9,10]))
print(mergeOnSecondVersionTwo([1,2,3,4,5],[6,7,8,9,10]))