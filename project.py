menu={'chicken':99,'rice':20,'soup':10,'bread':5,'mutton':150} 
print("welcome to Black Burner") 
print("chicken:Rs99\n rice:Rs20\n soup:Rs10\n bread:Rs5\n mutton:Rs150") 
order_total=0 
item_1=input("Enter your first item=")
if item_1 in menu: 
    order_total+=menu[item_1] 
    print(f"your first item has been added to the cart") #see when i add such srings after adding f that means we are writing formatted string
else:
    print("please order from the menu only")
another_order=input("Do you want to order another item? (yes/no)")
if another_order=='yes': 
    item_2=input("Enter your second item=") 
    if item_2 in menu: 
        order_total+=menu[item_2] 
        print(f"your second item has been added to the cart") 
    else: 
        print("please order from the menu only")  

print(f"Your total order amount is: Rs{order_total}") #well i am intentionllly leaving thishdere see this project ahs 2 mistakes first is you cant add more than two iems and second is you cant add more than 1piece/plate of thse same item.
