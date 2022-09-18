#task0
s=input('Enter a string ')
flag=1
string = ''
for  i in range(len(s)):
    if s[i]!= '':
        string+=s[i]
print(string)
for i in range(len(s)//2):
    if string[i] != string [-i -1]:
        flag=0
        break
if flag: print('Palindrom')
else: print ('not palindrom')


#independent task 1

str = ' eee eee eee ded frfr'
print((' ' + str).lower().count(' e'))

#2
s1 = ' George Bernard Shaw once said about British and Americans: “We are two countries separated by a common language '
print('s1.replace('':'', ''%'' ,2) = ',s1.replace(':', '%',2))
count_o = 0
for s1 in s1:
    if s1 == ':':
        count_o += 1
    else:
        pass
print(count_o)

#3
s1 = 'Last April, John took a trip to Las Vegas, Nevada. Las Vegas is a popular destination in the western portion of the United States. '
print('s1.replace(''.'', '' '' ,2) = ',s1.replace('.', ' ',2))
count_o = 0
for s1 in s1:
    if s1 == '.':
        count_o += 1
    else:
        pass
print(count_o)

#4
s1 = 'aaxxaxxaxaaxa '
print('s1.replace(''a'', '' o'' ) = ',s1.replace('a', 'o'))
count_o = 0
for s1 in s1:
    if s1 == 'a':
        count_o += 1
    else:
        pass
print(count_o)

#5
str = ' EEkkfjjf'
print('str.lower = ', str.lower())

#6
s1 = 'Last april, John took a trip to Las Vegas, Nevada. Las Vegas is a popular destination in the western portion of the United States. '
print('s1.replace(''a'', '' '' ) = ',s1.replace('a', ' '))
count_o = 0
for s1 in s1:
    if s1 == 'a':
        count_o += 1
    else:
        pass
print(count_o)


#7
def f(s): return s[:len(s)//2].replace("n", "*") + s[len(s)//2:]
print(f(input()))


#8
string= ' asdf sadf af addf afsd.'
print(len(string.split()))


#9
text=input("Enter your sentence:")
print("'the' appears", text.count("the"),"times")


#10
s = input('enter the text: ')
print(s.title())


#11
s = input('enter the text: ')
s2="n"
print('s.replace((''!'', ''.'')= ',s.replace('!', '.'))
print('s.count =',s.count(s2))


#12
s = input().split()
for i in s:
    if i[-1] == "i":
        print(i)
#15
num = 0
for i in s:
    if i == "t":
        num += 1
print(num)



