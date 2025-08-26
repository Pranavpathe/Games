import random
choices=("r","p","s")
emojis={"r":"🪨","p":"📄","s":"✂️"}
while True:
    user_choice=input("Rock, Paper, Scissors (r/p/s) :").lower()
    if user_choice not in choices:
        print("Invalid Input !!")
        continue
    computer_choice=random.choice(choices)
    print(f"You Chose {emojis[user_choice]} ",end=" AND ")
    print(f"Computer Chose {emojis[computer_choice]}")
    if user_choice==computer_choice:
        print("Its a tie")
    elif(
        (user_choice=="r" and computer_choice=="s") or
        (user_choice=="s" and computer_choice=="p") or
        (user_choice=="p" and computer_choice=="r")):
            print("--> You Won 🎉🎉")
    else:
        print("--> Computer won 😢")
    should_continue=input("Continue ??(y/n)").lower()
    if should_continue=="n":
        print("Thank You For Playing 😊")
        break

