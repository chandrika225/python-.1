'''list_1 = [3,6,5,8,4,6,8,4,3]
first_sum=sum(list_1)
second_sum = sum(set(list_1))*2
res = second_sum-first_sum
print(res)




n =254    #int(input())
fact = 1
for i in range(n,1,-1):
    fact = fact * i
print(fact)




n=int(input())
fact = 0
for i in range(1,n):
    fact+=n*i
print(fact)




n=int(input())
print(n*(55))

//Linear Search//

list_1 = [1,7,9,7,4,6,2]
target = 2
for i in range(len(list_1)):
    if target==list_1[i]:
        print(i)
        break'''





list_1 = [1,2,3,4,5,6,7,8,9,10]
target = 11
start = 10
end = 9
index = -1
while(start<=end):
    middle = (start+end)//2  
    if list_1[middle]==target:
        index =(middle)
    elif list_1[middle]>target:
        end = middle-1
    elif list_1[middle]<target:
        start = middle+1
        




















