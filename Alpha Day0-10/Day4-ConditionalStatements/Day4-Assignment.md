
# Assignment: Nested `if-else` Statements

## Objective

Design a Python program that simulates a simple ticket booking system for a movie theater. The program should allow users to select a movie, choose a showtime, and book tickets. Use nested `if-else` statements to handle different scenarios.

## Instructions

1. Create a list of available movies (at least 3 options).
2. Ask the user to select a movie by entering the corresponding number.
3. Based on the movie selection, display available showtimes (e.g., morning, afternoon, evening).
4. Ask the user to choose a showtime.
5. Prompt the user to enter the number of tickets they want to book.
6. Calculate the total cost based on the movie and showtime.
7. Display a confirmation message with the movie name, showtime, and total cost.

## Tasks

1. **Movie Selection**:
   - Ask the user to select a movie by entering the corresponding number.
   - Display the available movie options.

2. **Showtime Selection**:
   - Based on the movie selection, display available showtimes.
   - Ask the user to choose a showtime by entering the corresponding number.

3. **Ticket Booking**:
   - Prompt the user to enter the number of tickets they want to book.

4. **Cost Calculation**:
   - Calculate the total cost based on the movie and showtime.
   - Assume a fixed ticket price (e.g., $10 per ticket).

5. **Confirmation Message**:
   - Display a confirmation message with the movie name, showtime, and total cost.

## Example Interaction

```
Welcome to Movie Theater Ticket Booking!

Available Movies:
1. Avengers: Endgame
2. Inception
3. The Dark Knight

Enter the number of your chosen movie: 2
Showtimes for Inception:
1. Morning (10:00 AM)
2. Afternoon (2:30 PM)
3. Evening (7:00 PM)

Choose a showtime (enter the number): 3
Enter the number of tickets: 2

Confirmation:
Movie: Inception
Showtime: Evening (7:00 PM)
Total Cost: $20

Enjoy the movie!
```

## Bonus Challenge

Implement error handling for invalid inputs (e.g., if the user enters an invalid movie number or showtime).
