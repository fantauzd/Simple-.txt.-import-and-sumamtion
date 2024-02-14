# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/31/2023
# Description: Defines a file_sum that takes as a parameter the name of a text file that contains
# a list of numbers, one to a line, and returns the sum (just that number) to a text file named sum.txt.

def file_sum(num_list_file):
    """
    Adds each of the values in the passed file and writes the sum to a new file.
    :param num_list_file: the name of a text file that contains a list of numbers, one to a line
    :return: n/a, a file named sum.txt containing the sum of the numbers in num_list_file is created
    """
    sum_val = 0                                               # initialize sum to 0
    with open(str(num_list_file), 'r') as infile:
        for line in infile:
            sum_val += float(line)                            # adds value of each line to sum until no more lines

    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sum_val))                           # writes sum value to sum.txt file
