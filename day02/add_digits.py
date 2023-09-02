# Write a program that adds the digits in a number

num = input("Enter a number: ")

total = 0
try:
  for ch in str(num):
    total += int(ch)
  print(total)
except:
  print("I ASKED FOR A NUMBER.")
