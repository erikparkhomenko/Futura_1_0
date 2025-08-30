This Python script calculates the fair futures contract price based on user-provided parameters such as spot price, risk-free rate, storage costs, dividend yield, and time to maturity. It supports both monthly and yearly time units and includes error handling to manage invalid inputs gracefully.

Key Features:
- User-friendly input interface for all necessary parameters
- Handles calculations for both monthly and yearly time periods
- Provides clear and informative error messages for invalid input
- Uses the `math` library for mathematical operations

This script is ideal for traders, financial analysts, and anyone involved in futures contract pricing. It simplifies the process of determining fair contract prices with minimal manual intervention.

Example Usage:
```python
# Example run
Description = "Gold Futures"
Spot = 1800.50
rfr = 0.025
Time_unit = "M"
Storage_costs = 0.005
Dividend_yeild = 0.01

# Running the script with example inputs
contract_price = Spot * math.exp((rfr + Storage_costs - Dividend_yeild) * Time_to_maturity)
print(f"The fair contract price for a futures contract of {Description} is: {contract_price}")
```

This script is easy to use and can be integrated into larger trading platforms or financial analysis workflows.
