expense=[]
print("1.add expense")
print("2.view expense")
print("3.total expense")
while True:
    choice=int(input("enter your choice="))
    if choice==1:
        item=int(input("enter number of item="))
        amt=float(input("enter amount="))
        expense.append((item,amt))
    elif choice==2:
        print("Expense list:")
        for item,amt in expense:
            print("Total item is=",item,"->","Total amount is=",amt)
    elif choice==3:
        total=sum(amt for item,amt in expense)
        print("Total expense=",total)
    elif choice==4:
        print("THANK YOU")
        break
    else:
        print("INVALID CHOICE")
