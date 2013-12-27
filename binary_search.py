def binary_search(item, li, index=0):
    '''Returns the index of the item in li.

    precondition:
        item is in the list
        list is sorted
        
    

    >>> l = [1, 2, 3, 4, 5]
    >>> print(binary_search(3, l))
    2

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


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(binary_search(3, l))
