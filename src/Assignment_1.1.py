"""
Przy pomocy biblioteki random wygeneruj tablice o rozmiarze podanym przez uzyt-
kownika. Tablica powinna zawierac tylko zmienne typu foat. Nastepnie wyznacz

Sredni¡ tablicy korzystajac z metody wbudowanej, a nastepnie ta sama srednia bez
metod wbudowanych. Wyznacz tez mediane listy (skorzystaj z metody sort, ale nie
uzywaj funkcji dotyczacej wyznaczania mediany).
"""

import random,statistics 

def notBuildInMedian(array):
    n = len(array)
    s = sorted(array)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def randomNumbersArray(arrayLenght):
    random_number_array = []

    for _ in range(arrayLenght):
        random_float = round(random.uniform(0.0, 100.0), 2)
        random_number_array.append(random_float)
    
    print(f"Random numbers array: {random_number_array}")
    print(f"Mean with build-in function: {round(statistics.mean(random_number_array),2)}")
    print(f"Mean without build-in function: {round(sum(random_number_array)/arrayLenght,2)}")
    print(f"Median with build-in function: {round(statistics.median(random_number_array),2)}")
    print(f"Median without build-in function: {round(notBuildInMedian(random_number_array),2)}")

randomNumbersArray(10)