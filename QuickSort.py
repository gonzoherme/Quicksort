from StringToList import strtolist
dt = open('data.txt', 'r').read()
integer_list = strtolist(dt)

from Partitioning import partition
print(integer_list)


#QuickSorter 

def quicksort(list):

    pivot = list[0]
    partition(list, pivot)
    
    defined_small = partition(list, pivot)[0]
    defined_big = partition(list, pivot)[1]
    
    quicksort(defined_big)
    quicksort(defined_small)

    sorted_list.append(defined_small)
    sorted_list.append(pivot)
    sorted_list.append(defined_big)

    return sorted_list


quicksort(integer_list)

