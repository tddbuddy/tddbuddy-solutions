import pytest
from unittest.mock import Mock, create_autospec
from bake_sale import BakeSalePos, BakeSaleInventory, IInputBuffer, IOutputBuffer

# A test builder in Python isn't necessary in the same way because Python's
# dynamic nature allows us to easily swap out components.
# However, we can still use a setup function or fixtures to achieve similar setup.

@pytest.fixture
def bake_sale_inventory():
    inventory = BakeSaleInventory()
    # Additional setup if necessary
    return inventory

@pytest.fixture
def input_buffer():
    return create_autospec(IInputBuffer)

@pytest.fixture
def output_buffer():
    return create_autospec(IOutputBuffer)

def test_in_stock_purchase(bake_sale_inventory, input_buffer, output_buffer):
    # Arrange
    input_buffer.read_purchase_input.return_value = "B"
    input_buffer.read_amount_paid.return_value = 1.00

    bake_sale = BakeSalePos(bake_sale_inventory, input_buffer, output_buffer)

    # Act
    bake_sale.process_order()

    # Assert
    output_buffer.write_message.assert_called_once_with("Change due: $0.25")

def test_out_of_stock_purchase(bake_sale_inventory, input_buffer, output_buffer):
    # Arrange
    bake_sale_inventory.update_stock("W", -bake_sale_inventory.get_quantity("W"))  # Set Water stock to 0
    input_buffer.read_purchase_input.return_value = "W"

    bake_sale = BakeSalePos(bake_sale_inventory, input_buffer, output_buffer)

    # Act
    bake_sale.process_order()

    # Assert
    output_buffer.write_message.assert_called_once_with("Water is out of stock")

def test_not_enough_money(bake_sale_inventory, input_buffer, output_buffer):
    # Arrange
    input_buffer.read_purchase_input.return_value = "C"
    input_buffer.read_amount_paid.return_value = 1.00

    bake_sale = BakeSalePos(bake_sale_inventory, input_buffer, output_buffer)

    # Act
    bake_sale.process_order()

    # Assert
    output_buffer.write_message.assert_called_once_with("Not enough money")

def test_multiple_items_in_order(bake_sale_inventory, input_buffer, output_buffer):
    # Arrange
    input_buffer.read_purchase_input.return_value = "B,M"
    input_buffer.read_amount_paid.return_value = 2.00

    bake_sale = BakeSalePos(bake_sale_inventory, input_buffer, output_buffer)

    # Act
    bake_sale.process_order()

    # Assert
    output_buffer.write_message.assert_called_once_with("Change due: $0.25")

