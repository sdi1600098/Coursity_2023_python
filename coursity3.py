

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