
#task 1
list_numbers=[1, 2, 3, 4, 5, 6, 7, 12, 13]
print('list  :', list_numbers)
res = list_numbers[::-1]
print('reversed list:', res)


#task 2
def change(list_numbers):
    list_numbers[0], list_numbers[-1] = list_numbers[-1], list_numbers[0]
    return list_numbers
#checking
print(change([1, 2, 3, 4, 5, 6  ]))


#3
def to_list(*args):
    return list(args)
#checking
print(to_list(1, 2 , 5, 6,))

#4
def useless(llst):
    return max(llst) / len(llst)
#checking
print(useless([1, 2, 6]))
print(useless([5, 6 , 34]))
    

#5
def list_sort(llst):
    llst.sort(key=lambda x: abs(x), reverse=True)
    return llst

#checking
print(list_sort([1, 3, 4 , 5, 6, 8]))


#6
lst = ["aaa", "vvv", "Dilnaz", "Zulkharnayeva"]
print([x.rjust(len(max(lst, key = len)), '_') for x in lst])
