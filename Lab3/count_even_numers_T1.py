def count_even_numbers(number_list):
    # Initialize a counter variable to keep track of even numbers
    even_count = 0
    
    # Iterate through each number in the list
    for number in number_list:
        # Check if the number is even
        if number % 2 == 0:
            even_count += 1
    
    # Return the count of even numbers
    return even_count

# Example usage:
my_list = [2, 2, 2, 4, 5, 6]
result = count_even_numbers(my_list)
print("Count of even numbers:", result)
