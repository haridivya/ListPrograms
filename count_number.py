'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
#using with count_function
values=input().split(' ')
val=int(input())
number=[int(i) for i in values]
print(number.count(val))
#without using count
values=input().split(' ')
vals=int(input())
number=[int(i) for i in values]
count_num=0
for i in number:
    if i==vals:
        count_num+=1
print(count_num)
