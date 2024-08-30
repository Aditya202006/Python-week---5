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
