
def get_product():
    product = input("Please enter a Product : \n")

    try:
        product = str(product)
        return product

    except ValueError:
        print("Incorrect product\n")
        return get_product()

def get_maximum_quantity():
    quantity_max = input("Please enter a Maximum Quantity\n")

    try:
        quantity_max = int(quantity_max)
        return quantity_max
    
    except ValueError:
        print("\nIncorrect Maximum Quantity\n")
        return get_maximum_quantity()

def main():
    product = get_product()
    max_quantity = get_maximum_quantity()

    print("Product is : %s" % product)
    print("Maximum Quantity is : %s" % max_quantity)

main()