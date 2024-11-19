list1=[]
list2=[]
list1_size=int(input("enter the size of list1:"))
print("the elements of the list1:")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("enter the size of list2:"))
print("the elements in list2:")
for i in range(list2_size):
    list2.append(int(input()))
print(list1,list2)
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
merge_list=(even_list+odd_list)
print(merge_list)
