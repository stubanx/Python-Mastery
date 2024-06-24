
import time
timestamp = time.strftime('%H')
hour = int(timestamp)
if hour < 12:
    print("Good morning!")
elif hour < 16:
    print("Good afternoon!")
elif hour < 20:
    print("Good evening!")
else:
    print("Good night!")
