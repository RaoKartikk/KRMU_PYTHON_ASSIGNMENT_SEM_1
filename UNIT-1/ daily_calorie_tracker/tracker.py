# tracker.py
"""
Daily Calorie Tracker
Developer: [Kartik]
Date: [9/11/2025]
Project: Daily Calorie Intake Monitor
"""

import datetime

# Remove def main() and inline the code
# Task 1: Setup & Introduction
print("=" * 50)
print("      DAILY CALORIE TRACKER")
print("=" * 50)
print("Welcome to your daily calorie monitoring tool!")
print("This tool helps you log meals, track total calories,")
print("compare against your daily limit, and save logs.")
print("-" * 50)

# Task 2: Input & Data Collection
meal_names = []
calorie_amounts = []

try:
    num_meals = int(input("How many meals do you want to enter? "))
    print()
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Using loop for meal input
i = 0
while i < num_meals:
    print(f"Meal #{i+1}:")
    meal_name = input("  Enter meal name (e.g., Breakfast, Lunch): ")
    meal_names.append(meal_name)
    
    try:
        calories = float(input("  Enter calorie amount: "))
        calorie_amounts.append(calories)
        i += 1  # Only increment if input is valid
    except ValueError:
        print("  Invalid calorie amount! Please enter a number.")
        # Don't increment i, let user retry the same meal
    print()

# Task 3: Calorie Calculations
# Calculate total calories using loop
total_calories = 0
for calories in calorie_amounts:
    total_calories += calories

# Calculate average using loop
if len(calorie_amounts) > 0:
    average_calories = total_calories / len(calorie_amounts)
else:
    average_calories = 0

# Get daily limit with validation loop
while True:
    try:
        daily_limit = float(input("Enter your daily calorie limit: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\n" + "=" * 50)

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    excess_calories = total_calories - daily_limit
    print("⚠️  WARNING: You have EXCEEDED your daily limit!")
    print(f"   You are {excess_calories:.1f} calories over your limit.")
else:
    remaining_calories = daily_limit - total_calories
    print("✅ SUCCESS: You are within your daily limit!")
    print(f"   You have {remaining_calories:.1f} calories remaining.")

print("=" * 50)

# Task 5: Display Report
print("\n" + "=" * 60)
print("                  DAILY CALORIE REPORT")
print("=" * 60)

print(f"{'Meal':<15} {'Calories':>10}")
print("-" * 30)

# Display meals using loop
i = 0
while i < len(meal_names):
    print(f"{meal_names[i]:<15} {calorie_amounts[i]:>10.1f}")
    i += 1

print("-" * 30)
print(f"{'TOTAL':<15} {total_calories:>10.1f}")
print(f"{'AVERAGE':<15} {average_calories:>10.1f}")
print(f"{'DAILY LIMIT':<15} {daily_limit:>10.1f}")
print("=" * 60)

# Bonus Task: Save Session Log to File
save_choice = input("\nDo you want to save this report to a file? (y/n): ").lower()

# Handle save choice with loop for validation
save_processed = False
while not save_processed:
    if save_choice in ['y', 'yes']:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"calorie_log_{timestamp}.txt"
        
        try:
            with open(filename, "w") as file:
                file.write("=" * 60 + "\n")
                file.write("              DAILY CALORIE TRACKER LOG\n")
                file.write("=" * 60 + "\n")
                file.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("-" * 60 + "\n")
                file.write(f"{'Meal':<15} {'Calories':>10}\n")
                file.write("-" * 30 + "\n")
                
                # Write meals to file using loop
                j = 0
                while j < len(meal_names):
                    file.write(f"{meal_names[j]:<15} {calorie_amounts[j]:>10.1f}\n")
                    j += 1
                
                file.write("-" * 30 + "\n")
                file.write(f"{'TOTAL':<15} {total_calories:>10.1f}\n")
                file.write(f"{'AVERAGE':<15} {average_calories:>10.1f}\n")
                file.write(f"{'DAILY LIMIT':<15} {daily_limit:>10.1f}\n")
                file.write("-" * 60 + "\n")
                
                if total_calories > daily_limit:
                    file.write(f"STATUS: EXCEEDED limit by {total_calories - daily_limit:.1f} calories\n")
                else:
                    file.write(f"STATUS: Within limit ({daily_limit - total_calories:.1f} calories remaining)\n")
                
                file.write("=" * 60 + "\n")
            
            print(f"✅ Report saved successfully as '{filename}'")
            save_processed = True
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            save_processed = True
    
    elif save_choice in ['n', 'no']:
        save_processed = True
    else:
        save_choice = input("Please enter 'y' for yes or 'n' for no: ").lower()

print("\nThank you for using Daily Calorie Tracker!")
print("Stay healthy! 🍎")
