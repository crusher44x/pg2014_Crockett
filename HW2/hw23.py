x,y = np.load('Documents/GitHub/pg2014/examples/polynomial_data.npy').T


#plot(x,y,'k.')

def poly(u,v,N=1):
    g = np.polyfit(u, v, N)
    gx = linspace(0, 100, 1000)
    gy = polyval(g, gx)
    #plot(gx, gy, 'r.')

    #plot(u, v - gy, 'b.')
    for d in v:
        if d>=0:
            vv = d
        if d<0:
            vvv = d
        
    
    

    plot(vv + gy, u-v, 'purple')
    plot(vvv + gy, u-v, 'purple')
    
    

 

    
    
poly(x, y, 3)



