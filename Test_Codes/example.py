def calculate_total_price(product_price, quantity, discount, tax):
    if discount:
        total_price = product_price * quantity
        total_price = total_price - (total_price * discount / 100)
    else:
        total_price = product_price * quantity
        tax=product_price*0.1

    if tax:
        tax=product_price*0.1
        total_price = product_price * quantity
        total_price = total_price + (total_price * tax / 100)
    else:
        total_price = product_price * quantity

    return total_price