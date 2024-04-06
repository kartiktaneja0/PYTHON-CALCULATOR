def calc(decide):
    # Prompt the user to enter the 1st number
    num1 = int(input("Enter the 1st number: "))
    # Prompt the user to enter the 2nd number
    num2 = int(input("Enter the 2nd number: "))
    # Initialize the answer variable
    ans = 0
    # Perform the operation based on the input decision
    if decide == 1:  # Addition
        ans = num1 + num2
    if decide == 2:  # Subtraction
        ans = num1 - num2
    if decide == 3:  # Multiplication
        ans = num1 * num2
    if decide == 4:  # Division
        ans = num1 / num2
    if decide == 5:  # Floor division
        ans = num1 // num2
    if decide == 6:  # Exponential
        ans = num1 ** num2
    if decide == 7:  # Modulus
        ans = num1 % num2
    # Print the answer
    print("The answer is:", ans)

# Display the menu options
print("----------MENU----------- \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor division \n 6. Exponential \n 7. Modulus \n -------------------")
# Prompt the user to enter the operation number
decide1 = int(input("Please enter the operation number: "))
# Check if the input operation number is valid
if 1 <= decide1 <= 7:
    # Call the calc function with the chosen operation number
    calc(decide1)
else:
    # Print error message for invalid operation number
    print("Invalid operation number. Please select a number between 1 and 7.")
