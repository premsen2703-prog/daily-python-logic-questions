#problem statement: Write a program to check if a person is eligible to vote or not. The person is eligible to vote if his/her age is greater than or equal to 18 and he/she is a citizen of the country.
#approach: We can use an if statement to check if the age of the person is greater than or equal to 18 and if the person is a citizen of the country. We can use the logical operator "and" to check if both conditions are true. If both conditions are true, then we can print a message saying that the person is eligible to vote. Otherwise, we can print a message saying that the person is not eligible to vote.
#code:
a=20
b=True
if(a>=18 and b==True):
    print("eligible to vote")
else:
    print("not eligible to vote")