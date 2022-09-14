# a. assign a variable 'subtotal' to 17.75
# b. assign a variable 'taxPer' to .18
# c. assign a variable 'taxAmount' to the product of subtotal and taxPer
# d. assign a variable 'total' to the sum of subtotal and taxAmount

subtotal = 17.75
taxPer = .18
taxAmount = subtotal * taxPer
total = subtotal + taxAmount

print(f'''Subtotal: {subtotal}
Tax percentage: {taxPer}
Tax amount: {round(taxAmount, 2)}
Total: {round(total, 2)}''')