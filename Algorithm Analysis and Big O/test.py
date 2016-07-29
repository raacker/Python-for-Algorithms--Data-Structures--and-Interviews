def method1():
    l = [];
    for n in xrange(10000):
        l = l+ [n]

%timeit method1()
