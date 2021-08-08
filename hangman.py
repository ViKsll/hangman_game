attempts = 10
word = input('Enter a word: ').lower()
splitted_word = list(word)
guessed = ['_' for i in splitted_word]

while True:
    print(' '.join(guessed))
    print('Attempts: ', attempts)
    letter = input('Guess a letter: ').lower()
    if letter in splitted_word:
        for i, c in enumerate(splitted_word):
            if c == letter:
                guessed[i] = letter
        if '_' not in guessed:
            print('You win!')
            break
    else:
        attempts -= 1
    if attempts == 0:
        print('You lose!')
        break
