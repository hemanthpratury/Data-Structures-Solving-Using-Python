def strcompress(s):
    d = {}

    # s = s.split()

    for u in s:

        if u not in d:
            d[u] = 1
        else:
            d[u] += 1

    for key, value in d.items():
        print("%s%s" % (key, value), end='')

strcompress('AAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaCCCVVVHHHhhhhB')