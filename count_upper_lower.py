#Count Uppercase and Lowercase Letters
text="Python"
upper=0
lower=0
for i in text:
    if i==i.upper():
        upper+=1
    else:
        lower+=1

print("Uppercase:",upper)
print("Lowercase:",lower)
