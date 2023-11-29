# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Initialize an empty string to store uneaten letters
word_without_vowels = ""

# Iterate through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter in "AEIOU":
        # If it's a vowel, skip to the next iteration using continue
        continue
    else:
        # If it's not a vowel, add it to the word_without_vowels string
        word_without_vowels += letter

# Print the word without vowels
print("Word without vowels:", word_without_vowels)
