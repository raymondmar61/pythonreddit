#https://www.reddit.com/r/beginnerprojects/comments/45fmoa/print_a_deck_of_cards/
#random shuffle
#RM add random pick 5 cards
#RM add random pick 7 cards

from random import randint
suits = ["s","h","c","d"]
face = ["A","K","Q","J"]
#facecards = ["Ac","Ad","Ah","As","Kc","Kd","Kh","Ks","Qc","Qd","Qh","Qs","Jc","Jd","Jh","Js",]
#generate a list of cards
cards = []
for eachface in face:
	for eachsuits in range(0,4):
		print(eachface+""+suits[eachsuits])
		cards.append(eachface+""+suits[eachsuits])
for numbercards in range(10,1,-1):
	for eachsuits in range(0,4):
		print(str(numbercards)+""+suits[eachsuits])
		cards.append(str(numbercards)+""+suits[eachsuits])
print(cards)

#print five cards
fivecards = []
while len(fivecards) < 5:
	randomnumber = randint(0,51)
	selectedcard = cards[randomnumber]
	if selectedcard in fivecards:
		pass
	else:
		fivecards.append(selectedcard)
print(", ".join(fivecards))

#print seven cards
sevencards = []
while len(sevencards) < 7:
	randomnumber = randint(0,51)
	selectedcard = cards[randomnumber]
	if selectedcard in sevencards:
		pass
	else:
		sevencards.append(selectedcard)
print(", ".join(sevencards))