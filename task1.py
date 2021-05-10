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


###take help from here

step:1- Find the maximum number and create an auxiliary array of length max+1
step:2- Traverse through the array A, 
	for each element of A use it as the index of the aux and increment by 1
step:3- 


class KeyIndex:
    k = []    # array of integers
    # another global variable
    def __init__(self, p):
        mx = 0
        mn = 0
        negC = 0    # checking if any negative value exists
        for i in range(len(p)):
            if (p[i] < 0):
                negC += 1
        if (negC == 0):    # all positive values
            for i in range(len(p)):
                if (p[i] > mx):
                    mx = p[i]
            KeyIndex.k = [0]*(mx+1)
            for i in range(len(p)):
                for j in range(len(KeyIndex.k)):
                    if (p[i] == j):
                        KeyIndex.k[j] += 1
            print("All positive!", KeyIndex.k)
        elif (negC > 0):    # negative values present
            for i in range(len(p)):
                if (p[i] < mn):
                    mn = p[i]
            add = mn * (-1)
            for i in range(len(p)):
                p[i] += add
            for i in range(len(p)):
                if (p[i] > mx):
                    mx = p[i]
            KeyIndex.k = [0]*(mx+1)
            for i in range(len(p)):
                for j in range(len(KeyIndex.k)):
                    if (p[i] == j):
                        KeyIndex.k[j] += 1
            print("Some negative!", KeyIndex.k)

