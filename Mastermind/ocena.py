# dlugosc 4
def ocena(kod,dane):
    # pusta lista do zapisywania wynikow
    wynik = ['','','','']
    # zamiana danych wejsciowych string na tablice
    kod=list(kod)
    dane=list(dane)
    # Mozliwe wartosci w tablicy wynik
    # 0 - nie ma tej liczby w kodzie
    # 1 - liczba znajduje sie pod tym samym indeksem w kodzie
    # 2 - liczba znajduje sie pod innym indeksem w kodzie
    
    # sprawdzenie dokładnych trafień
    for i in range(4):
        if dane[i]==kod[i]:
            wynik[i] = '1'
            kod[i]=''
        else:
            wynik[i] = '0'
        
    # sprawdzanie wystepowania cyfry w innym miejscu w kodzie    
    for i in range(4):
        # pomija pozycje, które zostały już odgadnięte
        if wynik[i]!='0':
            continue
        # sprawdza, czy podana liczba występuje na innym miejscu w kodzie
        for j in range(4):
            if dane[i]==kod[j]:
                wynik[i]='2'
                kod[j]=''
                break
    print(dane)
    print(kod)
    return wynik

print(ocena(str(1234),str(1234)))
