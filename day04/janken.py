# Rock, Paper, Scissors

import random

ROCK = 0
PAPER = 1
SCISSORS = 2

view = [
  ["✊", "✊🏻", "✊🏼", "✊🏽", "✊🏾", "✊🏿"],
  ["✋", "✋🏻", "✋🏼", "✋🏽", "✋🏾", "✋🏿"],
  ["️✌️", "✌🏻", "✌🏼", "✌🏽", "✌🏾", "✌🏿"],
]

def main():
  skin_tone = read_tone()
  while True:
    choice = parse_choice(input("\nWhat do you choose? (rock, paper or scissors) "))
    cpu_choice = random.choice([ROCK, PAPER, SCISSORS])
  
    print(f"{view[choice][skin_tone]} v {view[cpu_choice][0]}")
    if beats(choice, cpu_choice):
      print("You win!")
    elif beats(cpu_choice, choice):
      print("oof, they win\n")
      keep_going = input("play again? ")
      if keep_going.stripl().lower()[0] == 'y':
        continue
    else:
      print("a draw! let's go again\n")
      continue
  
    break


def beats(left, right):
  if left == SCISSORS and right == PAPER:
    return True
  if left == PAPER and right == ROCK:
    return True
  if left == ROCK and right == SCISSORS:
    return True
  
  # Rather than determine the full ternary (true, false, equal) we only test
  # for one side (left > right) and leave the alternative consequence to the
  # caller.  This not only simplifies the current function it is still the
  # same number of comparisons!  It has an additional function call, but we're
  # aiming for readability here and not optimizing for fractions of milliseconds
  # in code that will be run a handful of times.  Sometimes simpler is good!
  return False


def parse_choice(input_string):
  norm_str = input_string.strip().lower()
  if norm_str == "rock":
    return ROCK
  if norm_str == "paper":
    return PAPER
  if norm_str == "scissor" or norm_str == "scissors":
    return SCISSORS

  print("yeah.. I didn't understand that.  I'll pick for you.")
  choice = random.randint(ROCK, SCISSORS)
  return choice


def read_tone():
  choice = input("Select a color tone [0..5] ")
  try:
    ichoice = int(choice)
    if 0 <= ichoice and ichoice < len(ROCK):
      return ichoice
    return 0
  except:
    return 0


if __name__ == "__main__":
  main()