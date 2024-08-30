#  Write a program to Extract Even or odd number from a given list in python

l=[]
s=int(input('Enter size of list :'))
for i in range (s):
	ele=int(input('Enter elements:'))
	l.append(ele)
even=[]
odd=[]
for i in range(s):
	if l[i]%2==0:
		even.append(l[i])
	else:
		odd.append(l[i])
print('Even numbers in a given list is :',even)
print('Odd numbers in a given list is :',odd)

''' output : Enter size of list :4
             Enter elements:45
             Enter elements:99
             Enter elements:41
             Enter elements:36
             Even numbers in a given list is : [36]
             Odd numbers in a given list is : [45, 99, 41]
