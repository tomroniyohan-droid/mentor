cart = {}

def add_item(item, price):
    cart[item] = price
    print(item, "added to cart")

def remove_item(item):
    if item in cart:
        del cart[item]
        print(item, "removed from cart")
    else:
        print("Item not found")

def calculate_total():
    total = sum(cart.values())
    return total

def apply_discount(total, discount):
    return total - (total * discount / 100)

add_item("Laptop", 50000)
add_item("Mouse", 500)
add_item("Keyboard", 1500)

remove_item("Mouse")

total = calculate_total()
print("Total Bill:", total)

final_amount = apply_discount(total, 10)
print("Final Amount after Discount:", final_amount)
