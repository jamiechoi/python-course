from random import randint

# A list of valid characters.
valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A function to read all lines from a file.
def read_lines(filename):
	# Open the file in read mode for reading the content of the file.
	file = open(filename, "r")
	
	# Create a list to store all the lines in the file.
	lines = []
	
	# Read all lines from the file.
	for line in file:
		lines.append(line.rstrip())
	
	# Return the list of read lines.
	return lines

# Select a random object from a list.
def select_random(arr):
	# Select a random number from 0 to len(arr) - 1.
	index = randint(0, len(arr) - 1)
	
	return arr[index]

# Fill the correct characters into the character list.
def fill_chars(char_list, word, char):
	for i in range(len(word)):
		if word[i].upper() == char.upper():
			char_list[i] = word[i]
		
	return char_list
	
# Create the blanks for a word for hangman.
def make_blanks(word):
	# Change the word into a list of characters.
	blanks = list(word)
	
	# If the character is a valid character, turn it into a underscore.
	for i in range(len(blanks)):
		if blanks[i].upper() in valid_chars:
			blanks[i] = '_'
	
	return blanks
	
def game(word):
	# A list to hold the characters being guessed.
	char_list = make_blanks(word)
	
	# Number of wrong guesses left.
	wrong_count = 8
	
	# List of used characters.
	used_chars = []
	
	# Game loop.
	while "".join(char_list) != word and wrong_count > 0:
		# Print information to user.
		print()
		print("Word to guess:", "".join(char_list))
		print("Character guessed:", ", ".join(used_chars))
		print("Wrong guesses left:", wrong_count)
		
		# Get guess from user.
		guess = input("Character to guess: ").upper()
		
		# Check that the guess is valid.
		if len(guess) != 1 or guess not in valid_chars:
			print(">> Error: Enter a valid character!")
			continue
		
		# Check that the guessed character is not already used.
		if guess in used_chars:
			print(">> Error: Character is used!")
			continue
		
		# Add the character to the list of used characters.
		used_chars.append(guess)
		
		# Check whether the guess is a wrong guess.
		if guess not in word.upper():
			wrong_count = wrong_count - 1
		
		# Fill the characters in the character list.
		fill_chars(char_list, word, guess)
	
	print()
	
	# Print a message when the game ends.
	if wrong_count > 0:
		print("You guessed the word:", word)
	else:
		print("You did not guess the word:", word)
	
def main():
	# Read the words from wordlist.txt.
	words = read_lines("wordlist.txt")
	
	# Select a random word from the list.
	word = select_random(words)
	
	# Start the game.
	game(word)

if __name__ == "__main__":
	main()
