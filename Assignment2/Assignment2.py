import copy

def smooth_a(a, n):
    copyA = copy.copy(a) 
    
    r = []

    if a == []:
        return r
    
    for _ in range(n):
        copyA.insert(0, copyA[0])
        copyA.append(copyA[-1])        

    for i in range(n, len(copyA)-n):
        r.append(sum(copyA[i-n : i+n+1])/(2*n+1)) 

    return r
   
    
def smooth_b(b, n):

    r =[]
    if n >= len(b):
        for i in range(len(b)):
            r.append( ((sum(b[0:2*n+1]) / len(b[0:2*n+1])) ) / (2))
        
        return r

    y = n
    for i in range(n):
        r.append( (sum(b[0:i+n+1]) + (sum(b[0:i+n+1]) / len(b[0:i+n+1])) * y ) / (2*n+1))
        y -= 1
    
    for i in range(n, len(b)-n):
        r.append(sum(b[i-n : i+n+1])/(2*n+1))
    
    z = n
    for i in range(n):    
        r.append( (sum(b [-n-z:])  + (sum(b[-n-z:])/len(b[-n-z:]))*(i+1))/(2*n+1))
        z -= 1

    return r


def round_list(a_list, ndigits):
    roundList = [round(elem, ndigits) for elem in a_list]
    return roundList

 
x = [1, 2, 6, 4, 5, 0, 1, 2]

print('smooth_a(x, 1): ', smooth_a(x, 1))  
print('smooth_a(x, 2): ', smooth_a(x, 2))

print('smooth_b(x, 1): ', smooth_b(x, 1)) 
print('smooth_b(x, 2): ', smooth_b(x, 2))

print('smooth_a(x, 1) rounded: ', round_list(smooth_b(x, 2), 2))




