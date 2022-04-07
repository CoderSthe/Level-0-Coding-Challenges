# This function takes two strings as input and outputs the common characters/letters that they share

def same_letters(first_string, second_string):
    common_letters = ""
    for a in set(first_string):
        if a in second_string:
            common_letters += a
    print("Common characters: ", ', '.join(common_letters))

string_1 = input("Enter the first string: ").lower()
string_2 = input("Enter the second string: ").lower()

same_letters(string_1, string_2)