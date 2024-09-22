'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
'''
#using with reverse_function
def reverse_number(number):
    temp=''
    number.reverse()
    for i in number:
        temp+=str(i)+' '
    print(temp)
number1=input().split(' ')
number=[int(i) for i in number1]
reverse_number(number)
#without using the reverse method
def reverse_num_without_using_reverse(number):
    temp=''
    temp_list=number[::-1]
    for i in temp_list:
        temp+=str(i)+' '
    return temp
number1=input().split(' ')
number=[int(i) for i in number1]
print(reverse_num_without_using_reverse(number))    
