word = input("Enter the word here: ") #Takes a input of string and stores it in word variable
reversed_word = word[::-1] #Reverses the word and stores it in reversed_word variable
print(f"Reversed word: {reversed_word}") #prints the reversed word with a use of f-strings
score = len(word) # score variable is assigned the int value which is length of the origional word
print(f"Your score: {score} points")
# Bonus
# print(f"Your score: {score*2 if (score == len(reversed_word)) else score} points")