class Product:
    """Simple class for product"""
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} {self.price} {self.stock}"

class Warehouse:
    """Simple class for warehouse"""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """Add product to warehouse"""
        self.products[product.name] = (product.price, product.stock)

    def remove_product(self, product):
        """Remove product from warehouse"""
        del self.products[product.name]

    def listing_products(self):
        """Listing products in warehouse"""
        for name, (price, stock) in self.products.items():
            print(f"{name} {price} {stock}\n")

    def search_product(self, name):
        """Search product in warehouse"""
        if name in self.products:
            return Product(name, price, stock)
        else:
            print(f"Product cannot be found.")
            return None

    def __str__(self):
        return "\n".join(str(product) for product in self.products)

if __name__ == "__main__":
    warehouse = Warehouse()

    while True:
        print("1. Add product")
        print("2. Remove product")
        print("3. Listing products")
        print("4. Search product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            product = Product(name, price, stock)
            warehouse.add_product(product)
            print("Product added successfully.")
        elif choice == "2":
            name = input("Enter product name: ")
            product = warehouse.search_product(name)
            if not product:
                print("The product is not in magazine.")
            else:
                warehouse.remove_product(product)
                print("Product removed successfully.")
        elif choice == "3":
            warehouse.listing_products()
        elif choice == "4":
            name = input("Enter product name: ")
            product = warehouse.search_product(name)
            if product:
                print(product)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please choose one from 1 to 5.")
            continue