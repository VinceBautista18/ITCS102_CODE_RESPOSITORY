
name = input("Input your name ----> ")
age = int(input("Input your age ----> "))

print("Hi," ,name, "That age is considered as ")

if age >= 1 and age <= 5 :
	print("INFANT")

elif age >= 6 and age <= 12 :
	print("KID")

elif age >= 13 and age <= 19 :
	print("TEENAGER")

elif age >= 20 and age <= 29 :
	print("EARLY ADULTHOOD")

elif age >= 30 and age <= 45 :
	print("ADULT")

elif age >= 46 and age <= 59 :
	print("ADVANCE ADULTHOOD")

elif age >= 60 and age <= 150 :
	print("SENIOR")

else :
	print("INVALID")