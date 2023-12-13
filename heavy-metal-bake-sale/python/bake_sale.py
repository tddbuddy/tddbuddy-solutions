class BakeSaleItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class BakeSale:
    def __init__(self):
        self.items = {
            "B": BakeSaleItem("Brownie", 0.75, 48),
            "M": BakeSaleItem("Muffin", 1.00, 36),
            "C": BakeSaleItem("Cake Pop", 1.35, 24),
            "W": BakeSaleItem("Water", 1.50, 30)
        }

    def process_order(self, order_codes, amount_paid):
        total_cost = 0
        for code in order_codes.split(','):
            item = self.items.get(code)
            if item and item.quantity > 0:
                total_cost += item.price
                item.quantity -= 1
            else:
                return f"{item.name if item else 'Item'} is out of stock" if item else "Invalid item code"

        if total_cost > amount_paid:
            return "Not enough money"
        return f"Change: ${amount_paid - total_cost:.2f}"

