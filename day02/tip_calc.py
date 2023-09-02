"""tip_calc.py - A tip calculator as a command-line interpreter.

Okay, this goes a little bit beyond what has been covered so far, but it may
still be useful to see what the same exercise coded with a little more caution
to bad inputs might look like.
"""

DEFAULT_TIP_PERCENT = 18
DEFAULT_GROUP_SIZE = 2

def main():
  subtotal = read_subtotal()
  tip_percent = read_tip_percent(DEFAULT_TIP_PERCENT)
  group_size = read_group_size(DEFAULT_GROUP_SIZE)

  per_person, tip_amount = calculate_tip(subtotal, tip_percent, group_size)
  per_person_string = "{:.2f}".format(per_person)
  diff_string = "{:.2f}".format(tip_amount)
  subtotal_string = "{:.2f}".format(per_person - tip_amount)

  print(f"Each person should pay {per_person_string} "+
        f"({subtotal_string} + {diff_string})")


def calculate_tip(subtotal, tip_percent, group_size):
  """Calculate the (per_person, tip) amounts from the provided parameters.

  Parameters:
    subtotal: the total of the bill before splitting it and adding tips
    tip_percent: a [1-100] value indicating the amount to tip as a percentage
    group_size: (int) how many people are in the party
  
  Returns:
    (tuple) per_person, tip_amount
  """
  adjustment = 1 + tip_percent/100
  total = subtotal * adjustment

  per_person = total / group_size
  subtotal_per_person = subtotal / group_size
  diff = round(per_person - subtotal_per_person, 2)

  return per_person, diff


# TODO? factor out the common pattern of read-input-with-retry

def read_subtotal():
  """Prompts the user for the bill's total amount and returns it as an int.
  
  Returns:
    (int) the bill's subtotal (after taxes, before tip and split)
  """
  subtotal = None
  while not subtotal:
    subtotal = input("What was the amount for the bill? $")
    if not subtotal.strip():
      print("Nothing entered.  retrying...")
      continue

    try:
      subtotal = float(subtotal)
    except:
      print("Hmm, I was expecting a number (integer or floating point).  "
            "retrying...")
      subtotal = None
    
  return subtotal


def read_tip_percent(default=None):
  """Prompts the user for a tip percentage and returns it as a float.
  
  Returns:
    (float) a percentage value to add to the subtotal
  """
  tip_percent = None
  # Normally we would prefer to compare directly to None but we also want to
  # reject zero values in this case, and Python does a conversion to bool here.
  while not tip_percent:
    tip_percent = input("What percentage tip would you like to give? " +
                        f"[{default}] " if default else "")
    if not tip_percent.strip():
      print("Nothing entered.")
      tip_percent = default
      if default:
        print(f"Using default value {default}")
      else:
        print("retrying...")
      continue

    try:
      tip_percent = float(tip_percent)
    except:
      # Can't convert, try again.
      print(f"Hmm, there was a problem converting {tip_percent}")
      tip_percent = default
      if default:
        print(f"Using default value {default}")
      else:
        print("retrying...")
  return tip_percent


def read_group_size(default=None):
  """Prompts the user for a group size and returns it as an int.
  
  If there is an issue with parsing the group size, a default value is used.  If
  no default was provided, it will retry prompting the user.

  Returns:
    (int) the number of people involved in paying
  """
  group_size = None
  # Normally we would prefer to compare directly to None but we also want to
  # reject zero values in this case, and Python does a conversion to bool here.
  while not group_size:
    group_size = input("How many people to split the bill? " +
                       f"[{default}] " if default else "")
    if not group_size.strip():
      print("Nothing entered.")
      group_size = default
      if default:
        print(f"Using default value {default}")
      else:
        print("retrying...")
      continue

    try:
      group_size = int(group_size)
    except:
      # Can't convert, try again.
      print(f"Hmm, there was a problem converting {group_size}")
      group_size = default
      if default:
        print(f"Using default value {default}")
      else:
        print("retrying...")
  return group_size


if __name__ == "__main__":
  main()