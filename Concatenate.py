#  Write a program to concatenate two lists index wise 

list1 = ['M', 'na', 'i', 'Abhi']
list2 = ['y', 'me', 's', 'Ram']

zipped = zip(list1, list2)
a=list(zipped)
b=(a[0][0]+a[0][1]),(a[1][0]+a[1][1]),(a[2][0]+a[2][1]),(a[3][0]+a[3][1])
c=list(b)
print(c)

''' output : ['My', 'name', 'is', 'AbhiRam']
