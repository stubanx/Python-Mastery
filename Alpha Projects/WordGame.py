import random
import os
import sys
tries=6
ans=[]
points=10
words=['microsoft','google','apple','meta','amazon','netflix','facebook','oracle']
word=random.choice(words)
hint=f'It starts with {word[0]} and ends with {word[-1]}'
name=input('Enter your name: ')
print()
print(f'Hello! {name},\n You have {tries} tries to guess the word. After 3rd try you can ask for hint,\nThe word is the company name of top tech companies in the world.')
for i in range(tries):
    print(f'Try {i}: ')
    print()
    while True:
        a=input("Guess the letter: ")
        if len(a)==1:
            if a in word and ans.count(a)<word.count(a):
                ans.append(a)
                print("It's in it")
            else:
                points-=1
                print('Wrong guess')
                break
        else:
            a=input('Try again: ')
        if len(ans)==len(word):
            break
    if len(word)==len(ans):
        print(f'Congratulations!!\nYou guessed the word right.\nIt was "{word}".\nYou are awarded with {points} points.')
        break
    if i==3:
        hint_a=input("Need a hint??It will cost -2 from points: ")
        if hint_a.lower().startswith('y')==1:
            points-=2
            print(hint)
        else:
            print("You/'re awesome! Here's a +1 to you for that.")
            points+=1
        sys.exit(1)

print(f'In the {tries} attempts you were able to guess {len(ans)} letters of the {len(word)} letter word.')
g_word=input("Guess the word: ")
if g_word==word:
    print(f'Congratulations!!\nYou guessed the word right.\nIt was "{word}".\nYou are awarded with {points} points.')  
else:
    print(f"OHNO!! You lose, The answer was '{word}'\nPoints: {points} ")
