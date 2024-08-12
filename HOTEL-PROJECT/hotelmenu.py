#Define the menu of restaurant
menu={
    'Pizza':199,
    'Pasta':99,
    'burger':29,
    'salad':39,
    'cofee':80,
    
}
#WELCOME MASSAGE
print("WELCOME TO HIREN RESTAURANT")
print("MENU \nPizza - 40\nPasta - 50\nBurger - 60\nSalad - 70\nCofee- 80 ")

order_total = 0

item_1 = input("Enter the name of the item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print (f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet !")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2= input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available !")
print(f"The totel amount of item to pay is {order_total}")