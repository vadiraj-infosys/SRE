number = int(input("Enter number range to print Prime numbers: "))
for num in range(2,number):
    if all(num % i != 0 for i in range(2, num)):
        print (num)
        