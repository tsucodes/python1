#Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
# =============================================
# Input: Ask the user to enter an amount in one currency (e.g., USD).
# Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
# Output: Display the converted amount in the target currency.

#input
USD_amount = float(input("Enter USD amount to convert:"))
exchange_rate = float(input("Enter exchange rate for country:"))
#processing
# formula for amount exchanged = source(USD) * exchange rate ex.EUR= 0.91
currency_exchange = USD_amount * exchange_rate
#output
print(USD_amount, "is equal to", currency_exchange)