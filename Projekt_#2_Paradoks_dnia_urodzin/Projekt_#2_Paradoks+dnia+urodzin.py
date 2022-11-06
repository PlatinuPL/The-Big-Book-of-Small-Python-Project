import datetime, random

def getBirthdays(numberOfBirthdays):
    '''Zwraca listę losowych dni urodzin'''
    birthdays = []
    for i in range(numberOfBirthdays):
        # Rok nie jest ważny dla naszej symulacji, jeśli tylko dni urodzin wypadają w tym samym roku
        startOfYear = datetime.date(2001, 1, 1)

        #Wylosuj dzień w roku
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    '''Zwraca datę urodzin, która pojawia się więcej niż raz w liście urodzin'''
    matches = []
    if len(birthdays) ==len(set(birthdays)):
        return None  # Wszystkie dni są unikatowe, dlatego zwróć None
    #Porównaj każdę urodziny z pozostałymi:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Zwróć takie same urodziny


# Wyświetl wstep:
print('''Paradoks dnia urodzin,

Paradoks dnia urodzin pokazuje, że w grupie N osób szansa,
że dwie osoby mają urodziny w tym samym dniu, jest zaskakująco duża.
Ten program wykorzystuje metodę Monte Carlo (czyli powtarzalne losowe
symulacje), by ustalić to prawdopodobieństwo.

(To tak naprawdę nie jest paradoks, tylko zaskakujący wynik.)''')

#Deklaracja krotki z miesiącami:
MONTHS = ('Sty', "Lut", 'Mar', 'Kwi', "Maj", 'Cze',
          'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', "Gru")
while True: #Pytaj dopóki urzytkownik nie poda odpowiedniej wartości
    print("Ile urodzin powieniem wygenerować? (Maks. 100)")
    response = input(">")
    if response.isdecimal() and (0<int(response) <=100):
        numBDay = int(response)
        break #użytkownik podał odpowiednią wartość
print()

# Wygeneruj i wyświetl dni urodzin:
print("Oto", numBDay, "dni urodzin:")
birthdays = getBirthdays(numBDay)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Po pierwszym dniu urodzin wyświetl przecinek
        print(", ", end ="")
        monthNAME = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthNAME, birthday.day)
        print(dateText, end ="")
print()
print()

# Sprawdź czy są takie same dni urodzin
match = getMatch(birthdays)
print("Match:", match)
# Wyświetl wyniki
print("W tej symulacji, ", end="")
if match != None:
    monthNAME = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthNAME, match.day)
    print("Kilka osób ma urodziny", dateText)
else:
    print("Nie ma takich samych dni urodzin")
print()

# Przeprowadzono 100 000 symulacji
print("Generowanie ", numBDay, "losowych dni urodzin 100 000 razy...")
input('Naciśnij Enter, aby rozpocząć...')

print("Przeprowadźmy kolejnych 100 000 symulacji")
simMatch = 0 # Liczba symulacji w których wystąpiły te same dni urodzin
for i in range(100_000):
    #Wyświetlanie postępu co 10 000 symulacji
    if i % 10_000 == 0:
        print(i, "przeprowadzonych symulacji...")
    birthdays = getBirthdays(numBDay)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100 000 przprowadzonych symulacji")

# Wyświetlanie wyników symulacji:
probability = round(simMatch / 100_000 * 100,2)
print("Ze 100 000 symulacji dla", numBDay, "osób, ten sam")
print("dzień urodzin wystąpił", simMatch, "razy. Oznacza to,")
print("że dla", numBDay, "ludzi istnieje",probability, '% szans, iż')
print("dwie lub więcej osób będzie miało urodziny w tym samym dniu")
print("To prawdopodonie więcej, niż przypuszczałeś!")

