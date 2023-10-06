a = int(input("Enter number : "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("case is 2")
    case 13:
        print("Case is 13")
    case 22:
        print("case is 22")
    case _:
        print("No match found")

# Quick quiz: Write a python program to print table of a number which lies between 1 to 10
num= int(input("Enter the number : "))

for i in range(1,11):
    print(num, 'x',i,'=',num*i)