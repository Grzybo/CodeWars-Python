


def divisors(n):
    div = []
    x = n - 1
    while x > 1:
        if(n%x == 0):
            div.append(x)
        x = x - 1
    if(len(div) <= 1):
        return ("%d is prime" % (n)) 
    else:
        div.sort()
        return div

        
print(divisors(5))

print(divisors(123))
print(divisors(144))
print(divisors(13))