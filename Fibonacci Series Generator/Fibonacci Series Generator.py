def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


n = int(input("Enter a Positive Number: "))
if n < 0:
    print("Number is not valid!!!")
i = 0
print("Fibonacci Series: ")
for i in range(0, n):
    print(fibonacci(i))
