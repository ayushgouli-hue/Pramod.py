items = ["red", "blue", "green", "red", "yellow"]

seen = set()
duplicate = None

for item in items:
    if item in seen:
        duplicate = item
        break
    seen.add(item)

if duplicate:
    print("Duplicate found:", duplicate)
else:
    print("No duplicates found.")
    