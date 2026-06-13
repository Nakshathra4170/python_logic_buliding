#Reverse a String
text="python"
new=""
count=len(text)
for  i in range(count):
    new+=text[count-i-1]
print(new)
