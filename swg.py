import random
P1_points = 0
P2_points = 0

# Inputs
print("**Welcome to my game***")
User = int(input("2 players or 1 player: "))
P1_name = input("P1 Enter Your name: ")
P2_name = "computer"
if User == 2 : P2_name = input("P2 Enter Your name: ") 
# # loop

while(P1_points < 3 and P2_points < 3):

    P1 = input("pick one Rock, paper, scissor for P1: ").lower()
    P1 = P1[0]
    choice = ["scissor", "rock", "paper"]
    # computer input
    if User == 1 : P2 = choice[random.randint(-1,2)]
    # print(P2)
    else: P2 = input("pick one Rock, paper, scissor for P2: ").lower()
    P2 = P2[0]

    # if ((P1 == 'r' and P2 == 'r') or (P1 == 'p' and P2 == 'p') or (P1 == 'p' and P2 == 'p')):
    #     pass
    if((P1 == 'r' and P2 == 's') or (P1 == 's' and P2 == 'p') or (P1 == 'p' and P2 == 'r')):
        P1_points+=1
        print(f"{P1_name} id awarded with 1 point! Total points for {P1_name} = {P1_points} and {P2_name} = {P2_points}")
    if((P1 == 'r' and P2 == 'p') or (P1 == 's' and P2 == 'r') or (P1 == 'p' and P2 == 's')):
        P2_points+=1
        print(f"{P2_name} id awarded with 1 point! Total points for {P1_name} = {P1_points} and {P2_name} = {P2_points}")


if(P1_points>P2_points): 
    print(f"{P1_name} Wins!")
else: 
    print(f"{P1_name} Wins!")






# print(P1)
# P2 =