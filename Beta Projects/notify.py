# import os
# os.system("osascript -e \'say \"Hello Dhruv\"\'; osascript -e \'display alert \"Drink Water\"\'")
import ctypes
import pyttsx3

# 1. Text-to-speech ("Hello Dhruv")
engine = pyttsx3.init()
engine.say("Hello! Dhruv, drink some water.")
engine.runAndWait()

# 2. Display an alert message box ("Drink Water")
ctypes.windll.user32.MessageBoxW(0, "Drink Water", "Reminder", 0x40 | 0x1)
