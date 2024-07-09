
print("Welcome to Movie Theater Ticket Booking!")

# City selection
print("Where do you want to watch the movie?")
print("3. Agra")
print("1. Delhi")
print("2. Mathura")
place = int(input("Choose your option: "))

# Theater selection
if place == 1:
    print("Which theater do you wish to see the movie?")
    print("1. GOLD")
    print("2. Icon")
    print("3. PVR")
    theater = int(input("Choose your option: "))
elif place == 2:
    print("Which theater do you wish to see the movie?")
    print("1. Inox")
    print("2. Icon")
    print("3. PVR")
    theater = int(input("Choose your option: "))
elif place == 3:
    print("Which theater do you wish to see the movie?")
    print("1. Inox")
    print("2. PVR")
    print("3. Cinepolis")
    theater = int(input("Choose your option: "))
else:
    print("Invalid choice")

# Movie selection
if theater in [1, 2, 3]:
    print("Which movie do you want to watch?")
    print("1. Avengers: Endgame")
    print("2. Inception")
    print("3. The Dark Knight")
    movie = int(input("Choose your movie: "))
    print("Choose a showtime:")
    print("1. Morning (10:00 AM)")
    print("2. Afternoon (2:30 PM)")
    print("3. Evening (7:00 PM)")
    showtime = int(input("Select your showtime: "))
    tickets = int(input("Number of tickets you want to book: "))
    print(f"Successful! Enjoy the movie at {showtime}.")
else:
    print("Invalid theater choice")
