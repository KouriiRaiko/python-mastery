# https://www.hackerrank.com/challenges/special-palindrome-again/

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple
from math import factorial

# Complete the substrCount function below.
def substrCount(n, s):
    s = list(s)
    count = 0

    Sequence = namedtuple(typename='Sequence', field_names=["letter", "amount"])
    sequences = []

    # Build list of sequences
    for letter in s:
        if not sequences or sequences[-1].letter != letter:
            sequences.append(Sequence(letter=letter, amount=1))
        else:
            sequences[-1] = Sequence(sequences[-1].letter, sequences[-1].amount + 1)

    # Count special palindrome substrings
    for i, sequence in enumerate(sequences):
        count += sum(range(1, sequence.amount + 1))

        if i + 2 < len(sequences) and sequences[i+1].amount == 1 and sequences[i].letter == sequences[i+2].letter:
            count += min(sequences[i].amount, sequences[i+2].amount)

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

