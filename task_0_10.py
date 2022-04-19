def same_letters(first_string, second_string):
    common_letters = ""
    for char in set(first_string.lower()):
        if char in second_string.lower():
            common_letters += char
    print("Common letters: ", ', '.join(common_letters).lower())


same_letters("TomatoeS", "PotaToeS")
