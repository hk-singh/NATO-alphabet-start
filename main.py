import pandas
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
flag = 0

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_alphabet = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while not flag:
    try:
        user_input = input("Enter a word: \n").upper()
        phonetic_code = [nato_alphabet[letter] for letter in user_input]
        print(phonetic_code)
        flag = 1
    except KeyError:
        print("Please enter only words, no numbers or special characters")

