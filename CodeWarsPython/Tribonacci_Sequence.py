

def tribonacci(signature, n):
    if n < 3:
        arr = []
        for i in range(0, n):
            arr.append(signature[i])
        return arr
    else:
        for i in range(3, n):
            signature.append(sum(signature[i-3:i]))
        return signature


print(tribonacci([1, 1, 1], 1))

