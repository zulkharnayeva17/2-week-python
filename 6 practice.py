#task 0
n=int(input('array length'))
m=int(input('array number'))
x=[]
y=[]
for i in range (n):
    print ('enter ', i, 'the element: ')
    x.append(int(input()))
for i in range(n):
    if abs (x[i])>m:
           y.append(x[i])
print ('enter the number M:',m)
print ('array X:',x)
print('array Y:',y)

# task 1
#1)
a = input()
a = a.split()
a = [int(i) for i in a]
for i in range(len(a)//2):
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = b
print(a)
max_number = max(a)
print("maximal number: ", max_number)
#2
numbers = [1, 2, 3, 4, 0, 5]
average = sum(numbers) / len(numbers)
numbers = [average if i == 0 else i for i in numbers]
print(numbers)

#task 2
#1
a = input()
a = a.split()
min_number = min(a)
print("minimal number: ", min_number)
print(a.index(min_number))
#2
numbers = [1,-2, 3, -4, 5, -6]
a = [] 
b = [] 
for num in numbers:
    if -num == -abs(num):
        a.append(num)
    else:
        b.append(num)
print(a)
print(b)

#task 3
#1
a=[1, 2, 3, 4, 5, 6] 
print(sum(x for i,x in enumerate(a) if i % 2 == 1))
#2
a=[1, 2, 3, 43, 5, 16 , 7 , 8]
print([2*x if x < 15 else x for x in a

#task 4
 #1
a = input()
a = a.split()
max_number = max(a)
print("maximal number: ", max_number)
print(a.index(max_number) + 1)

#2
numbers= [1, 2, 3, 4, 5, 6]
res = []
for el in numbers:
    if el % 2 != 0:
        res.append(el)
if len(res) == 0:
    print('No numbers')
 
print(sorted(res, reverse=True))

#task 5
 #1
       
 #2
arr = []
arr_2 = []
for _ in range(10):
   arr.append(int(input('enter the number: ')))
for el in arr:
   if el not in arr_2:
         arr_2.append(el)
print(arr_2)
 #task 6
#1
arr=[]
for value in range(10):
    value=int(input("\nEnter the element of array: "))
    arr.append(value)
 
max_element=max(arr)
print('Maximal element of array:',max_element)
 

for i in arr:
    if i>max_element:
        print(i,">",max_element)
    elif i<max_element:
        print(i,"<",max_element)
    elif i==max_element:
        print(i,"=",max_element)

#2
arr = []
s = 0
for i in range(10) :
    arr.append(int(input('Enter the number: ')))
    if arr[-1] > 5 :
        s += arr[-1]
print(arr)
print(s) 

#task 7
#1
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even=0
product=1
for i in range(len(arr)):
  if arr[i]%2!=0:
     product*=arr[i]
  else:
      sum_even+=arr[i]
print("Sum of even numbers:", sum_even)

#2
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimal=min(arr)
maximal=max(arr)
print('maximal number:', minimal)
print('minimal number:', maximal)

#task 8
#1
a = list(map(int, input().split()))

product= a[0]

for i in range(1, len(a)):

   product *= a[i]

print('sum of numbers' , sum(a))
print('product of numbers', product)

#2
numbers = [1, 2, 3, 4, 0, 5]
average = sum(numbers) / len(numbers)
numbers = [average if i == 0 else i for i in numbers]
print(numbers)

#task 9
#1
n=int(input("array length: "))
x=[]
for i in range(n):
    print('enter the element ',i)
    x.append(int(input()))
print('min modulo number:', min(x, key = abs))
numbers_reverse=x[::-1]
print('the array in reverse order: ', numbers_reverse)

#2
A=[1, 2, 3, 4, -5, 5 , 6]
B=[0,9, 7, 5, 4, 3, 3, 1]
print('original array A: ', A)
print('original array B: ', B)
A,B=B,A
print('new array A: ',A)
print('new array B: ',B)

#task 10
#1
mylist = []
num = int(input("Number of elements: "))
for i in range(0,num):
    ele = int(input("enter the elements: "))
    mylist.append(ele)
newlist = [] 
replist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
print("List of duplicates", replist)
print("Unique Item List", newlist)

#2

arr = [1, 2, 3, 4, 15, 45, 67, 3, 33, 12, 6, 8, 45, 67, 20]
print(*arr)
print(*[0 if i < 10 else 1 if i > 20 else i for i in arr])

#task 11

# 1
a=[]
for i in range(10):
    a.append(i)
x=a[0]
for i in a:
    if i > x and i % 2 == 0:
        x=i
print(x)
#2
a=[1, 2, 3, 4, 5, 6, 7, 12, 13,]

b=[]
for i in a:
    if i % 2 == 0 and i < 10:
        b.append(i)
if len(b) == 0:
    print("There are no numbers according to the given condition")
else:
    print(b)


#task 12

#1
num = list(map(int, input().split()))
min= 0
for i in range(len(num)):
    if num[i] % 2 == 1:
        min= num[i]
        break
for i in range(len(num)):
    if num[i] % 2 == 1:
        if num[i] < min:
            min = num[i]
if min != 0:
    print(min)
else:
    print(0)

#2
 A=[1, 2, 3, 4, -5, 5 , 6]
B=[0,9, 7, 5, 4, 3, 3, 1]
print('original array A: ', A)
print('original array B: ', B)
A,B=B,A
print('new array A: ',A)
print('new array B: ',B)

#task 13

#2
a=[1, 2, 3, 43, 5, 16 , 7 , 8]
print([2*x if x < 15 else x for x in a

# task 14
       n=int(input("array length\n"))
x=[]
for i in range(n):
    print('enter the elenent ',i)
    x.append(int(input()))
max_numb=max(x)
min_numb=min(x)
for i in range(len(x)):
    if x[i]==max_numb: x[i]=min_numb
    elif x[i]==min_numb: x[i]=max_numb
print('new array: ',x)

#15
#1
A = [1, 2, 3, 2 ,1 , 5 ,6]
counter = {}

for elem in A:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)

#2
a=[1, 2, 3, 4, 5, 6 ,7 ,8 ,9]
b= []
for i in a:
    if i % 2 != 0:
        b.append(i)
if len(b) == 0:
    print("There are no numbers according to the given condition")
else:
    print(b)
     




    
