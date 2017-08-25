#https://www.reddit.com/r/beginnerprojects/comments/4mwwxx/soundboard_x_post_rlearnpython/
#As the title says we will be making a soundboard that has a gui and a multitude (more than one) of song clips. Any package is allowed and this will be a great intro to basic GUI building.
#Bonus points if you: Somehow manage to use Snack (I couldn't for the life of me), can multi-thread a stop button and/or explain to me why the audio quality was terrible when pygame was used (on multiple devices)
#tldr: Make a soundboard that works with a gui and explain to me why I'm so bad
#source https://pastebin.com/1Dy6P2VD

from winsound import * #available Windows only
from Tkinter import *
import sys
# from pygame import *

# pygame.init()
# pygame.mixer.music.load("Let Your Love Flow.mp3")
# pygame.mixer.music.play()

top = Tk()
play =  lambda:  PlaySound("Let Your Love Flow.mp3" , SND_LOOP)
play1 = lambda: PlaySound("Life Is A Highway.mp3", SND_LOOP)
stop =  lambda:  PlaySound(None, SND_ASYNC)

button = Button(top, text = 'JOJO', command = play)
button.pack()

button1 = Button(top, text = 'Failure', command = play1)
button1.pack()

buttonS = Button(top, text = 'Stop', command = stop)
buttonS.pack()

top.mainloop()

