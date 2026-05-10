number=45
attempt=0
while True:
    guess=int(input("enter number="))
    attempt+=1
    if guess>number:
        print("Too High!")
    elif guess<number:
        print("Too Low!")
    else:
        print("Correct Guess")
        print("Attempt Use is ",attempt)
        break
