

def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    else:
        consec = {}
        shift = 1
        if k == 1:
            shift = 0
        for i in range(0, len(strarr) - shift):
            st = ''
            for word in strarr[i:i+k]:
                st += word
            consec[i] = st
        longest = ""
        for a in consec.values():
            if len(a) > len(longest):
                longest = a
        #return consec
        return longest

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))

# x = ["zone", "abigail", "theta", "form", "libe", "zas"]

# print(len(x[2:4]))


