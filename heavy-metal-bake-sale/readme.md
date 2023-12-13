# Heavy Metal Bake Sale Kata

The "Heavy Metal Bake Sale" kata is a fun and practical coding exercise set in 1999, where a local metal band needs your help to run a bake sale for raising funds. This kata combines basic arithmetic, inventory management, and customer interaction in a simple software application.

## Problem Description

You are tasked with creating software to manage the sales and inventory for the band's bake sale. The sale includes four items, each with a specific price, quantity, and purchase code:

| Item     | Price  | Quantity | Purchase Code |
|----------|--------|----------|---------------|
| Brownie  | $0.75  | 48       | B             |
| Muffin   | $1.00  | 36       | M             |
| Cake Pop | $1.35  | 24       | C             |
| Water    | $1.50  | 30       | W             |

The application must handle purchases and calculate the correct change. It also needs to track inventory to ensure items are in stock.

## Requirements

- Process a comma-delimited string of purchase codes to determine the total cost.
- Check and update inventory levels.
- Calculate and display the correct change if the customer overpays.
- Display appropriate messages for out-of-stock items or insufficient payment.

## Examples

- Items to Purchase: `B,C,W`
  - Total: `$3.50`
  - Amount Paid: `$4.00`
  - Change: `$0.50`
- Items to Purchase: `B`
  - Total: `$0.75`
  - Amount Paid: `$0.75`
  - Change: `$0.00`
- Items to Purchase: `C,M`
  - Total: `$2.35`
  - Amount Paid: `$2.00`
  - Change: `Not enough money`
- Items to Purchase: `W`
  - Total: `Water is out of stock`

## Hint

Consider using Stubs or Mocks (or both) to handle input and output for easier testing.

## Bonus

Years later, the band decides to have another bake sale. Update your software to read items, quantities, and prices from a configuration file and transform it into a Restful web service, moving away from console-based interaction.

---

This kata is an excellent opportunity to practice handling real-world scenarios in software development, encompassing basic data management, user interaction, and evolving requirements over time.

