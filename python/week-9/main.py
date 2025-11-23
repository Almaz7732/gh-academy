import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

num_rolls = int(input("How many times should you roll the dice? "))

frequency = {i: 0 for i in range(2, 13)}
print(frequency)

for _ in range(num_rolls):
    total = roll_dice()
    frequency[total] += 1

print("\nResults:")
print("Amount | Frequency | Percentage")
print("-" * 29)
for sum_value, count in frequency.items():
    percentage = (count / num_rolls) * 100
    print(f"{sum_value:6} | {count:9} | {percentage:6.2f}%")

most_common = max(frequency, key=frequency.get)
print(f"\nThe most common amount: {most_common} "
          f"(appeared {frequency[most_common]} times, "
          f"{frequency[most_common]/num_rolls*100:.2f}%)")