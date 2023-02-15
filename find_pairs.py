import argparse
from typing import List, Tuple


def find_pairs(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Find all pairs of integers from a list that sum to a given value.

    Args:
        numbers: List of integers to search for pairs.
        target: Target value to find pairs that sum to.

    Returns:
        List of pairs of integers that sum to the target value.
    """
    pairs = []  # list of pairs
    nums = {}  # dictionary of numbers
    for num in numbers:  # iterate through the list of numbers
        diff = target - num  # find the difference between the target and the current number
        if diff in nums:  # if the difference is in the dictionary, add the pair to the list
            pairs.append((num, diff))  # add the pair to the list
        nums[num] = True # add the number to the dictionary
    return pairs  # return the list of pairs


def main():
     # Parse command line arguments
    parser = argparse.ArgumentParser(description='Find pairs of integers from a list that sum to a given value.') # create the parser
    parser.add_argument('filename', help='Name of the file containing the list of numbers and target value') # add the filename argument
    args = parser.parse_args() # parse the arguments

    # Read the file contents and parse the numbers and target value
    with open(args.filename, 'r') as f: # open the file
        file_contents = f.read().strip().split('\n') # read the file contents
        numbers = list(map(int, file_contents[:-1])) # convert the numbers to integers
        target = int(file_contents[-1]) # convert the target value to an integer

    # Find the pairs and print the output
    pairs = find_pairs(numbers, target) # find the pairs
    for pair in pairs: # iterate through the pairs
        print(f"+ {pair[0]},{pair[1]}") # print the pair

if __name__ == "__main__":
    main()
