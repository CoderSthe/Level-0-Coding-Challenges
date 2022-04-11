def vowel_finder(user_string):
    vowels = set([each for each in user_string if each in "aeiouAEIOU"])
    print("Vowels found in string: ", ', '.join(vowels).lower())


vowel_finder("Umuzi")
