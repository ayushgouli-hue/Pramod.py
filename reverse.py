num = int(input("Enter a number: "))
original = num
reversed_num = 0

while num > 0:
    digit = num % 10              # get last digit
    reversed_num = reversed_num * 10 + digit
    num = num // 10               # remove last digit

print(f"Reverse of {original} is {reversed_num}")