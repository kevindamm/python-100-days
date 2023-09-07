import random

response = input("Who is putting their card into the bowl? (comma-separated names) ")
bankers = [banker.strip() for banker in response.split(",")]

# payer = random.choice(bankers)
person_who_will_pay = bankers[random.randint(0, len(bankers)-1)]

print(f"{person_who_will_pay} will pay the bill.")