print("Welcome to the Fibonacci Calculator App")

num = int(
    input("\nHow many digits of the fibonacci sequence would you like to compute: "))

fib = [1, 1]

for x in range(num - 2):
    new_fib = fib[x] + fib[x+1]
    fib.append(new_fib)

print(F"\nThe first {num} numbers of the Fibonacci Sequence are: ")
for x in fib:
    print(x)

golden = []
for i in range(len(fib) - 1):
    ratio = fib[i+1] / fib[i]
    golden.append(ratio)


print("\nThe corresponding Golden Ratio values ar: ")

for x in golden:
    print(x)


print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618..")
