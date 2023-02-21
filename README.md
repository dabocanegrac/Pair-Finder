# Find pairs

## Description

This is a Python script that takes a file as input and finds pairs of integers from a list that sum to a given value, where the list of integers and the target value are read from the input file. 

## Implementation

The find_pairs function takes two arguments, a list of integers and a target value, and returns a list of pairs of integers that sum to the target value. The function uses a dictionary to keep track of the numbers that have been seen so far, and for each number in the list, it checks if the difference between the target value and the number is in the dictionary. If it is, then it adds the pair to the list of pairs, it has a complexity of $O(n)$ and a space complexity of $O(n)$.

The main function uses the argparse module to parse the command line arguments, which in this case is just the name of the input file. It then reads the file contents, extracts the list of integers and the target value, calls the *find_pairs* function to find the pairs, and prints the pairs to the console in the format ```+ num1,num2```.

This script was written in *Python 3.9.2*.

## Usage

To run the script, you would need to create a text file with the list of integers and the target value separated by a newline character, and then run the script with the name of the file as an argument. A sample file is included in the repository, called 'sample.txt'. To run the script, you would do the following:

```bash
python find_pairs.py <filename>
```

where `<filename>` is the name of a file containing a list of numbers, one per line.

## Example

For example, if you create a file called numbers.txt with the following contents:
```bash
cat numbers.txt
1
2
3
4
5
6
7
8
9
10
```
Then you can run the script with the following command:
```bash
python find_pairs.py numbers.txt
+ 6,4
+ 7,3
+ 8,2
+ 9,1
```

## Testing
This project includes a test suite in *find_pairs_test.py*. To run the tests, open a terminal or command prompt and navigate to the directory where the *find_pairs_test.py* file is located. Then, run the following command:
```bash
python find_pairs_test.py
```
The test suite includes tests for various input scenarios, including an empty list, a list with one item, a list with no pairs that sum to target, a list with one pair that sum to target, a list with multiple pairs that sum to target, a list with negative numbers, and a large input list with even and odd number of elements.

This project also includes a random test data generator and a script to run the tests with random data. To run the tests with random data, open a terminal or command prompt and navigate to the directory where the *find_pairs_test_random.py* file is located. Then, run the following command:
```bash
python find_pairs_test_random.py
```
The script will generate a random list of integers and a random target value, and then run the tests with the random data. The script will run the tests 100 times, and will print the number of times the tests passed and the number of times the tests failed. The script will also print the list of integers and the target value if the tests fail, it will generate the expected pairs using brute force and compare them with the pairs returned by the *find_pairs* function.

You can change the arguments of the *generate_test_data* call inside the main function of *find_pairs_test_random.py* to change the number of elements in the list and the range of the numbers in the list. The default values are 100 elements and numbers between -50 and 50.

This file also provides a function called *compare_pairs* that can be used to compare the results of two different implementations of the *find_pairs* function.

## License

This software is licensed under the **MIT License**.

## Author

This software was written by [dabocanegrac](https://github.com/dabocanegrac)

## Acknowledgements

This coding challenge was provided by **MachEight**.

