using NSubstitute;

namespace HeavyMetalBakeSale.Tests;

public class BakeSaleTestBuilder
{
    private IInventory _inventory = new BakeSaleInventory();
    private IInputBuffer _inputBuffer = Substitute.For<IInputBuffer>();
    private IOutputBuffer _outputBuffer = Substitute.For<IOutputBuffer>();

    public BakeSaleTestBuilder WithInventory(IInventory inventory)
    {
        _inventory = inventory;
        return this;
    }

    public BakeSaleTestBuilder WithInputBuffer(IInputBuffer inputBuffer)
    {
        _inputBuffer = inputBuffer;
        return this;
    }

    public BakeSaleTestBuilder WithOutputBuffer(IOutputBuffer outputBuffer)
    {
        _outputBuffer = outputBuffer;
        return this;
    }

    public BakeSalePos Build()
    {
        return new BakeSalePos(_inventory, _inputBuffer, _outputBuffer);
    }
}
