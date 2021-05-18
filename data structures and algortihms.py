

LINEAR_ARRAY = [10,20,30,40,50,0,0,0] ##length=8-3
Circular_array = [0,0,10,20,30,40,50,0] ##length=8-3

class node: #Singly linked list
    def __init__(self,data,next):
        self.data = data
        self.next = next
        
class node1: #doubly linked list
    def __init__(self,data,next,previous):
        self.data=data
        self.next= next
        self.prev = prev
        
class DList:
    def __init__(self):
        self.head = None
        self.datas = []
    def append(self,data):
        if self.head == None:
            nnode = dnode(data)
            nnode.prev = None
            self.head = nnode
        else:
            nnode = dnode(data)
            current = self.head
            while current.ref:
                current = current.ref
            current.ref = nnode
            nnode.prev = current
            nnode.ref = None
    def prepend(self,data):
        #Supposed to add elements in the top#
        pass
    def print_list(self):
        current = self.head
        while current:
            x = current.data
            self.datas.append(x)
            current = current.ref
        return self.datas
        
def list_processing(a,dllist):
    for i in range (len(a)):
        dllist.append(a[i])
    
        
class stack:  #stack
    database= []
    def __init__(self,data="Default"):
        self.data=data
    def push(self,data):
        self.data=data
        self.databasea.append(self.data)
    def pop(self):
        self.database.pop(self.database(len(self.database)-1))
    def peek(self):
        return self.database[len(self.database)-1]
        
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx],array[step])
        
        
def insertion_sort(array):
    
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue
        
a = [4,6,7,1,2]

def bubble_sort(a):
    isSwap = False
    for i in range (4):
    	try:
    		if a[i]>a[i+1]:
    			temp = a[i]
    			a[i]=a[i+1]
    			a[i+1]=temp
    			bubble_sort(a)
    	except:
    		None
    print(a)
    
bubble_sort(a)

def fibo(n):
    n = int(n)
    if n==0:
        return 0
    if n==1:
        return 1 
    else:
        return (fibo(n-1)+fibo(n-2))
    
for i in range(0,8):
    print(fibo(i),end=" ")
    
    
def grid_walk(m,n):
  if m<0 or n<0:
    return 0
  if m==1 or n==1:
      return 1 
  else: 
      return grid_walk(m,n-1)+grid_walk(m-1,n)

a,b=4,4
print("\n",grid_walk(a,b))
list1 = [4,6,1,3,9]

def selectionSort(a): #not recursive
    indexingLength = range(0,len(a)-1)
    for i in indexingLength:
        min_value = i
        
        for j in range(i+1,len(a)):
            if a[j]<a[min_value]:
                min_value=j
        if min_value != i:
            a[min_value],a[i]=a[i],a[min_value]
            
    return a

print(selectionSort(list1))

def recus1(n):  #for memoization using lists
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return recus1(n-1)+recus1(n-2)
print(recus1(7))

def binarySearch(a,data,l,h):
    if l>h:
        return 0
    else:
        mid = (l + h) // 2
        if data == a[mid]:
            return "Present"
        elif data<a[mid]:
            return binarySearch(a,data,l,mid-1)
        else:
            return binarySearch(a,data,mid+1,h)
def bubble_sorting(a,n):  ##IMPROVED
    for i in range(n-1):
        try:
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
            if n-1>1:
                bubble_sorting(a,n-1)
        except:
            None
        
   

