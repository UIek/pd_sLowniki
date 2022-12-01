kl_1h = [
    {
    'imie':'Henryka',
    'nazwisko':'Matejko',
    'rocznik':666
    },
    {
    'imie':'Ziemowit',
    'nazwisko':'Kotecki',
    'rocznik':2137
    },
    {
    'imie':'Damroka',
    'nazwisko':'Jelonek',
    'rocznik':1234
    }
]
while True:
    print('a - dodaj ucznia')
    print('b - usuń ucznia')
    print('c - zmień informacje o uczniu')
    inp = input('co chcesz zrobić?').lower()

    if inp == 'a':
        nowy_uczen = {
            'imie':input('podaj imie:'),
            'nazwisko':input('podaj nazwisko:'),
            'rocznik':int(input('podaj rok urodzenia:'))
        }
        kl_1h.append(nowy_uczen)
    elif inp == 'b':
        nr = int(input('podaj numer ucznia którego chcesz usunać:'))
        kl_1h.pop(nr-1)
    elif inp == 'c':
        nr = int(input('podaj numer ucnia:'))
        klucz = input('co chcesz zmienić?')
        kl_1h[nr-1][klucz] = input('nowa wartość - ')
    else:
        break
