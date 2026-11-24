import random

def createCombination():
    #ASCII for numbers from 0 to 9 (48 - 57)
    ASCII_lower_range = 48
    ASCII_upper_range = 57
    #Code is four characters, like '8008'
    combination = ''
    for i in range(0,4):
        #get a random ASCII value from the range
        ASCII_num = random.randint(ASCII_lower_range,ASCII_upper_range)
        #add it at the end of the combination, changing it to a chr.
        combination = combination + chr(ASCII_num)
    return combination
