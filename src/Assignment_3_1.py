import csv
import pprint as pp
import datetime
from Assignment_2_3_4 import Months

    """
    Dany jest plik sesjaEgzaminacyjna.csv, w którym dane zapisane s¡ w nast¦puj¡cy
    sposób:
    • 30 Jan 2021 : Programowanie w Assembler
    • 02 Feb 2021 : Algorytmika i zao»ono±¢ obliczeniowa
    • 04 Feb 2021 : Klaskanie rytmiczne
    Sprawdzaj¡c dzisiejsz¡ dat¦ nale»y ustali¢, ile egzaminów zostaao jeszcze do ko«ca
    sesji. Przykaadowo dla daty 1 stycznia 2021 wynikiem b¦dzie 3, ale dla daty 1 lutego
    2021  2.
    """

f = open("src/data/sesjaEgzaminacyjna.csv")
numberOfExams = 0

for row in csv.reader(f):
    date = str(row)[2:13]
    print(date[3:6])
    for month in Months:
        if(date[3:6] == month.name):
           print(date)
           date = date.replace(month.name, str(month.value))
    print(f"Comparing right now: {datetime.date.today()} and { datetime.datetime.strptime(date, '%d %m %Y').date()}")
    if(datetime.date.today() < datetime.datetime.strptime(date, '%d %m %Y').date()):
        numberOfExams += 1

print(numberOfExams)


