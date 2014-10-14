###Hayden Crockett


def fib(n):
    
    l = [1, 1]
    a, b,  = 1, 1
    d = 0
    while d <= n:
        c = a + b; a = b; b = c 
        l.append(c)
        d += 1
    print(l[:n])

print fib(1)
print fib(2)
print fib(6)