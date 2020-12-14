import sqlite3
import datetime

connector = sqlite3.connect("studenci.db")
c = connector.cursor()

c.execute('''CREATE TABLE osoby (
    nrAlbumu INTEGER NOT NULL PRIMARY KEY,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    rok_studiow DATE timestamp,
    kierunek TEXT,
    srednia_ocen DOUBLE
);''')

c.execute('''CREATE TABLE kierunki (
    idKierunku INTEGER NOT NULL PRIMARY KEY,
    nazwa TEXT NOT NULL,
    skrot TEXT NOT NULL,
    otwarty BOOLEAN,
);''')