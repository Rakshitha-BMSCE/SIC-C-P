import sys

import Insertion_sort as ins_sort

Numbers = []

for i in  range(1,len(sys.argv)):
    Numbers.append(float(sys.argv[i]))

print('Numbers before sorting:',Numbers)

new_numbers = ins_sort.Insertion_sort(Numbers)

print('Numbers after sorting:',new_numbers)

''' program completed
'''

