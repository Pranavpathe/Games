import random
count=0
number_to_guess=random.randint(1,100)
has_guessed=True
while has_guessed:
    print("Enter your guess:")
    guess=int(input())
    count=count+1
    if(guess<number_to_guess):
        print("Too Low !")
    elif(guess>number_to_guess):
        print("Too High !")
    else:
        print(f"Guessed In {count} Tries")
        has_guessed=False
