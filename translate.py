from googletrans import *
import time

translator = Translator()

def translate():
	#result = translator.translate(phrase, src='fr', dest='en')
	phrase = input("entrer une phrase: ")
	translations = translator.translate(phrase, src='fr', dest='en')
	print("...")
	time.sleep(0.5)
	print(' ',translations.origin, '----->', translations.text)
	print("...\n")


restart = True 

while restart:
	translate()
	time.sleep(1)





	

