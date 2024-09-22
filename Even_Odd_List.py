'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
'''
size_list=int(input())
list1=[]
for i in range(size_list):# it is used for input the values into list
    list1.append(int(input()))
even_list=[]
odd_list=[]
for i in list1:#it is used to check wheather given value is even or odd
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f'The even list {even_list}')
print(f'The odd list {odd_list}')
