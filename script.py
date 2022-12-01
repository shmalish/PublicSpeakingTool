import random
import time
import pyttsx3
engine = pyttsx3.init()

engine.runAndWait()
text_file=open("nouns.txt",'r')
lines = text_file.read().split('\n')


while True:
	word = random.randint(0, len(lines)-1)
	print(lines[word])
	time.sleep(random.randint(10,200))
	engine.say(lines[word])
	
	

