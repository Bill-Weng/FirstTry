
def foos(value):    
    a = [value]
    boundary = value
    factor = 2
    while True:
        if a[-1] == factor:
            break
        elif a[-1] % factor == 0:
            temp = a[-1] / factor 
            a.clear()
            factor = 2
            boundary = temp
            a.append(temp)
        elif factor > boundary:
            break 
        else:
            boundary = a[-1] //factor
            factor += 1          
    return a[-1]   
    
t = foos(600851475143)
print(t)
