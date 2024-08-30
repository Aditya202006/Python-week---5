# Write a python program to interchange first and last elements in a list

l=[]
s=int(input('Enter size of list :'))
for i in range (s):
	ele=int(input('Enter elements:'))
	l.append(ele)
a=l[0]
b=l[-1]
l[0]=b
l[-1]=a
print(l)
