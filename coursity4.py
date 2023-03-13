s = str(input("String: "))
if len(s) == 1:
    print("Length = 1")
elif s == s[::-1]:
    adict = {s:len(s)}
    alist = list(s)
    print(adict)
    print(alist)
else:
    print("Not a palindrome")