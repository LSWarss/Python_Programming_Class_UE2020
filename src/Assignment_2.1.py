"""
1. Napisz funkcje zliczająca liczbe znaków w pliku.
"""

import csv
import magic

def countCharactersInCSV(fileName):
    """Function takes file and opens it, if the file is csv then 
    it counts characters in it

    Args:
        fileName ([String]): [File name we want to count characters in]

    Returns:
        [Int]: [Number of characters in the file]
    """
    file = open(fileName)
    charactersCount = 0
    if(magic.from_file(fileName,mime=True) == 'text/plain'):
        for row in csv.reader(file):
            charactersCount += len(row)
    else: 
        return 0
    file.close()
    return charactersCount

print(countCharactersInCSV("./data/APC Historical Data.csv"))
print(countCharactersInCSV("./data/testNonTestFile.py"))