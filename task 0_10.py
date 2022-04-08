def same_letters(first_string, second_string):
    common_letters = ""
    for a in set(first_string):
        if a in second_string:
            common_letters += a
    print("Common characters: ", ', '.join(common_letters))


same_letters("Tomatoes", "Potatoes")