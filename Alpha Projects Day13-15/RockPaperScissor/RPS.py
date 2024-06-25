# Rock Paper Scissors Game

player1 = input("Enter Player1's name: ")
player2 = input("Enter Player2's name: ")
p2_points = 0
p1_points = 0
highest = 0

while highest != 3:
    print(f"Player 1's points: {p1_points}\nPlayer 2's points: {p2_points}")
    p1_response = input("Enter Player1's response (rock, paper, scissors): ").lower()
    p2_response = input("Enter Player2's response (rock, paper, scissors): ").lower()

    if p1_response == p2_response:
        print("It's a draw!")
    elif (p1_response == 'rock' and p2_response == 'scissors') or \
         (p1_response == 'paper' and p2_response == 'rock') or \
         (p1_response == 'scissors' and p2_response == 'paper'):
        p1_points += 1
        print(f"{player1} wins this round!")
    elif (p2_response == 'rock' and p1_response == 'scissors') or \
         (p2_response == 'paper' and p1_response == 'rock') or \
         (p2_response == 'scissors' and p1_response == 'paper'):
        p2_points += 1
        print(f"{player2} wins this round!")
    else:
        print("Invalid input! Try again.")

    highest = max(p1_points, p2_points)

if p1_points == p2_points:
    print(f"It's a draw between {player1} and {player2}")
elif p1_points == highest:
    print(f"{player1} won the game.")
else:
    print(f"{player2} won the game.")
