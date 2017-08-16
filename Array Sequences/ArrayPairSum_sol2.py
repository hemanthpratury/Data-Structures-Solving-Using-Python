def pair_sum(arr,sum):
    
    seen = set()
    output = set()
    
    for ele in arr:
        
        print('element: %s'  %ele)
        target = sum-ele
        print('target: %s'  %target)
        if target not in seen:
            seen.add(ele)
            print('seen %s'  %seen)
        else:
            output.add((min(ele,target),max(ele,target)))
            print('output: %s '  %output)
            
    print('\n'.join(map(str,list(output))))