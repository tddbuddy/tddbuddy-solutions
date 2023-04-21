namespace HeavyMetalBakeSale;


public class BakeSalePos
{
    private readonly IInventory _inventory;
    private readonly IInputBuffer _inputBuffer;
    private readonly IOutputBuffer _outputBuffer;

    public BakeSalePos(IInventory inventory,
                       IInputBuffer inputBuffer,
                       IOutputBuffer outputBuffer)
    {
        _inventory = inventory;
        _inputBuffer = inputBuffer;
        _outputBuffer = outputBuffer;
    }

    public void ProcessOrder()
    {
        var order = _inputBuffer.ReadPurchaseInput();
        var items = order.Split(',');

        decimal total = 0;

        // Calculate total and check stock
        foreach (var item in items)
        {
            if (_inventory.GetQuantity(item) == 0)
            {
                _outputBuffer.WriteMessage($"{_inventory.GetName(item)} is out of stock");
                return;
            }

            total += _inventory.GetPrice(item);
            _inventory.UpdateStock(item, 1);
        }

        var amountPaid = _inputBuffer.ReadAmountPaid();

        if (amountPaid < total)
        {
            _outputBuffer.WriteMessage("Not enough money");
        }
        else
        {
            decimal change = amountPaid - total;
            _outputBuffer.WriteMessage($"Change due: {change:C}");
        }
    }
}


