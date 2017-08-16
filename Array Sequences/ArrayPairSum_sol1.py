def arrayPairSum(lst,sum):
    
    kv={}
    for ele in lst:
        if ele in kv:
            #diff = sum-ele
            kv[ele][1]+=1
            #kv[ele] = [_,cou]
        else:
            diff = sum-ele
            kv[ele] = [diff,1]
    print(kv)
    
    for ele in kv:
        if(kv[ele][1] > 1):
            if(kv[ele][0] == ele):
                print("(%s,%s)" %(ele,kv[ele][0]))
        if (kv[ele][0]) in lst:
            print("(%s,%s)" %(ele,kv[ele][0]))