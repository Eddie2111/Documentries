lst = [i for i in range(input())] #to create a sequential list by using a given range
lst1=list(input("Enter numbers:").split(",")) #to put every character inside the list
lst1=[int(i) for i in lst1] #converts each of the elements in the list to int from str

LINEAR_ARRAY = [10,20,30,40,50,0,0,0] ##length=8-3
Circular_array = [0,0,10,20,30,40,50,0] ##length=8-3

class node: #Singly linked list
    def __init__(self,data,next):
        self.data,self.next = data,next
        
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
        
#experiement-ternary search

def ternarySearch(l,r,key,ar):
    if (r>=l):
        mid1,mid2=l+(r-l)//3,r-(r-l)//3
        
        if (ar[mid1]==key):
            return mid1
        if (ar[mid2]==key):
            return mid2
        
        if (key<ar[mid1]):
            return ternarySearch(l,mid1-1,key,ar)
        if (key>ar[mid]):
            return ternarySearch(mid2+1,r,key,ar)
        
        else:
            return ternarySearch(mid1+1,mid2-1,key,ar)
    return -1


#l,p = 0,5
#ar = [1,3,5,8,13,15,27,33,41,53]
#r = len(ar)-1
#key = 27
#print('index:',ternarySearch(l, r, key, ar)+1)   

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
        
####Heap Data Structure####
##Max heap##
class MaxHeap:
    heap=[]
    def __init__(self,default=None):
        self.default=default
    def getParent(self,i):
        return int( ((i-1)/2)-1 )
    def left_child(self,i): #get-left
        return 2*i+1
    def right_child(self,i): #get-right
        return 2*i+1

    def has_parent(self,i):
        if self.getParent(i)!= 0: 
            return True
        else: return False;
    def has_leftChild(self,i):
        if self.left_child(i)!= 0: 
            return True
        else: return False;
    def has_rightChild(self,i):
        if self.right_child(i)!= 0: 
            return True
        else: return False;

    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def insert_key(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def delete_root(self):
        if len(self.heap)==0:
            return -1
        last=len(self.heap)-1
        self.swap(0,last)
        root=self.heap.pop(0)
        self.heapify_down(0)
        return root

    def heapify_up(self,i):
        while (self.has_parent(i)> self.heap[self.getParent(i)] and self.heap[i]> self.heap[self.getParent(i)]):
            self.swap(i,self.getParent(i))
            i=self.get_parent(i)
    def heapify_down(self,i):
        while(self.has_leftChild(i)):
            max_child=self.get_max_child(i)
            if max_child()== -1:
                break;
            if (self.heap[i] < self.heap[max_child]):
                self.swap(i,max_child)
                i=max_child
            else: break;

    def get_max_child(self,i):
        if (self.has_leftChild(i)):
            left_c=self.leftChild(i)
            if (self.has_leftChild(i)):
                right_c=self.rightChild(i)
                if (self.heap[left_c]>self.heap[right_c]):
                    return left_c
                else: return right_c;
        else: return -1;

    def print_heap(self):
        return self.heap


MaxHeap()
a=[45,90,63,27,29,57,42,35,12,24]
for i in range(len(a)):
    MaxHeap().insert_key(a[i])
#print("initial heap: ")
MaxHeap().insert_key(52)
MaxHeap().print_heap()
MaxHeap().insert_key(26)
MaxHeap().print_heap()
print(MaxHeap().getParent(57))
a=MaxHeap().print_heap()
print(a)
for i in range(len(a)):
    print(MaxHeap().getParent(a[i]),end=' ')        

####____Max heap____####
