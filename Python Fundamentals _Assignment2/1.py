a= int (input("Enter Salary : "))
if (a<30000):
    print ("Tax Rate is 5%")
    print((5*a)/100)
elif (a>=30000 and a<=70000):
    print ("Tax Rate is 15%")
    print((15*a)/100)
else :
    print ("Tax Rate is 25%")
    print((25*a)/100)