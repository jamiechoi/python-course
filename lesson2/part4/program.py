from random import randint

# This variable stores the randomly generated number.
generatedNumber = randint(1, 100)

# This variable stores the player's input.
playerInput = 0

# This variable stores the number of guesses of the player.
numberOfGuesses = 0

# These variables store the range of numbers that the player should guess.
lowerBound = 1
upperBound = 100

# Repeat forever
while True:
    # Print the range of numbers to player.
    print("Range:", lowerBound, "-", upperBound)

    # Read the player's input.
    playerInput = input("Enter a number: ")
    
    # Check if the player's input is a number.
    if not playerInput.isdigit():
        print("The input is not a number!")
        # Jump to the 'beginning' of the block (by going to the next iteration).
        continue
    
    # Convert the player's input into an integer.
    playerInput = int(playerInput)

    # Check if the player inputted a number outside the range.
    if playerInput < lowerBound or playerInput > upperBound:
        print("The input is outside the bound!")
        # Jump to the 'beginning' of the block (by going to the next iteration).
        continue
    
    # Update the number of guesses of the player.
    numberOfGuesses = numberOfGuesses + 1

    # Check if the player's input equals to the generated number.
    if playerInput == generatedNumber:
        # End the code block.
        break
    
    # Update the range of the numbers to guess according to player's input.
    if playerInput < generatedNumber:
        lowerBound = playerInput + 1
    else:
        upperBound = playerInput - 1

print("Number generated: ", generatedNumber)
print("Number of guesses:", numberOfGuesses)