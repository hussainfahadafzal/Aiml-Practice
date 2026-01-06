def print_digits(n):
    if n == 0:
        print(0)
        return

    while n > 0:
        digit = n % 10
        print(digit)
        n //= 10

n = int(input("Enter the number: "))
print_digits(n)
