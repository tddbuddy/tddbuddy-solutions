import pytest
from unittest.mock import Mock, call

# Import the classes under test from their module
from char_copy import Copier, ISource, IDestination

# Test that a ValueError is raised when source is None
def test_ctor_given_null_source_should_raise_value_error():
    destination = Mock(spec=IDestination)
    with pytest.raises(ValueError) as e:
        Copier(None, destination)
    assert "Source and destination cannot be None" in str(e.value)

# Test that a ValueError is raised when destination is None
def test_ctor_given_null_destination_should_raise_value_error():
    source = Mock(spec=ISource)
    with pytest.raises(ValueError) as e:
        Copier(source, None)
    assert "Source and destination cannot be None" in str(e.value)

# Test copying a single character
def test_copy_given_single_char_should_copy_char():
    source = Mock(spec=ISource)
    destination = Mock(spec=IDestination)
    source.read_char.side_effect = ['a', '\n']
    copier = Copier(source, destination)
    
    copier.copy()

    source.read_char.assert_has_calls([call(), call()])
    destination.write_char.assert_called_once_with('a')

# Test copying multiple characters until a newline is encountered
def test_copy_given_many_chars_should_copy_all_chars_until_newline():
    source = Mock(spec=ISource)
    destination = Mock(spec=IDestination)
    source.read_char.side_effect = ['a', 'b', 'c', 'd', '\n']
    copier = Copier(source, destination)

    copier.copy()

    assert source.read_char.call_count == 5
    expected_calls = [call('a'), call('b'), call('c'), call('d')]
    destination.write_char.assert_has_calls(expected_calls, any_order=False)
