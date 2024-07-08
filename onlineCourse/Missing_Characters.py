#!/bin/python3

import math
import os
import random
import re
import sys


def missingCharacters(s):
    # Create sets of all lowercase English letters and digits
    all_lowercase_letters = set('abcdefghijklmnopqrstuvwxyz')
    all_digits = set('0123456789')
    
    # Convert the input string to a set to remove duplicates
    input_set = set(s)
    
    # Calculate missing characters and digits
    missing_digits = ''.join(sorted(all_digits - input_set))
    missing_letters = ''.join(sorted(all_lowercase_letters - input_set))
    
    # Concatenate and return the result
    return missing_digits + missing_letters
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()