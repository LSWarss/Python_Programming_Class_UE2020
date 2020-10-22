"""
Dane s¡ dwie listy. Napisz metod¦ Merge, która poa¡czy listy tak, »eby elementy
pojawiaay si¦ na zmian¦.
"""

import random

# TODO: Correct this function or create new one while I've created this one, the way it only takes the longest list length opposite to just taking sum of the lengths

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

print(mergeOnSecond([1,2,3,4,5],[6,7,8,9,10]))