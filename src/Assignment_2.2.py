"""
2. Dany jest plik, gdzie w kazdej linii znajduje się słowo. Nalezy sprawdzic, czy dane
slowo jest palindromem, a nastepnie do pliku csv zapisac dla kazdego saowa następu-
j¡ce dane: liczba porzadkowa, słowo, wypisac wszystkie znaki znajdujace się w tym
słowie, wpisać true jezeli słowo jest palindromem i false, je»eli nie jest. Przykaad
ponizej:
• aabcbaa > 1, aabcbaa, abc, true;
• AabbaA > 2, AabbaA, Aab, true;
• alamakota > 3,alamakota, almkot, false.
"""
import csv
import pprint as pp

def isPalindrome(word):
    """[Simple function checking if word is a palindrom]

    Args:
        word ([String]): [Word we want to check if is a palindrom]

    Returns:
        [Bool]: [If is palindrom True if not False]
    """
    return word == word[::-1]

def allCharacters(word):
    """[Function look over the word looking for all character contained in it ]

    Args:
        word ([String]): [Word from which we want to exclude the characters ]

    Returns:
        [String]: [All characters contained in the word, in form of String]
    """
    charactersInWord = []
    for char in word: 
        if char in charactersInWord:
            pass
        else:
            charactersInWord.append(char)
    return ''.join(charactersInWord)

def palindromSearcher(fileName):
    """[Function checks if the word in the word list is a plaindrom and then returns it with all characters that are in it, and information if it was a palindrom 
    or not in form of CSV file]

    Args:
        fileName ([String]): [File with words list]
    """
    file = open(fileName)

    toCSVList = []
    index = 0

    for row in file:
        if isPalindrome(row.replace('\n', '')):
            toCSVList.append([index,row.replace('\n', ''),allCharacters(row.replace('\n', '')),True])
            index += 1
        else:
            toCSVList.append([index,row.replace('\n', ''),allCharacters(row.replace('\n', '')),False])
            index += 1

    file.close()
    file = open(fileName[:-4] + '.csv', 'w', newline='')

    for row in toCSVList:
        csv.writer(file).writerow(row)
    file.close()
palindromSearcher("./data/sampleWords.txt")
