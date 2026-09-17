cart = []
prices = {
    "laptop": 500000,
    "mouse": 20000,
    "keyboard": 30000
}

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter item name: ") . strip() . lower()
        if item in prices:
            cart.append(item)
            print(item, "added to cart.")
        else:
            print("Item not available.")
    elif choice == "2":
        item = input ("Enter item name: ") . strip() . lower()
        if item in prices:
            cart.remove(item)
            print (item, "has been removed")
        else:
            print("Item not found")   
    elif choice == "3":
        print("\n Cart:")
        for item in cart:
            print(item, "-", prices[item])
    elif choice == "4":
        total = 0
        for item in cart:
            total += prices[item]
        print("\nTotal amount:", total)
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid option. Please try again.")