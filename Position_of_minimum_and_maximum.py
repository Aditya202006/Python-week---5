#  Write a program to find the position of minimum and maximum elements of a list 

l=[]
s=int(input('Enter size of list :'))
for i in range (s):
	ele=int(input('Enter elements:'))
	l.append(ele)
a=max(l)
b=min(l)
x=l.index(a)
y=l.index(b)
print('Position of Maximum element in a list is :',x)
print('Position of Minimum element in a list is :',y)

''' output : Enter size of list :4
             Enter elements:89
             Enter elements:35
             Enter elements:62
             Enter elements:74
             Position of Maximum element in a list is : 0
             Position of Minimum element in a list is : 1
