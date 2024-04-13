## Program to check a palindrome ##

a=input("Enter a string: ")
rev=""
for i in range(len(a),0,-1):
    rev += a[i-1]
if rev == a:
    print("It is a palindrome")
else:
    print("It is not a palindrone")
