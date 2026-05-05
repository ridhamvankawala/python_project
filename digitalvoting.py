n=int(input("enter number of voters="))
a=0
b=0
print("Candidates:a,b")
for i in range(n):
    vote=input("Vote for candidates a or b=")
    if vote=="a":
        a+=1
    elif vote=="b":
        b+=1
    else:
        print("Invalid Choice")
if a>b:
    print("WINNER IS:A")
elif b>a:
    print("WINNER IS:B")
else:
    print("IT IS TIE!")


    
