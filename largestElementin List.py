'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
size_list=int(input())
list1=[]
sum1=0
for i in range(size_list):
    list1.append(int(input()))
print(max(list1))
