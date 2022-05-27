#Assignment-4
#Keshav Mathur
#SID-21107049
#Branch- Mechanical


#------------------------------------------#
print("Q1")
a=int(input("Enter your marks: "))
if a >= 80:
    print("Your grade is 'A'.")
elif a >= 60:
    print("Your grade is 'B'.")
elif a >= 50:
    print("Your grade is 'C'.")
elif a >= 45:
    print("Your grade is 'D'.")
elif a >= 25:
    print("Your grade is 'E'.")
else:
    print("Your grade is 'F'.") 

#------------------------------------------#
print("Q2")
a=int(input("Enter the year: "))
if a%400 == 0:
    print(a, "is a leap year.")
elif a%4 == 0:
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")

#------------------------------------------#
print("Q3")
import random

i=0
while i<10:
    num1=random.randint(0,10)
    num2=random.randint(0,10)

    print("Solve {} * {}=".format(num1,num2))
    ans=int(input("Enter the answer: "))
    if ans==num1*num2:
        print("Right!")
    else:
        print("Wrong!, the answer is" , num1*num2)
    i+=1

#------------------------------------------#
print("Q4")
for candies in range(200):
    if candies % 5== 2:
        if candies % 6== 3:
            if candies % 7== 2:
                print(candies, "candies are in the bowl!")
#------------------------------------------#

#------------------------------------------#

#Output of the code
'''
Q1
Enter your marks: 80
Your grade is 'A'.
Q2
Enter the year: 2004
2004 is a leap year.
Q3
Solve 10 * 3=
Enter the answer: 30
Right!
Solve 6 * 3=
Enter the answer: 18
Right!
Solve 0 * 4=
Enter the answer: 0
Right!
Solve 2 * 7=
Enter the answer: 15
Wrong!, the answer is 14
Solve 2 * 0=
Enter the answer: 2
Wrong!, the answer is 0
Solve 4 * 4=
Enter the answer: 16
Right!
Solve 0 * 10=
Enter the answer: 0
Right!
Solve 5 * 2=
Enter the answer: 10
Right!
Solve 10 * 9=
Enter the answer: 90
Right!
Solve 3 * 4=
Enter the answer: 12
Right!
Q4
177 candies are in the bowl!
'''
#------------------------------------------#