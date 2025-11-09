import datetime as dt

print("\033[1;33m" + "[======================= DAILY CALORIE TRACKER =======================]" + "\033[0m")
print("\nNAME: Kartik | ROLL NO: 2501730166")
print("DATE:", dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print()

meals, cal = [], []
num = int(input("HOW MANY MEALS YOU WANT TO ADD: "))
limit = float(input("ENTER DAILY CALORIE LIMIT: "))
print()

for _ in range(num):
    data = input("Enter meal and calories (comma separated): ").strip()
    name, value = [x.strip() for x in data.split(',')]
    meals.append(name.upper())
    cal.append(float(value))

print("\n\033[1;96m{:<5}{:<20}{:<15}\033[0m".format("No", "Meal", "Calories"))
print("\033[1;96m" + "-" * 45 + "\033[0m")
for i, (m, c) in enumerate(zip(meals, cal), 1):
    print("\033[1;96m{:<5}{:<20}{:<15}\033[0m".format(i, m, c))
print("\033[1;96m" + "-" * 45 + "\033[0m")

total = sum(cal)
avg = total / len(cal)
print(f"\nTOTAL CALORIES: {total:.1f}")
print(f"AVERAGE CALORIES/MEAL: {avg:.2f}\n")

if total > limit:
    print("ALERT: YOU EXCEEDED YOUR DAILY LIMIT.")
else:
    print("GOOD JOB: YOU ARE UNDER YOUR CALORIE LIMIT.")

save = input("\nSave report? (yes/no): ").strip().lower()
if save == "yes":
    with open("calorie_log.txt", "w") as f:
        f.write("===== DAILY CALORIE REPORT =====\n")
        f.write(f"NAME: Kartik\nROLL: 2501730166\nDATE: {dt.datetime.now()}\n\n")
        for i, (m, c) in enumerate(zip(meals, cal), 1):
            f.write(f"{i}. {m:<20} {c:<10}\n")
        f.write(f"\nTotal Calories: {total:.1f}\nAverage: {avg:.2f}\nLimit: {limit}\n")
        f.write("Status: {}\n".format("Exceeded Limit" if total > limit else "Within Limit"))
    print("File saved successfully.")
else:
    print("File not saved.")
