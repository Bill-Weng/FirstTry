class Fibs():
    
    def __init__(self, value):
        self.value = value 
        
    def __iter__(self):
        self.a = [2, 3, 5] 
        self.b = [2, 3, 5]
        self.boundary = 5
        return self
    
    def __next__(self):
        self.b.append(self.b[-1] +2)  
        self.boundary = self.b[-1]
        for i in self.a: 
            if i <= self.boundary/i:
                if self.b[-1]%i == 0:
                    append = False
                    break
            else:
                append = True
                break
        
        if not append :
            rtn = 0
        else:
            rtn = 1
            self.a.append(self.b[-1])
        
        if self.a[-1] >= self.value:
            raise StopIteration
        if rtn == 1:
            return self.a[-1] 

# file_data = open("test1.txt", 'w')        
t = Fibs(2000000)
b = [2, 3, 5]
a = [i for i in t if i is not None]
print(sum(a))

# 标志位的使用
