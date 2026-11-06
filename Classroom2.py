# classroom_chairs.py
# Purpose: Calculate and display the total number of chairs in a classroom 
# based on the given number of rows and chairs per row.

def calculate_chairs():
    rows = 6
    chairs_per_row = 8
    total_chairs = rows * chairs_per_row
    
    print(f"Number of rows: {rows}")
    print(f"Chairs per row: {chairs_per_row}")
    print(f"Total number of chairs: {total_chairs}")

if __name__ == "__main__":
    calculate_chairs()
