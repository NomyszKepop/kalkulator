# Definiowanie funkcji: dodawania, mnożenia, odejmowania i dzielenia

def dodawanie (x, y):
    return x + y

def odejmowanie (x, y):
    return x - y

def mnożenie (x, y):
    return x * y

def dzielenie (x, y):
    if y == 0:
        return "Error: Nie można dzielić przez zero"
    else:
        return x / y

print("Wybierz opcje: ")
print("1-Dodawanie")
print("2-odejmowanie")
print("3-mnożenie")
print("4-dzielenie")

while True:
    # Pobieranie danych od użytkownika
    choice = input("Wpisz wybór opcji (1,2,3,4): ")

    # Pętla i sprawdzanie który jest wybór użytkownika i które zadanie ma on wykonać
    if choice in ('1', '2', '3', '4'):
        Liczba_pierwsza = float(input("Wpisz pierwszą wartość: "))
        Liczba_druga = float(input("Wpisz drugą wartość: "))

        if choice == '1':
            print(Liczba_pierwsza, "+", Liczba_druga, "=", dodawanie(Liczba_pierwsza, Liczba_druga))

        elif choice == '2':
            print(Liczba_pierwsza, "-", Liczba_druga, "=", odejmowanie(Liczba_pierwsza, Liczba_druga))

        elif choice == '3':
            print(Liczba_pierwsza, "*", Liczba_druga, "=", mnożenie(Liczba_pierwsza, Liczba_druga))

        elif choice == '4':
            print(Liczba_pierwsza, "/", Liczba_druga, "=", dzielenie(Liczba_pierwsza, Liczba_druga))
        break
    else:
        print("Nieprawidłowe dane")