name = input("Input Sender name ----> ")

type = input("Input Type of Item ----> ")

is_Fragile = bool(input("Is the Product Fragile? -----> "))

if is_Fragile:
	base_cost += 10

weight = float(input("Weight of the product in kg? ----> "))

distance = float(input("How far is the buyer in km? ----->"))

is_Express = bool(input("Is it Expres? ----> "))

if is_Express:
	base_cost += 20

is_International = bool(input("Is it International> ---> "))

if is_International:
	base_cost += 50

base_cost = (weight * 2.50) + (distance * 0.15)

if Total >= (base_cost * 1.40) + 50

Total = (base_cost * 1.20) + 25

Total = base_cost + 30

Tota = base_cost


print ("Hi, ",name, ", how are you doing today ?")

print ("Your ",type, ",order is confirmed ")

if is_Fragile == True:
	print ("Baka mabasag to ingatan nyo")

else:
	print("Kahit ibalibag nyo yan")

print = weight

print = distance

if is_Express == True:
	print ("Ipriority nyo to")

else:
	print("kahit ihuli nyo pa yan")

if is_International == True:
	print ("Galing pa ito sa China")

else:
	print("Dito lang yan sa pinas")

print("Expected Output", Total)




