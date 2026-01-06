a = 100
n = int(input("Enter a Guess Number: "))
if(a<n):
    print("Too High")
elif(a>n):
    print("Too Low")
else:
    print("Correct!")