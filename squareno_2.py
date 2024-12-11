def find_squares(numbers):
    # Using list comprehension to calculate squares
    squares = [num ** 2 for num in numbers]
    return squares

# Example usage
if __name__ == "__main__":
    # Sample list of numbers
    number_list = [1, 2, 3, 4, 5]
    squares_list = find_squares(number_list)
    print("Squares of the numbers:", squares_list)
