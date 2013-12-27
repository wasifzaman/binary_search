def binary_search(item, li, index=0):
    '''binary search

    precondition:
        item is in the list
        list is sorted
        
    returns the index of the item

    >>> l = [1, 2, 3, 4, 5]
    >>> print(binary_search(1, l))
    0

    '''
    if len(li) == 1:
        return index
    else:
        mid = len(li) // 2
        right = li[mid:]
        left = li[:mid]
        #print((left, right, index))
        if item >= li[mid]:
            index += len(right) - len(li) % 2
            return binary_search(item, right, index)
        if item < li[mid]:
            return binary_search(item, left, index)
