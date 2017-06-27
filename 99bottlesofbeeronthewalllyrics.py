#https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/
#Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.
#1.	If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
#2.	Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#3.	Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
#4.	Put a blank line between each verse of the song.

def lyrics(count):
	if count != 1:
		print(count, "bottles of beer on the wall," ,count,  "bottles of beer.")
	else:
		print(count, "bottle of beer on the wall," ,count,  "bottle of beer.")
	count=count-1
	if count > 1:
		print("Take one down and pass it around," ,count, "bottles of beer on the wall.")
	elif count == 1:
		print("Take one down and pass it around," ,count, "bottle of beer on the wall.")
	else:
		print("Take one down and pass it around, no more bottles of beer on the wall.")
	print("\n")

def lastlyrics(startcount):
	print("No more bottles of beer on the wall, no more bottles of beer.")
	print("Go to the store and buy some more.")
	print(startcount, "bottles of beer on the wall.")

startcount = 99
count = startcount
while count > 0:
	lyrics(count)
	count -= 1
	if count == 0:
		lastlyrics(startcount)
		break