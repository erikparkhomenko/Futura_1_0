# importing key modules for the command line to work
import art
import math
# Purely cosmetic and can be removed :)
print(art.welcome)
# Obtaining user inputs about the futures contract
Description = input("What are you trying to price?")
Spot = float(input("Please enter the spot price: "))
rfr = float(input("Please enter the risk free rate (as a decimal): "))
Time_unit = input("Are you calculating in years of month? (Type M for months and Y for years)")
Storage_costs = float(input("Please enter the rate storage cost per unit: "))
Dividend_yeild = float(input("Please enter the dividend yeild rate:"))


# if statement - giving the user to choose a holding time between months and years
if Time_unit.capitalize() == "M":
    Time_to_maturity = float(input(("Please enter the time to maturity (in months): ")))
    Time_to_maturity = Time_to_maturity/12
    contract_price = Spot * math.exp((rfr + Storage_costs - Dividend_yeild) * Time_to_maturity)
    print(f"The fair contract price for a futures contract of {Description} is: {contract_price}")
elif Time_unit.capitalize() == "Y":
    Time_to_maturity = float(input(("Please enter the time to maturity (in years): ")))
    contract_price = Spot * math.exp((rfr+Storage_costs-Dividend_yeild) * Time_to_maturity)
    print(f"The fair contract price for a futures contract of {Description} is: {contract_price}")
else:
    print(art.error)
