"""
Wygeneruj losow¡ list¦ o wielko±ci zadanej przez u»ytkownika. Lista mo»e zawiera¢
aa«cuchy, zmienne typu float, int oraz warto±ci boolowskie. Nast¦pnie napisz metod¦,
która przyjmuje tak¡ list¦ jako parametr i dzieli j¡ na 4 nowe listy zawieraj¡ce osobno
elementy string, float, int oraz boolean.
"""

import random, string

def randomEverythingListGenerator(arrayLenght):
    randomEverythingItemsList = []
    for _ in range(arrayLenght):
        randomTypePicker = round(random.random(),2)
        if randomTypePicker >= 0.00 and randomTypePicker < 0.25:
            randomEverythingItemsList.append(get_random_string(random.randint(0,arrayLenght)))
        elif randomTypePicker >= 0.25 and randomTypePicker < 0.5:
            randomEverythingItemsList.append(round(random.random(),2))
        elif randomTypePicker >= 0.5 and randomTypePicker < 0.75:
            randomEverythingItemsList.append(random.randint(0, arrayLenght))
        else:
            randomEverythingItemsList.append(bool(random.randint(0,1)))
    return randomEverythingItemsList      

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def giveMeSeparation(array):
    floatArray = []
    intArray = []
    stringsArray = []
    boolArray = []
    for i in array:
        if type(i) is float:
            floatArray.append(i)
        elif type(i) is bool:
            boolArray.append(i)
        elif type(i) is int:
            intArray.append(i)
        else:
            stringsArray.append(i)
    print(f"Floats array: {floatArray} \n" +
        f"Strings array: {stringsArray} \n" +
        f"Ints array: {intArray} \n" +
        f"Bools array: {boolArray} ")

giveMeSeparation(randomEverythingListGenerator(10))