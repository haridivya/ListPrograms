'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
'''
size_list=int(input())
list1=[]
sum1=0
for i in range(size_list):
    list1.append(int(input()))
    sum1+=list1[i]
print(sum1)
