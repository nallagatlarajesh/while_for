num=int(input("enetr the number:"))
for i in range(2,num):
    if num%i==0:
        print(i,"factor")
        print(num,"is not prime number")
        break
else:
    print(num,"is prime number")
