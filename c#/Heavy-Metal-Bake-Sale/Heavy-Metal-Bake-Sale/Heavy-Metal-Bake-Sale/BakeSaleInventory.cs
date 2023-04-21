namespace HeavyMetalBakeSale;

public class BakeSaleInventory : IInventory
{
    private readonly Dictionary<string, BakeSaleItem> _items;

    public BakeSaleInventory()
    {
        _items = new Dictionary<string, BakeSaleItem>
        {
            { "B", new BakeSaleItem { PurchaseCode = "B", Name = "Brownie", Price = 0.75m, Quantity = 48 } },
            { "M", new BakeSaleItem { PurchaseCode = "M", Name = "Muffin", Price = 1.00m, Quantity = 36 } },
            { "C", new BakeSaleItem { PurchaseCode = "C", Name = "Cake Pop", Price = 1.35m, Quantity = 24 } },
            { "W", new BakeSaleItem { PurchaseCode = "W", Name = "Water", Price = 1.50m, Quantity = 30 } },
        };
    }

    public int GetQuantity(string purchaseCode)
    {
        return _items[purchaseCode].Quantity;
    }

    public decimal GetPrice(string purchaseCode)
    {
        return _items[purchaseCode].Price;
    }

    public string GetName(string purchaseCode)
    {
        return _items[purchaseCode].Name;
    }

    public void UpdateStock(string purchaseCode, int quantity)
    {
        _items[purchaseCode].Quantity -= quantity;
    }
}

