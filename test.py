import os
import pyttsx3 as tts

os.system("color 3")   # colour can be any number between 1 to 8

print("\t\t====================================================================================")
print("\t\t\t\t\t\tPython Personal Assistant")
print("\t\t====================================================================================")
print()

#tts.speak("Welcome to your Personal Assistant")

startProgram = ["open", "run", "start", "begin", "execute"]
closeProgram = ["close", "stop", "end", "finish", "terminate"]

cmd = input("enter u r command here")
