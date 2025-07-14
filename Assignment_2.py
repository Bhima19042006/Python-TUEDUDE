#Task - 1
num=int(input("Enter a number: "))
if(num%2==1):
    print(num, "is an odd number.")
else:
    print(num, "is an even number.")


#Task - 2
total = 0
for i in range (1, 51):
    total+=i
print("The sum of numbers from 1 to 50 is: ",total)