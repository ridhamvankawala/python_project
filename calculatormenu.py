a=int(input("enter a="))
b=int(input("enter b="))
print("1.for add")
print("2.for substract")
print("3.for multiply")
print("4.for divide")
print("5.for exit")
while True:
    ch=int(input("Enter your choice="))
    if ch==1:
        c=a+b
        print("sum is=",c)
    elif ch==2:
        c=a-b
        print("substract is=",c)
    elif ch==3:
        c=a*b
        print("Multiply is=",c)
    elif ch==4:
        c=a/b
        print("Division is=",c)
    elif ch==5:
        c=a+b
        print("THANK YOU")
        break
    else:
        print("INVALID CHOICE")
        

        
        

