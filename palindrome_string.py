#Palindrome
text="non"
new=""
count=len(text)
for i in range(count):
    new+=text[count-1-i]
if new==text:
    print(text,"is palindrome")
else:
    print(text,"is not palindrome")
