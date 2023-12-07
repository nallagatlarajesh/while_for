#program to input n numbers from user 
#store these numbesr in tuple 
# print the maximum and minimum numbers from this tuple 
numbers=tuple()
n=int(input("how many numbers you waNT TO ENTER:"))
for i in range (0,n):
    num=int(input())
    numbers=numbers+(num,)
print('\nthe numbers in the tuple are:')
print(numbers)
print('\nthe maximum numbers is:')
print(max(numbers))
print('\nthe minimum number is :')
print(min(numbers))
