##QuickSort

dt = open('data.txt', 'r').read()


##Function for string to integer list
def strtolist(x):
    counter = 0
    counter2 = 0
    temp_number = ''
    new_data = []
    
    for i in x:
        if i is not ' ':
            temp_number = temp_number + i

    
        elif i == ' ':
            new_data.append(int(temp_number))
            temp_number = ''
            continue

    return new_data

integer_list = strtolist(dt)

print('sometihng')
##QuickSorter 

