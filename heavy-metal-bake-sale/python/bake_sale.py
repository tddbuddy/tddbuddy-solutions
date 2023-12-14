# Assuming that Python 3.6 or above is being used

class BakeSaleItem:
    def __init__(self, purchase_code, name, price, quantity):
        self.purchase_code = purchase_code
        self.price = price
        self.quantity = quantity
        self.name = name


class BakeSaleInventory:
    def __init__(self):
        self.items = {
            "B": BakeSaleItem("B", "Brownie", 0.75, 48),
            "M": BakeSaleItem("M", "Muffin", 1.00, 36),
            "C": BakeSaleItem("C", "Cake Pop", 1.35, 24),
            "W": BakeSaleItem("W", "Water", 1.50, 30),
        }

    def get_quantity(self, purchase_code):
        return self.items[purchase_code].quantity

    def get_price(self, purchase_code):
        return self.items[purchase_code].price

    def get_name(self, purchase_code):
        return self.items[purchase_code].name

    def update_stock(self, purchase_code, quantity):
        self.items[purchase_code].quantity += quantity


class IInputBuffer:
    def read_purchase_input(self):
        raise NotImplementedError

    def read_amount_paid(self):
        raise NotImplementedError


class IOutputBuffer:
    def write_message(self, message):
        raise NotImplementedError


class BakeSalePos:
    def __init__(self, inventory, input_buffer, output_buffer):
        self.inventory = inventory
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer

    def process_order(self):
        order = self.input_buffer.read_purchase_input()
        items = order.split(',')

        total = 0

        # Calculate total and check stock
        for item in items:
            if self.inventory.get_quantity(item) <= 0:
                self.output_buffer.write_message(f"{self.inventory.get_name(item)} is out of stock")
                return

            total += self.inventory.get_price(item)
            self.inventory.update_stock(item, 1)

        amount_paid = self.input_buffer.read_amount_paid()

        if amount_paid < total:
            self.output_buffer.write_message("Not enough money")
        else:
            change = amount_paid - total
            self.output_buffer.write_message(f"Change due: ${change:.2f}")

