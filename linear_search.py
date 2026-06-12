number=[1,2,3,4,5,6,7,8,9,10]
b=20
found=False
for i in number:
    if b==i:
       found=True
       break
if found:
    print("Elemt is  found")
else:
    print("ELement is not found")
