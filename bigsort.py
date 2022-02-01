numbers=[]
num=1

#creating the list....

print("enter numbers, enter 0 to stop\n")
while(num!=0):
    num = int(input())
    if(num==0):break
    numbers.append(num)
    
#sorting....
big=1
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        if(numbers[j]>numbers[i]):
            switch=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=switch
print(numbers,end="\n")
input("Press enter to exit.....")
