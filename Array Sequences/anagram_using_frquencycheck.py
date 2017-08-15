def anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    #Edge case check
    if(len(s1) != len(s2)):
        return False
    
    #Creating counting Dictionary
    count ={}
    
    #Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    #Fill dictionary for second string (Subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    #check if counts are zero
    for k in count:
        if count[k] != 0:
            return False
        
    return True
