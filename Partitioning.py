def partition(list, pivot):
    
    small = []
    big = []
        
    for i in list:
        if i > pivot:
            big.append(i)
        if i <= pivot:
            small.append(i)

    return small, big
