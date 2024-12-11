def find_square(number):
    return number ** 2

# Example usage
if __name__ == "__main__":
    try:
        # Get user input
        num = float(input("Enter a number to find its square: "))
        square = find_square(num)
        print(f"The square of {num} is {square}.")
    except ValueError:
        print("Please enter a valid number.")
