# Question 1. Given an array of integer numbers, which are already sorted.
# E.g., A = [1,2,3,3,3,4,4,5,5,6]
# • Find the mode of the array
# • Provide the time complexity and space complexity of the array, and your reasoning
# • Note: write your own function using the basic data structure of your language,
# please avoid the provided available functions from external lib

from collections import Counter


def find_mode_of_array(input_array: list) -> list:
    """Find mode of the array."""
    if not input_array:
        raise Exception('Cannot compute mode on empty array!')
    counter_set = Counter(input_array)
    counter_max = max(counter_set.values())
    mode = [k for k, v in counter_set.items() if v == counter_max]
    return mode


# time complexity = O(n)
# space complexity = O(n)

if __name__ == "__main__":
    n_num = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]
    print(find_mode_of_array(n_num))
