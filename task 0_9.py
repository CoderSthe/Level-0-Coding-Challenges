def vowel_finder(user_string):
    vowels = set([each for each in user_string if each in "aeiou"])
    print("Vowels found in string: ", ', '.join(vowels))


vowel_finder("Umuzi")