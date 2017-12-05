from random import randint

# A list of valid characters.
valid_char = "abcdefghijklmnopqrstuvwxyz"

# A function to read all lines from a file.
def read_lines(filename):
    # Open the file in read mode for reading the content of the file.
    file = open(filename, "r")

    # Create a list to store all the lines in the file.
    lines = []

    # Read all lines from the file.
    for line in file:
        line = line.rstrip('\n')
        lines.append(line)
    
    # Return the list of read lines.
    return lines

# Select a random object from a list.
def select_random(arr):
    # Generate a random integer between 0 and length of array - 1 (inclusive).
    index = randint(0, len(arr) - 1)

    # Return the object from the list.
    return arr[index]

# Fill the correct characters from the word.
def fill_chars(char_list, word, char):
    # Iterate through each character in the characters list.
    for i in range(len(char_list)):
        # Check the character is correct.
        if word[i].lower() == char:
            # Change the character in the characters list.
            char_list[i] = word[i]
    
    # Return the list of characters.
    return char_list

# Create a character list filled with blanks for the word.
def generate_blanks(word):
    # Create a list for storing the characters.
    char_list = []

    for i in range(len(word)):
        # If the word is a valid character, insert an empty blank into the list.
        if word[i] in valid_char:
            char_list.append('_')
        # Otherwise, insert the original character into the list.
        else:
            char_list.append(word[i])

    # Return the list of characters.
    return char_list
        
# Check whether the character is a wrong guess.
def is_wrong_guess(word, char):
    return char not in word

# A function to play hangman.
def hangman(correct_word):
    # Create a list of empty blanks for the word.
    char_list = generate_blanks(correct_word)

    # Create a list to store the guessed characters.
    guessed_char = []

    # Number of wrong guesses left.
    wrong_guesses = 6

    while True:
        # Print an empty line for the format.
        print()

        # Print the word to be showed.
        print("Word: ", "".join(char_list))
        
        # Print the number of wrong guesses left.
        print("Wrong guesses left:", wrong_guesses)

        # Enter input from the user.
        guess = input('Input character to guess: ').lower()

        # Check that the length of the input is only 1 character.
        if len(guess) != 1:
            print("Please enter only 1 character!")
            continue

        # Check that the letter is a valid character.
        if guess not in valid_char:
            print("Please enter a valid character!")
            continue
        
        # Check that the character is not already guessed.
        if guess in guessed_char:
            print("Please enter an unguessed character!")
            continue
        
        # Check whether the character is correct or not.
        if is_wrong_guess(correct_word, guess):
            print("The character", guess, "is a wrong guess!")
            wrong_guesses -= 1
        else:
            print("The character", guess, "is a right guess!")

        # Add the character to the list of guessed characters.
        guessed_char.append(guess)

        # Fill the correct characters to the characters list.
        char_list = fill_chars(char_list, correct_word, guess)
        
        # Check if the correct word has been guessed.
        if correct_word == "".join(char_list):
            print("You have guessed the correct word:", correct_word)
            return


def main():
    words = read_lines("wordlist.txt")
    word = select_random(words)
    hangman(word)

if __name__ == '__main__':
    main()