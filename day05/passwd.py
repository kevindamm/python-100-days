# Password Generator
#
# This one has some practical use!

import random

def main():
  # Prompt user for character type distribution.
  print("Welcome to the PyPassword Generator!")
  num_letters = int(input("How many letters would you like in your password? ")) 
  num_symbols = int(input(f"How many symbols would you like? "))
  num_numbers = int(input(f"How many numbers would you like? "))

  # These ranges can be derived from the standard ASCII table.
  letters = chrange('a', 'z') + chrange('A', 'Z')
  numbers = chrange('0', '9')
  symbols = (chrange('!', '/') +
            chrange(':', '@') + 
            chrange('[', '`'))
  
  # Select the appropriate number of each character type.
  pwd = []
  for _ in range(num_letters):
    pwd.append(random.choice(letters))
  for _ in range(num_symbols):
    pwd.append(random.choice(symbols))
  for _ in range(num_numbers):
    pwd.append(random.choice(numbers))

  # Print the result after shuffling.
  random.shuffle(pwd)
  print("".join(pwd))


def chrange(start, limit):
  """Produces a string of the character range from `start` to `limit`.
  
  Includes `limit` in the output.
  """
  distance = ord(limit) - ord(start)
  return "".join([
    chr(ord(start) + ch) for ch in range(distance)])


if __name__ == "__main__":
  main()