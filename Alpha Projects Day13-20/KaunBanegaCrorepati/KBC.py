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

def kbc_lifelines(ll):
    from random import random
    # Implement lifelines here (e.g., 5050, phone_a_friend, etc.)
    if ll ==1:
        #5050
        
        print([correct_answers[i],5-correct_answers[i]].sorted())
    if ll ==1:

        #Phone-a-friend
        print(f'{random(1,4)},{correct_answers[i]}')
    if ll ==3:
        #5050
        print(f'{random(1,4)},{correct_answers[i]}')
    if ll ==1:
        #5050
        print(f'{random(1,4)},{correct_answers[i]}')
    if ll ==1:
        #5050
        print(f'{random(1,4)},{correct_answers[i]}')

    pass
def guide():
    print("\nLifelines:")
    print(dic_lifeline)
    print("\nPress (1), (2), (3), or (4) to choose an answer.")
    print("Press (0) for lifelines.")
    print("Press (9) to exit the game.")
    input("Press Enter to start the quiz.\n")
    

def win_amount(num):
    if levels[num + 1] < 5000:
        return 0
    elif levels[num + 1] < 10000:
        return 5000
    elif levels[num + 1] < 25000:
        return 10000
    else:
        return 25000

# Main code
print("Welcome to Gantavya's KBC!\n\nInput your basic details:")
form()
gude()

question_bank = [
    ["Who is the king?", "(1) Wazir", "(2) Raja", "(3) Rani", "(4) Salim"],
    ["Who is the pm of India?", "(1) Rahul Fandhi", "(2) Narendra Modi", "(3) Sonia", "(4) Akbar"],
    ["What is Python?", "(1) animal", "(2) House", "(3) monkey", "(4) Ashu"],
    ["what is 1+92?", "(1) 34", "(2) 36", "(3) 76", "(4) 93"],
]
correct_answers = [2,2,4,4]  # correct answers for each question
levels = [0, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 25000, 50000, 100000]
dic_lifeline = {
    1: "50-50",
    2: "Phone-a-Friend",
    3: "Audience Poll",
    4: "Switch the Question",
    5: "Ask the Expert"
}
for i in range(len(question_bank)):
    print(f"Question for Rs. {levels[i + 1]}:\nQ{i+1}")
    for line in question_bank[i]:
        print(line)
    ans = int(input("Enter response(1,2,3,4) or (0:lifeline; 321:exit): "))
    if ans == 0:
        ll=int(input(dic_lifeline))
        print("Lifeline called!\n")
        kbc_lifelines(ll)
    if ans == 9:
        print(f"You took an exit from the game with a prize money of Rs. {levels[i]}\n")
        break
    if ans == correct_answers[i]:
        print(f"You won Rs. {levels[i + 1]}")
        if i==len(question_bank)-1:
            print("7cr")
        # else:
        #     print("Press enter for next question.")
    else:
        print("Wrong Answer! Thank you for playing!")
        print(win_amount(i))
        break
