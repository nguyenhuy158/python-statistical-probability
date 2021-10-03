import hangman_life
import hangman_guessing
import random

# tru va show hinh
def missLetter(countDownt):
	countDownt -= 1
	print(hangman_life.lives[countDownt])
	return countDownt

# win or lost
def Result(guess, word):
	count = guess.count('_')
	if count == 0:
		print("WINNER GAME")
	else:
		print('you died lose game')
	print('this word is {}'.format(word))
    
# start game
def creat():
	# random word
# 	word = hangman_guessing.guess_list[random.randint(0, len(hangman_guessing.guess_list) - 1)].lower()
	word = random.choice(hangman_guessing.guess_list)
	word = word.lower()
	print(word)
	guess = ['_' for i in range(len(word))]
	return [word, guess]

def main():
	countDownt = len(hangman_life.lives) - 1
	setLetters = set()
	print(hangman_life.game_name)
	print('START')
	print(hangman_life.lives[countDownt])

	[word, guess] = creat()
	while countDownt != 0:
		if not guess.count('_'):
			break
		print(''.join(guess))
		letter = input('guess a letter: ')
		while letter in setLetters:
			letter = input('enter again: ')
		setLetters.add(letter)
		if letter in word:
			for i in range(len(guess)):
				if word[i] == letter:
					guess[i] = letter
		else:
			countDownt = missLetter(countDownt)

	Result(guess, word)

if __name__ == '__main__':
	main()



