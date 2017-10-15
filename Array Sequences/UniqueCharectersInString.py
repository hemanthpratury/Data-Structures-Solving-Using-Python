def uni_char2(s):
    chars = set()

    for i in s:

        if i in chars:
            return False
        else:
            chars.add(i)

    return True

result = uni_char2('aabcde')
print(result)