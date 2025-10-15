print('How many people are splitting the bill:')
countPeople = int(input())

people = []

for i in range(1, countPeople + 1):
    print(f'Enter a name for the {i} person')
    people.append(input().capitalize())

print('Enter the total bill amount:')
totalBillAmount = int(input())
print('Enter the tip percentage:')
tipPercentage= int(input())

tip = round((totalBillAmount/100) * tipPercentage, 2)
totalAmount = round(totalBillAmount + tip, 2)

everyPerson = round(totalAmount/countPeople, 2)

print(f'Total tip: {tip}')
print(f'Total amount: {totalAmount}')
print(f'Every person must pay {everyPerson}')

if tipPercentage > 20:
    print('Thank you for your generosity!')
