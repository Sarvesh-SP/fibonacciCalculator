print("Welcome to the Fibonacci Calculator App")

num = int(
    input("How many digits of the fibonacci sequence would you like to compute: "))

fib = [1, 1]

for x in range(num - 2):
    new_fib = fib[x] + fib[x+1]
    fib.append(new_fib)


print(fib)
