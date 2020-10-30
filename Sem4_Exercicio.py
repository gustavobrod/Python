def f1(n): 
    if n <= 1: 
        return 1 
    else: 
        return n * f1(n - 1) 
 

print(f1(4))

def f(n): 
    if n < 2: 
        return n 
    else: 
        return f(n-1) + f(n-2) 
 
print(f (6)) 

def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return max(v[i], f(v, i - 1)) 
 
l = [5,4,6,8,1,2] 
print(f(l, len(l) - 1))

def f(v, i): 
    if i == 0: 
        return v[i] 
    else: 
        return v[i] + f(v, i - 1) 
 
l = [5,4,6,8,1,2] 
print(f(l, len(l) - 1))

class S: 
    def __init__(self): 
        self.v = [ ] 
        self.i = -1 
 
    def push(self, x): 
        self.i += 1 
        self.v.append(x) 
 
    def pop(self): 
        if(not self.empty()): 
            self.i -= 1 
            return self.v.pop() 
 
    def empty(self): 
        return self.i < 0 
 
 
s = S() 
for i in range(10): 
    s.push(i) 
 
while not s.empty(): 
    print(s.pop())

class S: 
    def __init__(self): 
        self.v = [ ] 
        self.i = -1 
 
    def push(self, x): 
        self.i += 1 
        self.v.insert(0, x) 
 
    def pop(self): 
        if(not self.empty()): 
            self.i -= 1 
            return self.v.pop() 
 
    def empty(self): 
        return self.i < 0 
 
 
s = S() 
for i in range(10): 
    s.push(i) 
 
while not s.empty(): 
    print(s.pop())
    