import pytest
from mars_rover import MarsRover

def test_move_forward():
    rover = MarsRover([0, 0], 'S', [100, 100])
    rover.execute_commands('f')
    assert rover.current_location() == (0, 1)

def test_move_backward():
    rover = MarsRover([0, 1], 'N', [100, 100])
    rover.execute_commands('b')
    assert rover.current_location() == (0, 2)

def test_turn_left():
    rover = MarsRover([0, 0], 'N', [100, 100])
    rover.execute_commands('l')
    assert rover.current_direction() == 'W'

def test_turn_right():
    rover = MarsRover([0, 0], 'N', [100, 100])
    rover.execute_commands('r')
    assert rover.current_direction() == 'E'

def test_wrapping():
    rover = MarsRover([99, 99], 'S', [100, 100])
    rover.execute_commands('f')
    assert rover.current_location() == (99, 0)

def test_mixed_commands():
    rover = MarsRover([0, 0], 'N', [100, 100])
    rover.execute_commands('ffrblfl')
    assert rover.current_location() == (1, 97)
    assert rover.current_direction() == 'W'

def test_reverse_wrapping_facing_north():
    rover = MarsRover([0, 0], 'N', [100, 100])
    rover.execute_commands('b')
    assert rover.current_location() == (0, 1)

def test_reverse_wrapping_facing_south():
    rover = MarsRover([0, 0], 'S', [100, 100])
    rover.execute_commands('b')
    assert rover.current_location() == (0, 99)

def test_invalid_start_direction():
    with pytest.raises(ValueError):
        MarsRover([0, 0], 'X', [100, 100])

def test_invalid_commands():
    rover = MarsRover([0, 0], 'S', [100, 100])
    with pytest.raises(ValueError) as excinfo:
        rover.execute_commands('fxgx')

    assert "Unknown command" in str(excinfo.value)

def test_full_rotation():
    rover = MarsRover([0, 0], 'N', [100, 100])
    rover.execute_commands('llll')
    assert rover.current_direction() == 'N'  # Full rotation left
    rover.execute_commands('rrrr')
    assert rover.current_direction() == 'N'  # Full rotation right
