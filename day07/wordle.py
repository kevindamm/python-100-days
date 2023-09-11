# Wordle (instead of Hangman)

import random

from allowed import allowed_words
from answers import answer_words

NUM_LIVES = 6
allowed_words += answer_words


def main():
  print(ansi_reset)
  solution = random.choice(answer_words)
  length = len(solution)
  history = []
  render([["_"]*length], solution)

  for _ in range(NUM_LIVES):
    guess = read_guess(length)
    while guess in history:
      # Retry if this word was guessed already.
      guess = read_guess(length)
    history.append(guess)
    render(history, solution)

    if guess == solution:
      print("You win!")
      return
    
    

  print("You lose. :/")


def read_guess(length):
  guess = input("Guess a word: ").strip().lower()
  while len(guess) != length or guess not in allowed_words:
    print(f"Invalid guess {guess}, try again.")
    guess = input("Guess a word: ").strip().lower()
  return guess


def render(history, solution):
  for line in history:
    output = ["  "]
    for i, ch in enumerate(line):
      if ch == solution[i]:
        output.append(fg_color(ch, "green"))
      elif ch in solution:
        output.append(fg_color(ch, "blue"))
      else:
        output.append(fg_color(ch, "white"))
    print(" ".join(output))
    print()


# Reset any previous modification to terminal output from ANSI escape sequences.
ansi_reset = "\u001b[0m"

def fg_color(text, color):
  """Color text with ANSI color escape sequences for just the Wordle colors."""
  color = {
    "red":    "\u001b[31m",
    "green":  "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue":   "\u001b[34m",
    "white":  "\u001b[37m",
  }.get(color, "\u001b[37m")  # defaults to white if unknown
  return f"{color}{text}{ansi_reset}"


if __name__ == "__main__":
  main()