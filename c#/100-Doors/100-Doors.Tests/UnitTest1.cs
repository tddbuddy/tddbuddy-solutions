using System;
using NUnit.Framework;
using DoorKataLib;

namespace DoorKataLib.Tests
{
    /*
     * To ensure the best coverage with as few tests as possible you will want to follow boundaries and equivalence partitions. 
     * Consider these partitions:
     * 
     * Doors that are perfect squares, as they will be open after the 100 passes.
     * Doors that are not perfect squares, as they will be closed after the 100 passes.
     * 
     * You can choose representative doors from these partitions and test the boundaries for more thorough test coverage. 
     * For example, door 1 is a boundary case for perfect squares, and door 2 is a boundary case for non-perfect squares. 
     */

    [TestFixture]
    public class DoorKataTests
    {
        [Test]
        public void TestPerfectSquareBoundary_Doors1And4()
        {
            // Arrange
            bool[] doors = new bool[100];

            // Act
            new DoorKata().RunDoorKata(doors);

            // Assert
            Assert.IsTrue(doors[0], "Door 1 should be open"); // Door 1 (Open)
            Assert.IsTrue(doors[3], "Door 4 should be open"); // Door 4 (Open)
        }

        [Test]
        public void TestPerfectSquareInsidePartition_Door9()
        {
            // Arrange
            bool[] doors = new bool[100];

            // Act
            new DoorKata().RunDoorKata(doors);

            // Assert
            Assert.IsTrue(doors[8], "Door 9 should be open"); // Door 9 (Open)
        }

        [Test]
        public void TestNonPerfectSquareBoundary_Doors2And3()
        {
            // Arrange
            bool[] doors = new bool[100];

            // Act
            new DoorKata().RunDoorKata(doors);

            // Assert
            Assert.IsFalse(doors[1], "Door 2 should be closed"); // Door 2 (Closed)
            Assert.IsFalse(doors[2], "Door 3 should be closed"); // Door 3 (Closed)
        }

        [Test]
        public void TestNonPerfectSquareInsidePartition_Doors5And7()
        {
            // Arrange
            bool[] doors = new bool[100];

            // Act
            new DoorKata().RunDoorKata(doors);

            // Assert
            Assert.IsFalse(doors[4], "Door 5 should be closed"); // Door 5 (Closed)
            Assert.IsFalse(doors[6], "Door 7 should be closed"); // Door 7 (Closed)
        }
    }
}
