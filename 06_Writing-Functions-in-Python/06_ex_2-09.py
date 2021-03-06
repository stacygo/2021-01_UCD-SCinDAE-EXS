# Exercise 2-09: Scraping the NASDAQ

from functions import stock

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
    # Open "NVDA.txt" for writing as f_out
    with open('output/NVDA.txt', 'w') as f_out:
        for _ in range(10):
            value = nvda.price()
            print('Logging ${:.2f} for NVDA'.format(value))
            f_out.write('{:.2f}\n'.format(value))
