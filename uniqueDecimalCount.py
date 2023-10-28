# 1. Coding - Unique Decimal CountGiven a binary string, binary, that consists of characters '0' and '1' only, find the number of unique decimal representations of binary numbers that can be represented by non-empty subsequences of the string. Note:The string binary may have leading zeros.A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not. Examplebinary = "010" Distinct subsequences of the string are 0, 1, 01, 010, 10.Their corresponding decimal representations are 0, 1, 1, 2, 2. Distinct decimal numbers are 0, 1, 2.The unique decimal representations count is 3. Return 3. Function DescriptionComplete the function getCount in the editor below. getCount has the following parameter: string binary: a binary string Returns int: the number of unique decimal representations of binary numbers formed from non-empty subsequences of the string Constraints1 ≤ |binary| ≤ 20The string binary consists of characters '0' and '1' only Input Format For Custom TestingSample Case 0Sample Input For Custom TestingSTDIN FUNCTION----- --------011 → binary = "011"Sample Output3ExplanationGiven binary = "011".Distinct subsequences of the string are 0, 1, 01, 11.Their corresponding decimal representations are 0, 1, 1, 3. Distinct decimal numbers are 0, 1, 3. Sample Case 1LanguagePython 2 EnvironmentAutocomplete ReadyMore1101112131415161718192021#!/bin/pythonimport mathimport osimport randomimport reimport sys## Complete the 'getCount' function below.## The function is expected to return an INTEGER.# The function accepts STRING binary as parameter.#def getCount(binary):

#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'getCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING binary as parameter.
#

def getCount(binary):
    # Write your code here
    
    n = len(binary)
    unique_decimals = set()

    for i in range(n):
        current_char = binary[i]

        # Create a new set to store unique decimal values at this index
        new_decimals = set()
        new_decimals.add(int(current_char))  # Add the current digit as a decimal value

        # Merge unique decimal values from the previous set
        for decimal in unique_decimals:
            new_decimals.add(decimal * 2 + int(current_char))

        # Add all new unique decimal values to the result set
        unique_decimals.update(new_decimals)

    # Return the count of unique decimal values
    return len(unique_decimals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary = raw_input()

    result = getCount(binary)

    fptr.write(str(result) + '\n')

    fptr.close()
