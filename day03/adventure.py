"""
A kind of choose your own adventure
"""

import time 

# Yes, I borrowed this from E.T., I had to after the instructor made a reference
# to falling in the hole in that old Atari game.  She's a real OG gamer!
map = [
  ["forest"],
  ["well/1", "well/2", "well/3", "well/4"],
  ["DC/office"],
]

# WARNING: don't use global state.. we only do it in these early exercises
# because the entire program is in one file and they are not being written
# for reusability (until functions and custom types are covered it wouldn't
# really make sense to, anyway).  Try this at home, don't try it in the office.
current_pos = (1, 2)

# I would normally like to build a mapping of state transitions, like:
# transitions = {
#   "forest": transition_forest,
# ... }
#
# or maybe even inlining a lambda from state_transition["forest"][direction]
# 
# but doing so would be going 5+ days beyond the current lesson.  The lists
# above are also advanced but that will be presented in tomorrow's videos, so
# it's not so bad, kind of like the conditionals I included in yesterday's
# final exercise, tip_calc.py.  But anyway, let's make a big procedural
# nest... just try to avoid making a habit of deeply nested conditionals.
# I've split the transition functions and describe functions out so that it
# isn't too deep within a local scope.

def main_loop():
  global current_pos
  while True:
    i, j = current_pos
    location = map[i][j]

    if location == "forest":
      describe_forest()
      move = read_direction()
      transition_forest(move)
    elif location.split("/")[0] == "well":
      describe_well(location)
      move = read_direction()
      transition_well(move)
    elif location == "DC/office":
      describe_office()
      move = read_direction()
      transition_office(move)


def read_direction():
  print()
  direction = input("Which direction do you want to move? ").strip().lower()
  if direction == "east": direction = "right"
  if direction == "west": direction = "left"
  if direction == "north": direction = "up"
  if direction == "south": direction = "down"

  # TODO: could do some additional filtering here, retry on unrecognized input.
  return direction


def transition_forest(direction):
  global up, left, right

  if direction in ["left", "right", "up"]:
    if direction == "left":
      left += 1
    if direction == "right":
      right += 1
    if direction == "up":
      up += 1

    if left == up and right == up:
      print("You find a strange creature here.\n")
      response = input('"Do you want to get out of here?" they ask. ')
      if response.strip().lower() == "yes":
        print('"ok."  You blink and find yourself back in the real world.  No treasure awaits you.  No harm, either, though.\n\nTHE END', end='')
        time.sleep(2.4)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        print()
        time.sleep(0.8)
        print("or is it???")
        exit()
      else:
        print('"WHAAAAAT??" it screams, seemingly bewildered.  Then its mouth opens wider than you thought physically possible.  Almost grotesquely, it opens even wider still, as though it is battling the fiercest yawn of its life, the corners of its mouth tilting upwards, gently.. and then it eats you in one fell swallow.')
        exit(-1)
  elif direction == "down":
    current_pos = (1, 1)
  else:
    print("Hmm, I didn't understand that.  Where do you want to go? ")

# global counts for the forest "maze."
left, right, up = 0, 0, 0

def transition_well(direction):
  global current_pos
  delta = None  # if it's still None later, we didn't change it. 

  if direction == "up":
    current_pos = (0, 0)
  elif direction == "down":
    current_pos = (2, 0)
  elif direction == "left":
    delta = -1
  elif direction == "right":
    delta = +1

  if delta != None:
    _, well_pos = current_pos
    current_pos = (1, (well_pos + delta) % 4)


def transition_office(direction):
  # If the player doesn't move up immediately, they will be caught by an agent.
  if direction == "up":
    current_pos = (1, 2)
  
  else:
    print("You attempt to keep a low profile while looking for an exit when out of nowhere appears a man in a grey trenchcoat, a fedora tipped low over their face.  \"You're coming with me,\" they say as they reach their hand out towards you.  Just as you notice the taser held in their grip, its electrods spark and you feel a strange tingling sensation in your side.  You look down just as your legs collapse under you, warmth spreading to your lower body, as the world fades you hear another kzzt sound near your side.")
    print()
    print("THE END")
    time.sleep(2)
    print()
    print("No, really.  You died while they finished dissecting you.  But,.. your friends probably escaped!")
    exit(-1)

  
def describe_forest():
  print("You are in a forest surrounded by a variety of trees.  There is a path here but it intersects with another one further ahead.  Seems you could go in any direction.")

def describe_well(which):
  print("You are in some kind of rock quarry, it is too dark to see your surroundings well.  There may be holes hidden within the shadows.")
  if which == "well/1":
    print("You hear a sound in the distance, like wind chimes made of a deeply resonant metal.  It seems to be coming from the north, towards the forest.")
  elif which == "well/2":
    print("You hear something scurrying around in the darkness.  It sounds disturbingly large.")
  elif which == "well/3":
    print("You can hear the sounds of traffic and machinery not far from here.  It seems to be coming from the south.")
  elif which == "well/4":
    print("\nYou fall into a hole.  It is surprisingly deep!  It feels as though you were sliding down that last slope for at least a few seconds.  It's so dark that you nearly trip and fall over while standing up.  Almost a minute later your eyes have adjusted enough that you can just barely make out the entrance where you fell in. ", end=' ')
    response = input("What do you do? ")
    if response.find("stretch") != -1 and response.find("neck") != -1:
      print("\n\nYou stretch your neck as far as you can, hoping against any reason that it will bring you closer to that dim shaft of light emitted from above.  You strain until your neck is too tired to keep extended, and as you relax your effort, exhaling a sigh of exhaustion, your legs rise up to meet the rest of your body.  Wait, what?  You extended your neck and your body inched upwards.\n\nYou stretch your neck again, wildly thinking this can't be happening, then relax and your legs move ever slightly up.  It seems to require extended effort to make any noticeable distance.\n\n...\n\nHours later, your neck sore with fatigue, the whole length of your back from the base of your skull to the end of your vertebre are tingling with near-numbness but the hole is almost within arm's reach!  Just a little more!  You frantically try to extend your neck again but it feels like your body won't respond, and just as you start to feel gravity take its hold on you, a shifting blur out of the corner of your eye grabs your attention.  You see its tail whip in the edge of light near the mouth of this god-forsaken hole and it sends a rush of adrenaline through your body, you bolt upright and feel your whole body extend.  The hole is within reach!  You move your arms easily, they had been relatively useless until now, and scramble up and out into the shaded desolation of the quarry.")
    else:
      print("\nYou call out for help until your voice gives out.  Eventually you give up hope and die of dehydration a day later.  A cave in three years later further buries your bones and your alien presence is never discovered.")
      exit(-1)
  else:
    print("wh- what happened? where is this place? nothing looks familiar..")

def describe_office():
  print("You are assaulted with loud, bustling, and harried sounds of city life.  You see the squat concrete and glass buildings and fast-moving land vehicles.  So much smog!  Your eyes and mouth are irritated almost immediately.  You feel a rising panic swell up in your gut as you try to control your breathing and heart rate.  This place doesn't feel safe but you must keep hold of your wits.")

if __name__ == "__main__":
  main_loop()