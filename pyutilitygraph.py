import matplotlib.pyplot as plt

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

def get_utility(max_quantity, product):
    i = 1
    utility = {}
    while i <= max_quantity:
        result = input("For %d %s what added happiness do you get ?\n" % (i,product))
        utility[i] = int(result)
        i = i + 1
    print(utility)
    quantity = list(utility.keys())
    hapiness = list(utility.values())
    plt.plot(quantity, hapiness)
    print(quantity)
    print(hapiness)
    plt.show()

def main():
    product = get_product()
    max_quantity = get_maximum_quantity()

    print("Product is : %s" % product)
    print("Maximum Quantity is : %s" % max_quantity)
    get_utility(max_quantity, product)

main()