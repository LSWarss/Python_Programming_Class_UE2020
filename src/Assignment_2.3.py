"""
3. Do zadania doałczony zostaa plik csv z rzeczywistymi notowaniami spółki indekso-
wanej na giełdzie. Plik skaada się z daty oraz zmiany procentowej w cenie instru-
mentu względem poprzedniego odczytu. Bardzo często w zestawieniach nansowych
przedstawia się zwroty za ostatni miesiąc. Nalezy odczytać dane, nastapnie wyzna-
czy¢ średnił dla kazdego z miesiłca i zapisać średnie zmiany miesięczne w osobnym
pliku. Przykładowo dla danych:
• Apr 29 2018 : 0.28
• Apr 22 2018 : 12.12
• Apr 15 2018 : -2.67
• Apr 08 2018 : -4.74
• Apr 01 2018 : -5.60
Nale»y do nowego pliku csv wpisa¢: Apr 2018 : -0.12 (czyli 0.28 +12.12 - 2.67 - 4.74
- 5.60 podzielone na 5 i zaokr¡glone do dwóch miejsc po przecinku).
"""
import csv
import pprint as pp
import numpy as np
import pandas as pd
import enum

class Months(enum.Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


def formatData(fileName):
    """Simple data formatting function, to format given data for something computer readable

    Args:
        fileName (csv file): Specific csv file given in assignment, with Company's stock price indexed

    Returns:
        Numpy array : Formatted numpy array 
    """
    file = open(fileName)
    data = []
    formatedData = []
    for row in csv.reader(file):
        data.append(str(row))
    
    # Formating loop
    for row in data:
        placeholder = row
        placeholder = placeholder.replace("['", '')
        placeholder = placeholder.replace("']", '')
        placeholder = placeholder.replace(' : ', ' ')
        placeholder = placeholder.split(' ')
        formatedData.append(placeholder)

    numpyFormattedArray = np.array(formatedData)
    return numpyFormattedArray

def lastMonthsRetun(array):
    """Function taking the formatter data array and then converting it to dataFrame, with aim to find returns data we are interested in

    Args:
        array (Numpy array): Numpy array
    """
    df = pd.DataFrame(array)
    placeholderArray = []
    df.columns=['Month','Day','Year','Return']
    df['Return'] = pd.to_numeric(df['Return'])
    for year in df['Year'].unique():
        for month in Months:
            returnsSumForSpecificMonth = df.loc[(df.Month == month.name) & (df.Year == year)]
            # print(returnsSumForSpecificMonth['Return'])
            placeholderArray.append([month.name, year, ":", calculateReturn(returnsSumForSpecificMonth['Return'])])

    pp.pprint(placeholderArray)
    file = open('returns.csv', 'w', newline='')

    for row in placeholderArray:
        csv.writer(file).writerow(row)
    file.close()

def calculateReturn(arrayOfReturns):
    """Simple calculation of returns function to make code more readable

    Args:
        arrayOfReturns ([Float]): Array of retuns from specific month

    Returns:
        Float : Returns sum devided by 5
    """
    return round((sum(arrayOfReturns)/5),2)


lastMonthsRetun(formatData("/Users/lukaszstachnik/Workspace/Python_Programming_Class_UE2020/src/data/APC Historical Data.csv"))
