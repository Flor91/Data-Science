print("List comprehension")
a = [1, 3, 5, 7, 9, 11]

print([i - 1 for i in a])

print("Set comprehension")
b = {"abc", "def"}

print({s.upper() for s in b})

print("Dict comprehension")
c = {"name": "Pooka", "age": 5}

print({v: k for k, v in c.items()})
