#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    numero = 0
    rom_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in roman_string:
        numero += rom_dic.get(i, 0)
    s_rom = {"CM": -200, "CD": -200, "XC": -20, "XL": -20, "IX": -2, "IV": -2}
    alph = ""
    for i in range(0, len(roman_string) - 1):
        alph = roman_string[i] + roman_string[i + 1]
        if alph in s_rom:
            numero += s_rom[alph]
    return numero
