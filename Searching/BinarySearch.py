def binary_search(arr,ele):

    first = 0
    last = len(arr)-1

    found = False
    result = ()
    found_index = None

    while first <= last and not found:

        mid = (first+last)//2
        if arr[mid] == ele:
            found = True
            found_index = mid

        else:

            if(ele>arr[mid]):
                first = mid+1

            else:
                last = mid-1

    result = (found,found_index)
    return result

print(binary_search([1,2,3,4,5,6,7,8],8))