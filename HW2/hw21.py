#Hayden Crockett
#2014-10-13
#HW2 Problem 1

n = np.array([[1,2],[3,4]])
m = np.array([[6,1],[5,2]])
ar = np.empty(4, dtype='float').reshape(2,2)


def dist(N,M):
   
    d00 = pylab.dist(n[0],m[0])
    d11 = pylab.dist(n[1],m[1])
    d01 = pylab.dist(n[0],m[1])
    d10 = pylab.dist(n[1],m[0])
    ar[0,0] = d00
    ar[0,1] = d01
    ar[1,1] = d11
    ar[1,0] = d10
    print ar
    

dist(n,m)

    
    