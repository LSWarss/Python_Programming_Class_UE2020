"""
Napisz waasn¡ metod¦ sort() umo»liwiaj¡c¡ sortowanie listy tak»e w sytuacji, kiedy
na li±cie znajduj¡ si¦ liczby i aa«cuchy. Zakaadamy, »e wszystkie elementy liczbowe
znajduj¡ si¦ na pocz¡tku, a aa«cuchy znajduj¡ si¦ w dalszej cz¦±ci listy - posortowane
saownikowo.
"""

def mixSort(array):
    stringList = []
    numbersList = []
    for i in array:
        if type(i) is str:
            stringList.append(i)
        else:
            numbersList.append(i)
    length = len(array)
    stringList.sort()
    numbersList.sort()
    array.clear()

    for i in range(length):
        if i < len(numbersList):
            array.append(numbersList[i])
        else:
            array.append(stringList[i - len(numbersList)])
    return array

print(mixSort(["lal", "bala",1,3,4,5,7,"Mara","dola",True]))
