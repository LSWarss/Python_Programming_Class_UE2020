import csv
import datetime
from Assignment_2_3_4 import Months

"""
    U»ytkownik proszony jest o podanie formatu danych u»ywaj¡c liter y, m oraz d.
    Przykaadowe formaty to: yyyy.mm.dd, yyyy/mm/dd, dd:mm:yyyy, dd:mm:yy (gdzie
    yy to dwie ostatnie cyfry roku) i tak dalej. Nale»y napisa¢ funkcj¦, która konwertuje
    dat¦ z biblioteki timedate na format podany przez u»ytkownika. Przykaadowo:
    """

f = open("src/data/sesjaEgzaminacyjna.csv")

def fitTheFormat(format,date):
    formatedDate = ''
    yearsAdded = False
    monthsAdded = False
    daysAdded = False
    formatSpacialSign = ''
    if type(date) is datetime:
        print("Type of date is datetime")
    if type(date) is str:
        print("Type of date is str")
        date = date.split()
        for i in format:
            if(i != 'd' and i != 'm' and i != 'y'):
                formatSpacialSign = i
                print(f'Special format sign is: {formatSpacialSign}')
                break
        print(date)
    
    for i in range(len(format)-1):
        if(format[i] == 'd' and format[i + 1] == 'd' and daysAdded == False):
            formatedDate = formatedDate + date[0] + formatSpacialSign
            daysAdded = True
        if(format[i] == 'm' and format[i + 1] == 'm' and monthsAdded == False):
            formatedDate = formatedDate + "0" + date[1] + formatSpacialSign
            monthsAdded = True
        if(format[i] == 'y' and format[i:i+3]=="yyy" and yearsAdded == False):
            formatedDate = formatedDate + date[2] + formatSpacialSign
            yearsAdded = True
        elif(format[i] == 'y' and format[i + 1] == 'y' and yearsAdded == False):
            formatedDate = formatedDate + date[2][-2:] + formatSpacialSign
            yearsAdded = True
    print(formatedDate)

def formatDate(date):
    for month in Months:
        if(date[3:6] == month.name):
            date = date.replace(month.name, str(month.value))
    return date

fitTheFormat("yyyy:dd:mm",
formatDate("02 Feb 2021"))