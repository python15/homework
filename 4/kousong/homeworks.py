group={3,6,9,8,7}
num=[9,6,7,5,3,3,2,0,4,1,8]
lst1=[10]
lst2=[10]

def sort (iterable,key=lambda a,b: a<b):
    for x in iterable:
        if x  in group:
            for i,y in enumerate(lst1):
                if key(x,y):
                    lst1.insert(i,x)
                    break
        else:
            for j,z in enumerate(lst2):
                if key(x,z):
                    lst2.insert(j,x)
                    break                
    lst1.pop()
    lst2.pop()
    return(lst1+lst2)

print(sort(num))