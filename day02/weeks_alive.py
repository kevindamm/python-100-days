# What I would have thought this prompt would be:
#
# dob = input("When were you born? (MM/DD/YYYY) ")
#... with some use of datetime lib to get the delta

age = input("What is your current age? ")

# Being optimistic here thinking that we will all live to 90?  Or pessimistic?
years_left = 90 - int(age)

count_days = years_left * 365.25
count_weeks = years_left * 52.1429 
count_months = years_left * 12

print(f"You have about {count_days} days left to learn Python -- " +
      f"that's just {count_weeks} weeks, or {count_months} months!")
print()
print("or maybe more if we science our way out of senesence, "
      "but probably not a lot more "
      "unless we find a more efficient representation than "
      "bags of meat containing mostly water.")
