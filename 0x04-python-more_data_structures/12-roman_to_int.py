#!/usr/bin/python3
def roman_value(character):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return roman_dict.get(character, 0)

def next_value(roman_string, index):
    if index + 1 < len(roman_string):
        return roman_value(roman_string[index + 1])
    else:
        return 0

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not all(char.upper() in 'IVXLCDM' for char in roman_string):
        return 0

    result = 0
    for index, character in enumerate(roman_string):
        current_value = roman_value(character)
        next_value_ = next_value(roman_string, index)

        if current_value >= next_value_:
            result += current_value
        else:
            result += (next_value_ - current_value)

    return result
