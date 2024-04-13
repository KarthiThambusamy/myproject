     ##  Fibonacci Series ##
n=int(input("Enter a series: "))
first=0
second=1
total=0
for i in range(n):
    print(total,end=' ')
    total = first+second
    second = first
    first = total
