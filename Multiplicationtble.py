num = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 3:
        continue        # skip this iteration
    print(f"{num} x {i} = {num * i}")   