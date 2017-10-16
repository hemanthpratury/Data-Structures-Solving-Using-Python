def rec_binary_search(arr,ele):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if(arr[mid] == ele):
            return True
        if(ele>arr[mid]):
            return rec_binary_search(arr[mid+1:],ele)
        else:
            return rec_binary_search(arr[:mid],ele)

print(rec_binary_search([1,2,3,4,5,6,7],5))
