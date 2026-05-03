mark=[]
print("1.for add mark")
print("2.for view all mark")
print("3.for average mark")
print("4.for highest mark")
print("5.for exit")
while True:
    ch=int(input("enter your choice="))
    if ch==1:
        values=int(input("enter total subject="))
        for i in range(values):
            value=int(input("enter mark="))
            mark.append(value)
        print("MARK ADDED")
    elif ch==2:
        if (len(mark)==0):
            print("no mark add")
        else:
            print(mark)
    elif ch==3:
        avg=sum(mark)/len(mark)
        print("Average mark is ",avg)
    elif ch==4:
        high=max(mark)
        print("Highest is ",high)
    elif ch==5:
        print("THANK YOU")
        break
    else:
        print("INVALID CHOICE")
        
    
            
        


        
