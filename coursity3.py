#List construction and list slicing
#mylist: list of y elements, elements are a multiplication of x* (list index + 1)
#mylist01: list of y elements that are either 1 if element of mylist with the same index is odd, 0 if it is even
#mylist_a: list with the elements of mylist that are in odd numbered index
#mylist_p: list with the elements of mylist that are in even numbered index

x = int(input('x = '))
y = int(input('y = '))
mylist = [x*(i+1) for i in range(y)]
mylist01 = [int(bool(mylist[i]%2)) for i in range(y)]
mylist_p = mylist[1:y:2]
mylist_a = mylist[0:y:2]
print(mylist)
print(mylist01)
print(mylist_p)
print(mylist_a)