import sys
<<<<<<< HEAD
=======

>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
input_list = []

for i in range(1,len(sys.argv)):
    input_list.append(float(sys.argv[i]))

<<<<<<< HEAD
print('Input list =', input_list)

for i in range(0,len(input_list)-2):
    for j in range(0,len(input_list)-2-i):
        if input_list[j] > input_list[j +1]:
             temp = []
             temp = input_list[j]
             input_list[j] = input_list[j+1]
             input_list[j+1] = temp
             

print('Input list after buuble sort:',input_list)

''' program completed
'''
=======
print('Input list = ',input_list)

for i in range (0,len(input_list)-2):
    for j in range(0,len(input_list)-2-i):
        if input_list[j] > input_list[j+1]:
            temp = []
            temp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j+1] = temp

print('Input list after bubble sort: ',input_list)
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
