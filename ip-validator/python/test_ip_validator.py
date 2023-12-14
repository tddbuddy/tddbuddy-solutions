import pytest
from ip_validator import IpValidator  # Replace 'your_module' with the actual name of your Python module

# Test data for each category
BASIC_FORMAT_TESTS = [
    ("1.1.1.1", True),
    ("192.168.1.1", True),
    ("10.0.0.1", True),
    ("127.0.0.1", True)
]

RANGE_TESTS = [
    ("256.1.1.1", False),
    ("192.300.1.1", False),
    ("10.0.0.256", False)
]

LEADING_ZERO_TESTS = [
    ("01.1.1.1", False),
    ("192.168.01.1", False),
    ("10.0.0.01", False)
]

NETWORK_BROADCAST_ADDRESS_TESTS = [
    ("192.168.1.0", False),
    ("0.0.0.0", False),
    ("255.255.255.255", False)
]

EDGE_CASE_TESTS = [
    (None, False),
    ("", False),
    (" ", False),
    ("not.an.ip", False),
    ("1234.1234.1234.1234", False),
    ("....", False)
]

@pytest.mark.parametrize("ip_address,expected_result", BASIC_FORMAT_TESTS)
def test_validate_ipv4_address_basic_format(ip_address, expected_result):
    # Arrange
    validator = IpValidator()

    # Act
    actual = validator.validate_ipv4_address(ip_address)

    # Assert
    assert actual == expected_result

@pytest.mark.parametrize("ip_address,expected_result", RANGE_TESTS)
def test_validate_ipv4_address_range(ip_address, expected_result):
    # Arrange
    validator = IpValidator()
    
    # Act
    actual = validator.validate_ipv4_address(ip_address)

    # Assert
    assert actual == expected_result

@pytest.mark.parametrize("ip_address,expected_result", LEADING_ZERO_TESTS)
def test_validate_ipv4_address_leading_zero(ip_address, expected_result):
    # Arrange
    validator = IpValidator()

    # Act
    actual = validator.validate_ipv4_address(ip_address)

    # Assert
    assert actual == expected_result

@pytest.mark.parametrize("ip_address,expected_result", NETWORK_BROADCAST_ADDRESS_TESTS)
def test_validate_ipv4_address_network_broadcast(ip_address, expected_result):
    # Arrange
    validator = IpValidator()

    # Act
    actual = validator.validate_ipv4_address(ip_address)

    # Assert
    assert actual == expected_result

@pytest.mark.parametrize("ip_address,expected_result", EDGE_CASE_TESTS)
def test_validate_ipv4_address_edge_cases(ip_address, expected_result):
    # Arrange
    validator = IpValidator()

    # Act
    actual = validator.validate_ipv4_address(ip_address)

    # Assert
    assert actual == expected_result

