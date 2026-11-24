kod = ''
dane = ''
# dlugosc 4
def ocena(kod,dane):
    wynik = ''
    # 0 - nie ma
    # 1 - jest w tym miejscu
    # 2 - jest w innym
    for i in range(0,4):
        for j in range(0,4):
            # sprawdza i-ty znak w calym napisie
            duplikaty = 0
            if dane[i]==kod[j]:
                if duplikaty>1:
                    wynik =+ wynik + '2'
                else:
                    wynik = wynik + '1'
                duplikaty += 1
            else:
                wynik = wynik + '0'
