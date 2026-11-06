while True:
    user_input = input("Enter a number greater than 1 (or 'e' to exit): ")
    print()
    
    if user_input.lower() == "e":
        break
        
    number = int(user_input)
    
    if number <= 1:
        print("Must be greater than 1!\n")
        continue
    print(f"Multiplication table of {number}")

    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
    print()
