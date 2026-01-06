def sum_digit (n):
    if(n==0):
        return 0
    sum = 0
    while(n>0):
        sum += n%10
        n//=10
    return sum

n = int(input("Enter the no."))
print(sum_digit(n))    
    
        
