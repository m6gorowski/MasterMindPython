def koloruj(przyjete,poprawnosc):
    licznik = 0
    for i in range(0,4): #zmiana koloru
        znak = poprawnosc[i]
        if znak == '0':
            print("\033[31m", end="") #czerwony
        elif znak =='1':
            print("\033[32m", end="") #zielony
            licznik+=1
        else:
            print("\033[33m", end="") # żółty
        print(przyjete[i],"\033[0m", end="") #wyświetla i czyści kolor
    print()
    if licznik==4:
        return True
    return False


def wyswietl():
    rozwiazanie = 0
    print(f"{"MasterMind":-^48}")
    los = "1234" # createCombination()
    for i in range(1,8):
        print(f"[{i}] ", end="")
        urzytkownik = input("podaj: ")
        if len(urzytkownik)==4:
            ocena="0012" # ocena(los,urzytkownik)
            if koloruj(urzytkownik,ocena):
                rozwiazanie = i
                break
        else:
            print("\033[31m podano złą długość \033[0m")
    if rozwiazanie!=0:
        print(f"\033[32mBrawo udało ci się rozwiązać w: {rozwiazanie} próboach \033[0m")
    else:
        print("niestety nie udało się rozwiązać, oto poprawny wynik: ",los)
