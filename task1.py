a = [-2,3,9,4,1,2,3]
class keyindex:
    def __init__(self,a):
        self.a = a
        x1,x2 = self.a[0], self.a[len(self.a)-1]
        mini = self.a[0]
        if x1>=0:
            self.index = [0]*(max((self.a))+1)
            for i in range(len(self.a)):
                if self.a[i]<len(self.index):
                    self.index[self.a[i]] += 1
        else:#still under construction
            self.index = [0]*(max((self.a))+1)
            while x1<0:
                self.index.append(0)
                x1 += 1
            for i in range(len(self.a)):
                if self.a[i]<len(self.index):
                    self.index[self.a[i]] += 1
            ##work in it without class
            if min(b)<0:
        for i in range(min(b),0,1):
        c.append(0)
    g=0
    for j in range(min(a)-1,0,1):
        if a[g]<j:
            c[g] += 1
            g += 1
            #########################
            
    def __void__(self):
        return self.index
    
def sorter(a):
    try:
        for i in range(len(a)):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                sorter(a)
    except:
        pass
    return a

print(keyindex(sorter(a)).__void__())
