#Declaring a function
def calculateTax(bill,tax_rate):
    return round((bill*tax_rate)/100.0,2)

print('Total tax is:', calculateTax(500.25,13))
print('Total tax is:', calculateTax(250.25,13))