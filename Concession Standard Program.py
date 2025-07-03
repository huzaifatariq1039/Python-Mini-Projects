menu = {"Pizza" : 3.00,
        "Burger" : 1.50,
        "Pulao" : 5.00,
        "Mutoon" : 10.00,
        "Beef" : 12.00,
        "Biryani" : 2.50}
cart =[]
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")

print("---------------------------")
while True:
    food = input("Select an item(q for quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("---------------------------")
print(" YOUR ORDER         ")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is ${total:2f}")