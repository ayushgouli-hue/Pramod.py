n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    if i % 2 != 0:      # odd check
        total += i

print(f"Sum of odd numbers from 1 to {n} is {total}")