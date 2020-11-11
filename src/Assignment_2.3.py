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


def formatData(fileName):
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

    pp.pprint(formatedData)
    return formatData

#TODO: Implement function going through the formated data and calculating the returns
def lastMonthsRetun(fileName):
    formatedData = formatData(fileName)



formatData("./data/APC Historical Data.csv")
