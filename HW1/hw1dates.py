###Hayden Crockett   ****NOT COMPLETE**


def readit(filename):
    f = open(filename)
    
    for line in f.readlines():
        data = line.split(',')
        if len(data) == 39:
            print data
            
            
            
            

    
filename = 'Documents\GitHub\pg2014\HW1\discharge.dat'
readit(filename)

    