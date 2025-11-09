# tracker.py
"""
Daily Calorie Tracker
Developer: [Kartik]
Project: Daily Calorie Intake Monitor
"""

import datetime

print("=" * 50)
print("      DAILY CALORIE TRACKER")
print("=" * 50)
print("Welcome to your daily calorie monitoring tool!")
print("This tool helps you log meals and track calories.")
print("-" * 50)

# Get number of meals
try:
    num_meals = int(input("How many meals do you want to enter? "))
    print()
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Collect meal data
meal_names = []
calorie_amounts = []

for i in range(num_meals):
    print(f"Meal #{i+1}:")
    meal_name = input("  Enter meal name: ")
    meal_names.append(meal_name)
    
    try:
        calories = float(input("  Enter calorie amount: "))
        calorie_amounts.append(calories)
    except ValueError:
        print("  Invalid calorie amount! Using 0 calories.")
        calorie_amounts.append(0)
    print()

# Calculate totals
total_calories = 0
for calories in calorie_amounts:
    total_calories += calories

if num_meals > 0:
    average_calories = total_calories / num_meals
else:
    average_calories = 0

# Get daily limit
try:
    daily_limit = float(input("Enter your daily calorie limit: "))
except ValueError:
    print("Invalid input! Using default limit of 2000 calories.")
    daily_limit = 2000

print("\n" + "=" * 50)

# Check limit status
if total_calories > daily_limit:
    excess_calories = total_calories - daily_limit
    print("⚠️  WARNING: You have EXCEEDED your daily limit!")
    print(f"   You are {excess_calories:.1f} calories over your limit.")
else:
    remaining_calories = daily_limit - total_calories
    print("✅ SUCCESS: You are within your daily limit!")
    print(f"   You have {remaining_calories:.1f} calories remaining.")

print("=" * 50)

# Display report
print("\n" + "=" * 50)
print("           DAILY CALORIE REPORT")
print("=" * 50)

print(f"{'Meal':<15} {'Calories':>10}")
print("-" * 30)

for i in range(len(meal_names)):
    print(f"{meal_names[i]:<15} {calorie_amounts[i]:>10.1f}")

print("-" * 30)
print(f"{'TOTAL':<15} {total_calories:>10.1f}")
print(f"{'AVERAGE':<15} {average_calories:>10.1f}")
print(f"{'DAILY LIMIT':<15} {daily_limit:>10.1f}")
print("=" * 50)

# Save to file option
save_choice = input("\nDo you want to save this report to a file? (y/n): ").lower()

if save_choice in ['y', 'yes']:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"
    
    try:
        with open(filename, "w") as file:
            file.write("=" * 50 + "\n")
            file.write("        DAILY CALORIE TRACKER LOG\n")
            file.write("=" * 50 + "\n")
            file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            file.write("-" * 50 + "\n")
            
            file.write(f"{'Meal':<15} {'Calories':>10}\n")
            file.write("-" * 30 + "\n")
            
            for i in range(len(meal_names)):
                file.write(f"{meal_names[i]:<15} {calorie_amounts[i]:>10.1f}\n")
            
            file.write("-" * 30 + "\n")
            file.write(f"{'TOTAL':<15} {total_calories:>10.1f}\n")
            file.write(f"{'AVERAGE':<15} {average_calories:>10.1f}\n")
            file.write(f"{'LIMIT':<15} {daily_limit:>10.1f}\n")
            
            if total_calories > daily_limit:
                file.write(f"STATUS: EXCEEDED by {total_calories - daily_limit:.1f} calories\n")
            else:
                file.write(f"STATUS: Within limit ({daily_limit - total_calories:.1f} remaining)\n")
            
            file.write("=" * 50 + "\n")
        
        print(f"✅ Report saved successfully as '{filename}'")
        
    except Exception as e:
        print(f"❌ Error saving file: {e}")

print("\nThank you for using Daily Calorie Tracker!")
print("Stay healthy! 🍎")
