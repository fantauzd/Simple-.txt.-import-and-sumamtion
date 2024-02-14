from file_sum import *
import unittest

class tester(unittest.TestCase):
    def test_1(self):
        file_sum('some_num.txt')
        sum = 0
        with open('some_num.txt', 'r') as infile:
            for line in infile:
                sum += float(line)
        with open('sum.txt', 'r') as infile:
            val = float(infile.read())
        self.assertEqual(sum, val)

