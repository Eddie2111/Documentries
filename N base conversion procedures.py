def binary(x,base):
    while x>0:
        a=x//base
        print(a,'and',x-a*base)
        return binary(a,base)
        
        
binary(int(input('=>')),int(input('Base:')))
