from numpy import array, insert, delete

# Calculate Average Temperature

temp_list = []
days = int(input("How many day's temperature: "))
for day in range(days):
    temp_list.append(float(input(f"Day {day + 1}'s high temp: ")))
avg = round(sum(temp_list) / len(temp_list), 2)

days_above_avg = len([day for day in temp_list if day > avg])
print(f"Average: {avg}")
print(days_above_avg)
