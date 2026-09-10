name = input("Input Sender name ----> ")

type = input("Input Type of Item ----> ")

is_Fragile = bool(input("Is the Product Fragile?( Enter \"yes\" if yes, press Enter if no) -----> "))

weight = float(input("Weight of the product? (in kg) ----> "))

distance = float(input("Distance? (in km) ----->"))

is_Express = bool(input("Is it Expres? (Enter \"yes\" if yes, press Enter if no) ----> "))

is_International = bool(input("Is it International? (Enter \"yes\" if yes, press Enter if no) ---> "))

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2 and distance  <= 100 and is_Express == False and is_International == False :
	print("FREE SHIPPING")
	Total = 0

elif is_International == True and is_Express == True :
	print("Package is Express or Heavy International is applied")
	Total = (base_cost * 1.2) + 50

elif is_Express == True or (is_International == True and weight > 20):
	print("Package is Express or Heavy International is applied") 
	Total = (base_cost * 1.2) + 25

elif weight > 30 or distance > 1000 :
	print("Oversized is applied")
	Total = base_cost + 30

else:
	Total = base_cost
	print("Standard rate is applied")
	

print ("Hi, ",name, ", how are you doing today ?")

print ("Your ",type, ",order is confirmed ")

print("Total Output : PHP ", Total)



