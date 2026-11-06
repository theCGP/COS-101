#weekly_expenses.py
#Student Weekly Expense Calculator
#Author: Jim-Suleiman Paul
#Matric Number: VUG/SEN/26/16035

# --- INPUT ___
name = input("Enter Student name: ")
daily_transport = float(input("Enter daily transport cost: ").replace(",", ""))
daily_feeding = float(input("enter daily feeding cost: ").replace(",", ""))
days = int(input("Enter number of days on campus: "))
other_expenses = float(input("Enter other weekly expenses: ").replace(",", ""))

# --- PROCESS ---
transport_total = daily_transport * days
feeding_total = daily_feeding * days
weekly_total = transport_total + feeding_total

# --- OUTPUT ---
print()
print("WEEKLY EXPENSE SUMMARY")
print(f"Student: {name}")
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding Total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN{other_expenses:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")

# --- SUBMITTED BY ---
print()
print("=" * 40)
print("Submitted by: Jim-Suleiman Paul")
print("Matric No:   VUG/SEN/26/16035")
print("=" * 40)
      
