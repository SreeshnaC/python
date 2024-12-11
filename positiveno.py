def generate_positive_list(integers):
    # Using list comprehension to filter positive integers
    positive_numbers = [num for num in integers if num > 0]
    return positive_numbers

# Example usage
if __name__ == "__main__":
    # Sample list of integers
    integer_list = [10,-13,-7,8,-20,30,15,-6]
    positive_list = generate_positive_list(integer_list)
    print("Positive numbers:", positive_list)