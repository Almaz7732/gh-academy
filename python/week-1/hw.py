print('Enter your name:')
name = input()
print('Enter the total bill amount:')
totalBillAmount = int(input())
print('Enter the tip percentage:')
tipPercentage= int(input())

tip = (totalBillAmount/100) * tipPercentage
totalAmount = totalBillAmount + tip

print(name + ', Total tip: ' + str(tip))
print(name + ', Total amount: ' + str(totalAmount))