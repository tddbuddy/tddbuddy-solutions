import pytest
from bake_sale import BakeSale  # Replace with your actual module and class names

def test_total_calculation():
    bake_sale = BakeSale()
    assert bake_sale.process_order("B,C,W", 4.00) == "Change: $0.40"

def test_exact_amount():
    bake_sale = BakeSale()
    assert bake_sale.process_order("B", 0.75) == "Change: $0.00"

def test_insufficient_payment():
    bake_sale = BakeSale()
    assert bake_sale.process_order("C,M", 2.00) == "Not enough money"

def test_out_of_stock():
    bake_sale = BakeSale()
    # Simulate purchasing all water bottles
    for _ in range(30):
        bake_sale.process_order("W", 1.50)
    assert bake_sale.process_order("W", 1.50) == "Water is out of stock"

def test_invalid_code():
    bake_sale = BakeSale()
    assert bake_sale.process_order("Z", 1.00) == "Invalid item code"

