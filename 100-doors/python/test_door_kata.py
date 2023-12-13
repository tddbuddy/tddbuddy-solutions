import pytest
from door_kata import DoorKata 

# To ensure the best coverage with as few tests as possible, you will want to follow boundaries and equivalence partitions.
# Consider these partitions:
#
# Doors that are perfect squares, as they will be open after the 100 passes.
# Doors that are not perfect squares, as they will be closed after the 100 passes.
#
# You can choose representative doors from these partitions and test the boundaries for more thorough test coverage.
# For example, door 1 is a boundary case for perfect squares, and door 2 is a boundary case for non-perfect squares.

def test_perfect_square_boundary_doors_1_and_4():
    dk = DoorKata()
    doors = [False] * 100
    dk.run_door_kata(doors)
    assert doors[0], "Door 1 should be open"  # Door 1 (Open)
    assert doors[3], "Door 4 should be open"  # Door 4 (Open)

def test_perfect_square_inside_partition_door_9():
    dk = DoorKata()
    doors = [False] * 100
    dk.run_door_kata(doors)
    assert doors[8], "Door 9 should be open"  # Door 9 (Open)

def test_non_perfect_square_boundary_doors_2_and_3():
    dk = DoorKata()
    doors = [False] * 100
    dk.run_door_kata(doors)
    assert not doors[1], "Door 2 should be closed"  # Door 2 (Closed)
    assert not doors[2], "Door 3 should be closed"  # Door 3 (Closed)

def test_non_perfect_square_inside_partition_doors_5_and_7():
    dk = DoorKata()
    doors = [False] * 100
    dk.run_door_kata(doors)
    assert not doors[4], "Door 5 should be closed"  # Door 5 (Closed)
    assert not doors[6], "Door 7 should be closed"  # Door 7 (Closed)

