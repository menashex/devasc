def retlst(strng):
	lst=[]
	for i in range(len(strng)):
		lst.append(strng[i])
	return lst[:]

def countdup(lst1,lst2):
    for i in range(len(lst1)):
	    cnt=0
	    test=lst1.count(i)
	    test+=1
	    for i in range(len(lst2)):
		    if(lst1[i] == lst2[i]):
			    cnt+1
			    if(cnt == test ):
				    print("FAIL countdup")
				    return 0
    return 1

def isin(lst1,lst2):
	for i in range(len(lst1)):
		if(lst1[i] not in lst2):
			print("FAIL isin")
			return 0
	for i in range(len(lst2)):
		if(lst2[i] not in lst1):
			print("FAIL isin")
			return 0
	return 1


word1=input("please enter first word: ")
word2=input("please enter second word: ")

lst1=retlst(word1)
lst2=retlst(word2)

if(isin(lst1,lst2) and countdup(lst1,lst2)):
	print("is an anagram")
else: print("not an anagram")

