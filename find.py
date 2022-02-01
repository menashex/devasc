def pos(source,Find):
	return source.find(Find)

def ishidden(lst):
	for i in range(len(lst)):
		if(i == len(lst)): break
		if(lst[i]<lst[i]+1):
			return 0
	return 1

first=input("enter word: ")
second=input("enter string: ")

lst=[]


for i in range(len(first)):
	lst.append(pos(second,first[i]))

if(ishidden(lst)):
	print("yes!", first, "is hidden in", second)
else:
	print("no,", first, "isn't hidden in", second)