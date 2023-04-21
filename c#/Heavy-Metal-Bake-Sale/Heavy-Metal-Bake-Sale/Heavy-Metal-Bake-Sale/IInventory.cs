namespace HeavyMetalBakeSale;

public interface IInventory
{
    int GetQuantity(string purchaseCode);
    decimal GetPrice(string purchaseCode);
    string GetName(string purchaseCode);
    void UpdateStock(string purchaseCode, int quantity);
}

