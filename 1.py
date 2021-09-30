array=[]
print("введите количество элементов массива")
n=int(input())
for i in range (n):
	print("введите элемент массива")
	array.append(int(input()))
print("введите значение дельта")
d=int(input())
m=min(array)
k=0
for i in range (n):
	if array[i]-m==d:
		k=k+1
print("количество элементов, отличающихся от минимального на дельта =",k)
