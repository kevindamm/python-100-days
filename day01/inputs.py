# hey there
name = input("What is your name? ")

print("Hello " + name)
print(f"Your name has {len(name)} letters!")

# SWAPPER
a = input("a: ")
b = input("b: ")
print()

# We can also swap by packing into a tuple and unpacking in swapped order.
a, b = b, a

print("...after swapping:")
a = print(f"a = {a}")
b = print(f"b = {b}")
