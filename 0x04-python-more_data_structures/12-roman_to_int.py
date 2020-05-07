#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not  roman_string or type(roman_string) != str:
        return 0

    numeric = 0

    for letter, index in zip(roman_string, range(len(roman_string))):

        prev_letter = roman_string[index - 1]
        if roman[letter] > roman[prev_letter]:
                numeric += roman[letter] - 2 * roman[prev_letter]
        else:
            numeric += roman[letter]

    return numeric
