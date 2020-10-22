"""
Napisz funkcj¦ wypisuj¡c¡ co drugi element listy w odwrotnej kolejno±ci. Mo»na
u»y¢ metod wbudowanych dla list.
"""

def reversedSecond(list):
    list.reverse()
    for i in range(len(list)): 
        if i % 2 == 0:
            print(list[i])


testList = ["a","b","c","d","e"]

reversedSecond(testList)