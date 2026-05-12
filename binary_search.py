def binary_search(search_element, input_list):
<<<<<<< HEAD
    low = 0
    high = len(input_list) - 1
=======
    low = 0 # the index of very 1st element
    high = len(input_list) - 1 # index of the last element
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
    while low <= high:
        mid_index = (low + high) // 2
        if search_element == input_list[mid_index]:
            return mid_index
<<<<<<< HEAD
        elif search_element == input_list[mid_index]:
            high = mid_index - 1

        else:
            low = mid_index + 1   

            ''' program completed
'''  
    
=======
        elif search_element < input_list[mid_index]:
            high = mid_index - 1 # set the new search area as 1st half of the list
        else:
            low = mid_index + 1 # set the search area as 2nd half of list
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
