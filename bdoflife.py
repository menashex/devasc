def calc(x):
	sum=0
	lst=[]
	for i in range(0,len(str(x))):
		lst.append(str(x)[i])
	for i in range(len(lst)):
		sum+=int(lst[i])
		print(sum)
	print("lst: ",lst)
	return sum


bd = int(input("enter birthday in YYYYMMDD format: "))


while(len(str(bd))!= 1):
	bd=calc(bd)

print(bd)
