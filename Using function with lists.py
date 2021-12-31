food=["hamburger", "pizza", "juice", "frices", "sushi"]
prices=[5.64,3.92,7.29,4.95,3.28]


print("\n")

print(food)

print("\n")

food.insert(2,"grapes")
print(food)

print("\n")

food.extend(prices)
print(food)

print("\n")

print(food.index("pizza"))

print("\n")

print(food.index("juice"))
print("\n")

food.clear()
print(food)