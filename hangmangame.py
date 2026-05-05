word=["hi","abc","hello","xyz","bye"]
max_attempt=6
attempt_left=max_attempt
while attempt_left>0:
    guess=input("enter word=")
    if guess in word:
        print("CORRECT GUESS")
        break
    else:
        attempt_left-=1
        print(f"INCORRECT GUESS!,attempt_left={attempt_left}")
    if attempt_left==0:
        print("\nGAME OVER!YOU USE ALL 6 ATTEMPT")
        break
    
        


