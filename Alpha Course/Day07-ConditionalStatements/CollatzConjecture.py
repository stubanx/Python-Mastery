# Collatz Conjecture
n = int(input("Enter a positive integer: "))
print(f"{n} -> ", end="")
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    print(n, end=" -> ")
print("1")
