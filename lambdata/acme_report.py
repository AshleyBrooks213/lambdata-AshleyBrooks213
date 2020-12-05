import random
from acme import Product


NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']


def generate_products(num_products=30):
    products = []

    for n in range(num_products):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products.append([name, price, weight, flammability])

    return products


def inventory_report(products):
    """number of products in our list"""
    number_of_products = len(products)

    """number of unique product names"""
    """products is a list of products"""
    product_names = [prod.name for prod in products]
    """turn into set to remove duplicates"""
    unique_product_names = set(product_names)

    """get the price for each product in our list of products"""
    product_prices = [prod.price for prod in products]

    """get the mean for these prices"""
    """mean = sum of prices / total number of products"""
    sum_of_prices = sum(product_prices)
    avg_price = sum_of_prices / number_of_products

    product_weights = [prod.weight for prod in products]
    sum_of_weights = sum(product_weights)
    avg_weight = sum_of_weights / number_of_products

    
    product_flams = [prod.flam for prod in products]
    sum_of_flams = sum(product_flammability)
    avg_flam = sum_of_flams / number_of_products


    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique Product Names:", unique_product_names)
    print("Avg. Price:", avg_price)
    print("Avg. Weight:", avg_weight)
    print("Avg. Flammability:", avg_flam)




if __name__ == '__main__':
    inventory_report(generate_products())

