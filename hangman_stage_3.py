from random import choice
a = choice(['python', 'java', 'kotlin', 'javascript'])
b = input("Guess the word:") 
if a == b:
    print("You survived!")    
else:
    print("You are hanged!")  