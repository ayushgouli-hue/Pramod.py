text = input("Enter a string: ")

seen = set()
first_repeat = None

for char in text:
    if char in seen:
        first_repeat = char
        break
    seen.add(char)

if first_repeat:
    print("First repeated character:", first_repeat)
else:
    print("No repeated character found.")