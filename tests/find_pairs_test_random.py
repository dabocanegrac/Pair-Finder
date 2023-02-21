import sys
sys.path.insert(0, '../')  # Add the parent directory to the path
from random import randint  # import randint for generating random test data
from typing import List, Tuple  # import types for type hints
from find_pairs import find_pairs  # import the function to test


# type hint the function
def generate_test_data(num_tests: int, min_size: int, max_size: int, min_val: int, max_val: int) -> List[Tuple[List[int], int]]:
    """
    Generate random test data for the find_pairs function.

    Args:
    - num_tests (int): the number of test cases to generate
    - min_size (int): the minimum length of each test case list
    - max_size (int): the maximum length of each test case list
    - min_val (int): the minimum value of each test case list element
    - max_val (int): the maximum value of each test case list element

    Returns:
    - tests (List[Tuple[List[int], int]]): a list of test cases, where each test case is a tuple consisting of a list of
    integers and a target integer to find pairs that sum to it
    """
    tests = []  # create an empty list to store the test data
    for i in range(num_tests):  # loop through the number of tests
        # generate a random size for the list
        size = randint(min_size, max_size)
        # generate a list of random numbers of the specified size
        test_numbers = [randint(min_val, max_val) for _ in range(size)]
        # generate a random target value
        test_target = randint(min_val, max_val)
        # append the test data to the list
        tests.append((test_numbers, test_target))
    return tests  # return the list of test data


# type hint the function
def compare_pairs(expected_pairs: List[Tuple[int, int]], result_pairs: List[Tuple[int, int]]) -> Tuple[bool, Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]]:
    """
    Compare the expected and actual output of the find_pairs function.

    Args:
    - expected_pairs (List[Tuple[int, int]]): a list of expected pairs of integers that sum to the target
    - result_pairs (List[Tuple[int, int]]): a list of actual pairs of integers that sum to the target

    Returns:
    - (Tuple[bool, Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]]): a tuple of a boolean indicating if the test
    passed, and a tuple of the expected and actual output if the test failed
    """
    expected_pairs = sorted([tuple(sorted(pair)) for pair in expected_pairs]) # sort the expected pairs
    expected_pairs = list(set(expected_pairs)) # remove duplicates
    expected_pairs.sort() # sort the list 
    expected_pairs = [(x, y) for (x, y) in expected_pairs] # convert the list of tuples to a list of lists
    result_pairs = sorted([tuple(sorted(pair)) for pair in result_pairs]) # sort the result pairs
    result_pairs = list(set(result_pairs)) # remove duplicates
    result_pairs.sort() # sort the list
    result_pairs = [(x, y) for (x, y) in result_pairs] # convert the list of tuples to a list of lists
    if expected_pairs == result_pairs: # compare the expected and actual output
        return True, None # return True if the output is correct
    else: # return False if the output is incorrect and the expected and actual output
        return False, (expected_pairs, result_pairs)


def main():
    """
    Test the find_pairs function with randomly generated test data.
    """
    test_data = generate_test_data(100, 1, 10, -50, 50) # generate random test data
    for i, (numbers, target) in enumerate(test_data): # loop through the test data
        expected_pairs = [(num, target - num) for num in numbers if num != 
                          target - num and target - num in numbers] # find the expected pairs and dont include the same number twice using brute force
        expected_pairs = [(x, y) for (x, y) in expected_pairs] # convert the list of tuples to a list of lists
        result_pairs = find_pairs(numbers, target) # test the function
        result_pairs = [(x, y) for (x, y) in result_pairs] # convert the list of tuples to a list of lists
        passed, error = compare_pairs(expected_pairs, result_pairs) # compare the expected and actual output
        if passed: # print the result of the test
            print(f"Test {i} passed")
        else: # print the result of the test and the expected and actual output
            print(f"Test {i} failed") 
            print(f"Error: {error}") 
            print(f"Numbers: {numbers}")
            print(f"Target: {target}")


if __name__ == "__main__":
    main()
