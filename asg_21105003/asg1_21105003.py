# 1st question

#Average of three numbers given by user
print("-> Question 1")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

Sum = num1 + num2 + num3    # sum of given numbers
avg  = Sum / 3              # average of given numbers

print("Average of given numbers is ", avg ,'\n')



# 2nd question

# Calculating tax in dollars.
print("-> Question 2")
print(" All values are to be entered in dollars.")
gross_income = float(input("Enter your gross income: $"))
dependents = int(input("Enter no of dependents: "))

#Given data
tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000

#formula for taxable income
taxable_income = (gross_income - standard_deduction - (dependent_deduction*dependents))
tax = taxable_income*tax_rate
print("The tax you need to pay is $", tax,'\n') 


# 3rd question

# Details of a Student
print("-> Question 3")
print("Student = [SID, Name, Gender, Course, Cgpa]")
sid = int(input("Enter your SID: "))
name = input("Enter your name: ")
gender = input("Enter your gender 'M', 'F', 'O'. M-> Male, F-> Female, O-> Others : ")
course = input("Enter your course name: ")
cgpa = float(input("Enter your cgpa: "))

student = [sid, name, gender, course, cgpa]   # converting data provided by user into list.
print("Student details: ", student, '\n')

# 4th question

# Marks of 5 students

print("-> Question 4")
# taking input from user
a = int(input("Enter marks of student 1: "))
b = int(input("Enter marks of student 2: "))
c = int(input("Enter marks of student 3: "))
d = int(input("Enter marks of student 4: "))
e = int(input("Enter marks of student 5: "))

# converting input data into list.
marks = [a,b,c,d,e]
print("Marks of 5 students are ", marks)

# sorting the list in asecending and descending order.
marks.sort()
print("Marks in ascending order ", marks)

marks.sort(reverse = True)
print("Marks in descending order ", marks, '\n')

# 5th question

# Removing the elements of a given list
print("-> Question 5")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

# Removing the 4th term and returning modified list
color.pop(3)
print(" The modified list  is color 1 =", color)

# Replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list is color 2 =", color2)
