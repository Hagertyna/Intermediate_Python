# Iterator from a fruits tuple and print values
fruitstup = ("Lemon", "Orange", "Banana")
newit = iter(fruitstup)

# Printing each value from fruitstup
print(next(newit))  # Lemon
print(next(newit))  # Orange
print(next(newit))  # Banana

# Fruit tuple2
# iterating through string characters
fruit = "Orange"
itrator = iter(fruit)
print(next(itrator))
print(next(itrator))
print(next(itrator))
print(next(itrator))
print(next(itrator))
print(next(itrator))
print()
myfruit = "Birtukan"

for i in myfruit:
    print(i)