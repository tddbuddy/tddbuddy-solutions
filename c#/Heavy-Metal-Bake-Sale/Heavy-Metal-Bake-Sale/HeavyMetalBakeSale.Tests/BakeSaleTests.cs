using NSubstitute;

namespace HeavyMetalBakeSale.Tests;

public class Tests
{
    [TestFixture]
    public class BakeSaleTests
    {
        [Test]
        public void TestInStockPurchase()
        {
            // Arrange
            var inputBuffer = Substitute.For<IInputBuffer>();
            inputBuffer.ReadPurchaseInput().Returns("B");
            inputBuffer.ReadAmountPaid().Returns(1.00m);

            var outputBuffer = Substitute.For<IOutputBuffer>();

            var bakeSale = new BakeSaleTestBuilder()
                .WithInputBuffer(inputBuffer)
                .WithOutputBuffer(outputBuffer)
                .Build();

            // Act
            bakeSale.ProcessOrder();

            // Assert
            outputBuffer.Received().WriteMessage("Change due: $0.25");
        }

        [Test]
        public void TestOutOfStockPurchase()
        {
            // Arrange
            var inventory = new BakeSaleInventory();
            inventory.UpdateStock("W", -inventory.GetQuantity("W")); // Set Water stock to 0

            var inputBuffer = Substitute.For<IInputBuffer>();
            inputBuffer.ReadPurchaseInput().Returns("W");

            var outputBuffer = Substitute.For<IOutputBuffer>();

            var bakeSale = new BakeSaleTestBuilder()
                .WithInventory(inventory)
                .WithInputBuffer(inputBuffer)
                .Build();

            // Act
            bakeSale.ProcessOrder();

            // Assert
            outputBuffer.WriteMessage("Water is out of stock");
        }

        [Test]
        public void TestNotEnoughMoney()
        {
            // Arrange
            var inputBuffer = Substitute.For<IInputBuffer>();
            inputBuffer.ReadPurchaseInput().Returns("C");
            inputBuffer.ReadAmountPaid().Returns(1.00m);

            var outputBuffer = Substitute.For<IOutputBuffer>();

            var bakeSale = new BakeSaleTestBuilder()
                .WithInputBuffer(inputBuffer)
                .WithOutputBuffer(outputBuffer)
                .Build();

            // Act
            bakeSale.ProcessOrder();

            // Assert
            outputBuffer.Received().WriteMessage("Not enough money");
        }

        [Test]
        public void TestMultipleItemsInOrder()
        {
            // Arrange
            var inputBuffer = Substitute.For<IInputBuffer>();
            inputBuffer.ReadPurchaseInput().Returns("B,M");
            inputBuffer.ReadAmountPaid().Returns(2.00m);

            var outputBuffer = Substitute.For<IOutputBuffer>();

            var bakeSale = new BakeSaleTestBuilder()
                .WithInputBuffer(inputBuffer)
                .WithOutputBuffer(outputBuffer)
                .Build();

            // Act
            bakeSale.ProcessOrder();

            // Assert
            outputBuffer.Received().WriteMessage("Change due: $0.25");
        }
    }
}
