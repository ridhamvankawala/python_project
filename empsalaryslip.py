name=input("enter name=")
sal=float(input("enter basic salary="))
hra=sal*20/100
da=sal*10/100
pf=sal*12/100
net=hra+da+sal-pf
print("--SLIP SALARY--")
print("Employee Name=",name)
print("Basic Salary=",sal)
print("Hra(20%)is=",hra)
print("Da(10%)is=",da)
print("pf(12%)is=",pf)
print("Net Salary is=",net)



