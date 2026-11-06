while True:
    user_input = input("Enter a number (or 'e' to exit): ")
    
    if user_input.lower() == "e":
        break
        
    number = int(user_input)
    
    if number <= 1:
        print("Must be greater than 1!\n")
        continue

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
    print()
