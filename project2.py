#task-1
a=int(input("Enter a number:"))
# program even or odd
if a%2==0:
    print("the number is even")
elif a%2==1:
    print("the number is odd")
else:
    print("not a valid number")

# task-2
for i in range(1,51):
    print(i)

#integer numbers sum
k=0
for i in range(1,51):
    k=k+i
print(k)
print("the sum of first 50 numbers is:",k)