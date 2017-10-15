def compress(s):
    l = len(s)
    i = 1
    cnt = 1
    r = ''

    if l == 0:
        return ""
    if l == 1:
        return s + "1"

    while i < l:

        if s[i] == s[i - 1]:
            cnt += 1

        else:
            r = r + s[i - 1] + str(cnt)
            #print(r)
            cnt = 1

        i += 1
    r = r + s[i - 1] + str(cnt)

    return r

result = compress('AABBCCCCCCaaaa')
print(result)