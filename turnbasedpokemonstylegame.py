#https://www.reddit.com/r/beginnerprojects/comments/1aw0iq/project_turn_based_pokemon_style_game/
#Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
#The first move should do moderate damage and has a small range (such as 18-25).
#The second move should have a large range of damage and can deal high or low damage (such as 10-35).
#The third move should heal whoever casts it a moderate amount, similar to the first move.
#After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
#SUBGOALS
#When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
#When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
#Give each move a name.

from random import randint
def smallrangedamage():
	smallrangedamage = randint(18,26)
	return smallrangedamage
def longrangedamage():
	longrangedamage = randint(10,36)
	return longrangedamage
def healdamage():
	healdamage = randint(18,26)
	return healdamage

userhealth = 100
computerhealth = 100
counter = 1
while userhealth > 0 and computerhealth > 0:
	if userhealth > 100:
		userhealth = 100
	if computerhealth > 100:
		computerhealth = 100
	print("\n")
	print("Round",counter)
	print("User's health",userhealth)
	print("Computer's health",computerhealth)
	usermove = input("User small range attack (s), long range attack (l) or heal (h)?")
	if usermove == "s":
		damage = smallrangedamage()
		computerhealth = computerhealth - damage
		print("Damage to computer", damage)
		print("Computer's health",computerhealth)
	elif usermove == "l":
		computerhealth = computerhealth - longrangedamage()
		print("Computer's health",computerhealth)
	elif usermove == "h":
		userhealth = userhealth + healdamage()
		print("User's health",userhealth)
	if computerhealth <= 0:
		print("User wins!")
		break
	computermovechoices = ["s","l","h"]
	computermove = computermovechoices[randint(0,2)]
	print("Computer chooses "+computermove)
	if computermove == "s":
		userhealth = userhealth - smallrangedamage()
		print("User's health",userhealth)
	elif computermove == "l":
		userhealth = userhealth - longrangedamage()
		print("User's health",userhealth)
	elif computermove == "h":
		computerhealth = computerhealth + healdamage()
		print("Computer's health",computerhealth)
	if userhealth <= 0:
		print("Computer wins!")
		break
	counter += 1




