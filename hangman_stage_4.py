from random import choice
any_word = choice(['python', 'java', 'kotlin', 'javascript'])
print(any_word)

any_word_ko_split = [x for x in any_word]

for i in range(3, len(any_word_ko_split)):
    any_word_ko_split[i] = "-"
given_word = "".join(any_word_ko_split)

print("Guess the word", given_word)
input_ = input()
if input_ == any_word:
    print("You survived!")
else:
    print("You are hanged!")     