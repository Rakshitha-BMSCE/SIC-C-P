def sequentially_search(search_element, elements):
    for i in range(len(elements)):
        if elements[i] == search_element:
            return i
    return -1

<<<<<<< HEAD

input_size = int(input('Enter size of the list:'))

elements = []

print(f'Enter the {input_size} elements of the list ')
=======
input_size = int(input('Enter size of the list: '))

elements = []  # elements = list()

print(f'Enter the {input_size} elements of the list')
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
for i in range(input_size):
    element = float(input())
    elements.append(element)

<<<<<<< HEAD
print('User given elements are \n',elements)
search_element = float(input('Enter the element to be searched:'))

search_index = sequentially_search(search_element,elements)
=======
print('User given elements are \n', elements)
search_element = float(input('Enter the element to be searched: '))

search_index = sequentially_search(search_element, elements)
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0

if search_index == -1:
    print(f'The search element {search_element} was not found in the list')
else:
<<<<<<< HEAD
    print(f'The search element {search_element} was  found at position {search_index} in the list')

    ''' program completed
'''
=======
    print(f'The search element {search_element} was found at position {search_index + 1}')
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
