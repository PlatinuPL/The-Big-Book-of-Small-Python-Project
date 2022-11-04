import random


NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bajgle, lgoiczna gra na dedukcję.
    Mam na mysli {}-cyfrową liczbę, w której nie powtarza się żadna z cyfr. Spróbuj ją odgadnąć.
    Oto wskazówki:
    Gdy mówię:          Oznacza to:
    Piko                Jedna cyfra jest poprawna, ale jest na złej pozycji
    Fermi               Jedna cyfra jest poprawna i znajduje sie w odpowiednim miejscu
    Bajgle              Żadna cyfra nie jest poprawna

    Na przykład, jeśli tajna liczba to248, a Ty podasz liczbe 843, 
    wskazówka będzie brzmieć Fermi Piko.'''.format(NUM_DIGITS))
    while True:
        secret_num = get_secret_num()
        print('Mam na myśli liczbę.')
        print('Masz {} prób, by odgadnąć, jaka to liczba.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Próba #{}: ".format(num_guesses))
                guess = input(">")
            clues = getClues(guess, secret_num)
            print(clues)
            num_guesses +=1
            
            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("Wykorzystałeś wszystkie próby.")
                print("Prawidłowa odpowiedź to: {}.".format(secret_num))
        print("Czy chcesz zagrać jeszcze raz? (tak lub nie)")
        if not input('>').lower().startswith("t"):
            break
        print("Dziękuje za grę!")

def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)


    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    if guess == secret_num:
        return "Udało się!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append('Piko')
    if len(clues) == 0:
        return "Bajgle"
    else:
        clues.sort()
        return " ".join(clues)





if __name__ == "__main__":
    main()