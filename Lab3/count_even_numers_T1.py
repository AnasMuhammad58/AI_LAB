def count_even_numbers(number_list):
    # Check if the list is empty
    if len(number_list) == 0:
        return 0  
    
    # Initialize a counter variable 
    even_count = 0
    
    # Iterate through each number in the list
    for number in number_list:
        # Check if the number is even
        if number % 2 == 0:
            even_count += 1
    
    # Return the count of even numbers
    return even_count

# Example usage:
my_list = [22]
result = count_even_numbers(my_list)
print("Count of even numbers:", result)

empty_list = []
result_empty = count_even_numbers(empty_list)
print("Count of even numbers in an empty list:", result_empty)
