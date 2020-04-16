

def persistence(n):
    how_many_times = 0
    while len(str(n)) != 1:
        x = 1
        how_many_times += 1
        for i in str(n):
            x = x * int(i)
        n = x
    return how_many_times


print(persistence(999))

