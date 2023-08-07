import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import wordlist
chosen_word = random.choice(wordlist.word_list)


display = []
word_length = len(chosen_word)
for i in range(word_length):
    display+= "_"
print(display)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print("You have already guessed this letter")

    for j in range(word_length):
        letter = chosen_word[j]
        if letter == guess:
            display[j] = letter
    if guess not in chosen_word:
        print("Choosen letter not in the word. Baam you loose a life!")
        lives-=1
        if lives ==0:
            end_of_game = True
            print("You loose!")
    
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
