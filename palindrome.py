def ispali(lst1,lst2):
    for i in range(len(lst1)):
        if(lst1[i] != lst2[i]):
            return 0
    return 1

word = input("please enter a string: ")

testword=word
testword=testword.lower()
print(testword)
check1=[]

for i in range(len(word)):
    if (ord(testword[i]) == 32): continue
    check1.append(testword[i])

check2=check1[:]
check2.reverse()

if(ispali(check1,check2)):
    print("\n\'", word, "\' is a palindrome!", sep="")
else:
    print("\n\'", word, "\' is not a palindrome.", sep="")

input("\n\nplease press enter to continue")





