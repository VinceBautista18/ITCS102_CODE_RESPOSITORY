print("    TINDAHAN NI ALING NENA ")
print("|-----------------------------|")

name = input("What is your name? --> ")
item = input("What is your order? --> ")

fragile_input = input("Is it fragile? (yes/no) --> ")
if fragile_input == "yes":
  is_fragile = True
else:
  is_fragile = False

weight = float(input("How heavy is it in kg? --> "))
distance = float(input("How far is the destination in km? --> "))

express_input = input("Is it in a hurry (express)? (yes/no) --> ")
if express_input == "yes":
  is_express = True
else:
  is_express = False

international_input = input("Is it international? (yes/no) --> ")
if international_input == "yes":
  is_international = True
else:
  is_international = False

base_cost = (weight * 2.5) + (distance * 0.15)

if (
    distance <= 100
    and weight <= 2
    and not is_express
    and not is_international
):
  total = 0
elif is_international and is_express:
  total = (base_cost * 1.4) + 50
elif weight > 20 and (is_international or is_express):
  total = (base_cost * 1.2) + 25
elif distance > 1000 or weight > 30:
  total = base_cost + 30
else:
  total = base_cost

if total == 0:
  shipping_fee = 0
else:
  shipping_fee = total - base_cost

print("Sender:", name)
print("Order:", item)
print("Fragile:", is_fragile)
print("Weight:", weight, "kg")
print("Distance:", distance, "km")
print("Express:", is_express)
print("International:", is_international)
print("Base Cost: PHP", base_cost)
print("Shipping Fee: PHP", shipping_fee)
print("Total: PHP", total)
