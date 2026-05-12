# Define the menu of restaurant.    
# Welcome to our 0
Menu={
      'Pizza':200,
      'Pasta':150,
      'Burger':80,
      'Sandwich':60,
      'Coffee':30
     }
print(Menu)

#Greet Customer

print("Welcome to Python Restaurant")
print("Pizza: Rs.200\nPasta: Rs.150\nBurger: Rs.80\nSandwich: Rs.60\nCoffee: Rs.30")      #( \n ) manage in a sequencial way 

order_total = 0

item1 = input("enter the name of item you want to order")
if item1 in Menu:
    order_total += Menu[item1]        # 0 + 200
    print("your item {item1} has been added to your order")

else:
    print("Ordered item {item1} is not avaialable yet")

another_order = input("Do you  want to add other item?  (Yes/No)")
if another_order=="Yes":
    item2=input("Enter a name of second item = ")
    if item2 in Menu:
        order_total += Menu[item2]
        print(f"item {item2} has been added to order ")
    
    else:
        print("ordered item {item2} is not avaialable")
    
print("Total amount of item to pay is {order_total} ")