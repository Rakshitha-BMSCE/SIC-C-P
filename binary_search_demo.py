import sys
import binary_search
<<<<<<< HEAD
input_list = []

for i in range(1,len(sys.argv)):
    input_list.append(float(sys.argv[i]))

print(f'User given elements are \n',input_list)

search_element = float(input('Enter the element to be searched:'))

search_index = binary_search.binary_search(search_element,input_list)
=======

input_numbers = []

for i in range(1, len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print(f'User given elements are \n', input_numbers)

search_element = float(input('Enter the element to be searched: '))

search_index = binary_search(search_element, input_numbers)
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0

if search_index == -1:
    print(f'The search element {search_element} was not found in the list')
else:
<<<<<<< HEAD
    print(f'The search element {search_element} was  found at position {search_index + 1} in the list')

''' program completed
'''
=======
    print(f'The search element {search_element} was found at position {search_index + 1}')
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
