import random

def saveScore(a, b):
	fi = open('score.txt','w')
	result = f'scorePlayer{a}\nscoreComputer{b}'
	fi.write(result)
	fi.close()

# set variable default
scorePlayer = 0
scoreComputer = 0
color = {1: 'red', 2: 'green', 3: 'blue'}

#
print('Welcome to ..')
print('\trule of game:')
print('\t1: red\n\t2: green\n\t3: blue')

while True:
	#
	choosePlayer = int(input('Enter you choose: '))
	while choosePlayer not in [1, 2, 3]:
		choosePlayer = int(input("Error I don't understand, again: "))

	chooseComputer = random.randint(1,3)
	print(f'\nyou choose {color.get(choosePlayer)}')
	print(f'computer choose {color.get(chooseComputer)}')
	if choosePlayer == chooseComputer:
		scorePlayer += 1
		print('You win')
	else:
		scoreComputer += 1
		print('You miss')
	print('score you: {}\nscore computer: {}'.format(scorePlayer, scoreComputer))

	again = input('\n\nDo you want play again? (Y/N)').upper()
	if again == 'N':
		break

print('Thank for you play. Hope you enjoy it')
saveScore(scorePlayer, scoreComputer)