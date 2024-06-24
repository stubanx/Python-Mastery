def form():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Choose your gender (M/F): ").upper()
    locationa = input("Enter your country: ")
    locationb = input("Enter your state: ")
    locationc = input("Enter your City: ")
    print("Kindly confirm your details:\n", name, age, gender, locationa, locationb, locationc)
    confirm = input("Y/N: ").upper()
    if confirm.startswith("Y")!=1:
        form()

def kbc_lifelines():
    # Implement lifelines here (e.g., 5050, phone_a_friend, etc.)
    pass

def win_amount():
    if levels[i + 1] < 5000:
        return 0
    elif levels[i + 1] < 10000:
        return 5000
    elif levels[i + 1] < 25000:
        return 10000
    else:
        return 25000

# Main code
print("Welcome to Gantavya's KBC!\n\nInput your basic details:")
form()

print("\nLifelines:")
print("1: 50-50")
print("2: Phone-a-Friend")
print("3: Audience Poll")
print("4: Switch the Question")
print("5: Ask the Expert")
print("\nPress (1), (2), (3), or (4) to choose an answer.")
print("Press (0) for lifelines.")
print("Press (321) to exit the game.")
input("Press Enter to start the quiz.\n")


question_bank = [
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"]
    # Add more questions here...
]
correct_answers = [2,2,2,2,2,2,2,2]  # Add correct answers for each question
levels = [0, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 25000, 50000, 100000]
dic = {
    1: "50-50",
    2: "Phone-a-Friend",
    3: "Audience Poll",
    4: "Switch the Question",
    5: "Ask the Expert"
}
for i in range(len(question_bank)):
    print(f"Question for Rs. {levels[i + 1]}:\n")
    for line in question_bank[i]:
        print(line)
    ans = int(input("Enter response(1,2,3,4) or (0:lifeline; 321:exit): "))
    if ans == 0:
        print(dic)
        print("Lifeline called!\n")
        kbc_lifelines()
    if ans == 321:
        print(f"You took an exit from the game with a prize money of Rs. {levels[i]}\n")
        break
    if ans == correct_answers[i]:
        print(f"You won Rs. {levels[i + 1]}\n")
        print("Press enter for next question.")
    else:
        print("Wrong Answer! Thank you for playing!\n")
        win_amount()
        break
