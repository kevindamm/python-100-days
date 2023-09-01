def main():
  #1. Create a greeting for your program.
  print("TOTALLY AWESOME BAND NAME GENERATOR")
  print("===================================\n")

  #2. Ask the user for the city that they grew up in.
  city = print("Which city did you grow up in?\n")
  print()

  #3. Ask the user for the name of a pet.
  pet_name = print("The name of a pet?\n")

  #4. Combine the name of their city and pet and show them their band name.
  print("\nYour very predictable band name is " + city + " " + pet_name)

  #5. Make sure the input cursor shows on a new line:
  print()

if __name__ == "__main__":
  main()