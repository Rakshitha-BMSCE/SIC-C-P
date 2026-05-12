def Insertion_sort(Numbers):
    for i in range(len(Numbers)):
        element = Numbers[i]
        j = i - 1
        while j>=0 and element < Numbers[j]:
            Numbers[j+1] = Numbers[j]
            j-= 1
            Numbers[j+1] = element
    return Numbers

''' program completed
'''