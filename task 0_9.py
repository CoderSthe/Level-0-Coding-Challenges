# This function takes in a string and prints out all the vowels

def vowel_finder(user_string):
    vowels = set([each for each in user_string if each in "aeiou"])
    print("Vowels found in string: ", ', '.join(vowels))

string = input("Enter a string: ").lower()

vowel_finder(string)