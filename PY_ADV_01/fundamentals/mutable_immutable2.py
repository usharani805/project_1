# Example 2: List vs Tuple

numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)

# List is mutable
numbers_list.append(4)

print("Modified list:", numbers_list)

# Tuple is immutable
# numbers_tuple.append(4)  # This would cause an error

print("Tuple:", numbers_tuple)