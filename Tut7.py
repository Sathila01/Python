#Tutorial 7

hidden_word = "example"
no_of_Attempts = len(hidden_word)
storage = "_"*len(hidden_word)

print("Let's play Guess the Word")
print("You have "+str(no_of_Attempts)+" turns to guess the word!")
print(storage)

while no_of_Attempts > 0:

    guess = input("Guess a letter: ").lower()
    no_of_Attempts = no_of_Attempts - 1

    for i in range(len(hidden_word)):

        if guess == hidden_word[i]:
            storage = storage[:i] + guess + storage[i+1:]  # ********

    print(storage)

print("End of the game")
