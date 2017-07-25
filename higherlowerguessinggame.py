#https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/
#Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the answer. When the user guesses the correct number, print out a congratulatory message.
#Add an introduction message that explains to the user how to play your game.
#In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
#At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

from random import randint
def playgame():
	guessthenumber = randint(1,100)
	guess = 1
	counter = 1
	while guess != guessthenumber:
		print("cheat:",guessthenumber)
		guess = int(input("Guess the number between 1 and 100 "))
		if guess == guessthenumber:
			print("Congratulations.  Number of guesses", counter)
			break
		elif guess > guessthenumber:
			print("Guess lower")
		elif guess < guessthenumber:
			print("Guess higher")
		else:
			print("Malfunction")
			break
		counter += 1

playgame()
while True:
	playgamep = input("Do you want to play again?  Type y to play again. ")
	if playgamep == "y":
		playgame()
	else:
		break


