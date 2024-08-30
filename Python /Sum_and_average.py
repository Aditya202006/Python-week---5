#  Write a program to find the sum and average of the list

l=[]
n=int(input('Enter no.of elements : '))
for i in range(n):
	ele=int(input('Enter elements :'))
	l.append(ele)
add=sum(l)
avg=add/n
print('Sum of elements : ',add)
print('Average of elements : ',avg)

''' output : Enter no.of elements : 3
 	     Enter elements :45
	     Enter elements :99
	     Enter elements :7
	     Sum of elements :  151
	     Average of elements :  50.333333333333336
