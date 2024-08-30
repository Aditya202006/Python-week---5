# Write a program to reverse a list in python

l=[]
s=int(input('Enter no.of elements of list:'))
for i in range(s):
	ele=int(input('Enter elements:'))
	l.append(ele)
n=l[::-1]
print(n)
m=l.reverse()
print(m)

''' output : Enter no.of elements of list:4
	 Enter elements:45
	 Enter elements:18
	 Enter elements:3
	 Enter elements:7
	 [7,3,18,45] 
