age = int(input("Enter your age: "))

if age >= 18:
    print("✅ You are eligible to vote!")
else:
    print(" You are not eligible to vote yet.")
    print(f"You need to wait {18 - age} more year(s).")
