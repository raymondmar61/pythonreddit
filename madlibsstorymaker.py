#https://www.reddit.com/r/beginnerprojects/comments/1i8vt5/project_mad_libs_story_maker/
#http://www.madtakes.com/
#Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted. The story doesn't have to be too long, but it should have some sort of story line.
#If the user has to put in a name, change the first letter to a capital letter.
#Change the word "a" to "an" when the next word in the sentence begins with a vowel.

vowels = ["a","e","i","o","u","A","E","I","O","U"]
def aan(word):
	if word[0] in vowels:
		return "an"
	else:
		return "a"

adjective1 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
animal = input("Animal: ")
noise = input("Noise: ")
number = float(input("Number: "))
print("\n")
print(adjective1.title()+ " Macdonald had " +aan(noun1)+ " " +noun1+ " E-I-E-I-O")
print("and on that " +noun2+ " he had " +aan(noun2)+ " " +animal+ ", E-I-E-I-O")
print("with " +aan(noise)+ " " +noise+ " " +noise+ " here")
print("and " +aan(noise)+ " " +noise+ " " +noise+ " there,")
print("hear " +aan(noise)+ " " +noise+ " there " +aan(noise)+ " " +noise+ ",")
print("everywhere " +aan(noise)+ " " +noise+ " " +noise+ ",")
print(adjective1.title()+ " Macdonald had " +aan(noun1)+ " " +noun1+ " E-I-E-I-O")
print("And " +adjective1.title()+ " favorite number is" ,number)