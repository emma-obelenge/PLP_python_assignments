def calculate_discount(price, discount_percent):
    discount_price = (discount_percent / 100) * price
    final_price = price - discount_price
    return(final_price)

price = float(input("Enter the item original price: "))
discount = float(input("Enter the discount percentage value: "))
if(discount == None or discount < 0):
    discount = 0

#function call and discount implementation
print(f"Discount of {discount}% applied!")
print(f"Final price of item is N{calculate_discount(price, discount)}")