dx = 100.0
dt = 5.0
g = 9.8
H = 10.0

u = zeros(10)
eta = 1


eta = eta - (dt*H/dx)*(u[1:]-u[:-1])
u[1:-1] = u[1:-1] - (dt*g/dx)*(eta[1:]-eta[:-1])

class Waves(object):
    '''DOC'''
    def __init__(self, dt=5.0, H=10.0, dx=9.8, eta=eta, u=u):
        self.dt = dt
        self.H = H
        self.dx = dx
    
    def __eta__(self,eta=eta):
        eta = eta - (dt*H/dx)*(u[1:]-u[:-1])
        return eta

    
    def __u__(self, u=u):
        u = u[1:-1] = u[1:-1] - (dt*g/dx)*(eta[1:]-eta[:-1])
        return u
