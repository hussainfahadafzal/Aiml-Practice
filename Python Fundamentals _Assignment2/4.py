def count_digit (n):
    count = 0
    if(n==0):
        return 1
    while(n>0):
        count += 1 
        n //= 10
    return count
n=int(input("Enter the no."))
print(count_digit(n))