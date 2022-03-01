print("Assignment 4\n")


print('\nQuestion 1\n')

def hanoi(n, disk_1 , disk_2 , aux):
    if n == 0:
        return
    
    hanoi(n-1, disk_1 , aux, disk_2)       
    print(f"Move Disk {n} from {disk_1} to {disk_2}")
    hanoi(n-1, aux, disk_2, disk_1)

#calling hanoi funtion for 3 disks
hanoi(3, 'A', 'C', 'B')



print("\nQuestion 2\n")
# Pascal's Triangle


# using recursion
n = int(input("Enter n upto which pascal triangle is to be printed."))
print("\n Recursive Way : \n")
def pascal(n, space=n):
    if n<0:
        return "Rows can't be negative. Please enter a positive value"
    if n == 0:
        return
    
    pascal(n-1,space)

    #printing the spaces
    print('  '*(space-n), end='')

   
    val = 1
    for row in range(1, n+1):

        print(val, end ='   ')

        #using Binomial Coefficient
        # nCr = n! / (r! * (n-r)!)
        val = val * (n - row) // row
    print()

pascal(n)

# using iterations.
print("\n Iterative way : \n")

for row in range(1, n+1):

    # printing spaces.
    print('  '*(n - row), end='') #In each row (n-row) spaces to be printed

    val = 1
    
    #printing values in each row
    for col in range(1, row+1): 
        print(val, end='   ')

        val = val * (row- col) // col
    print()
print("")




print("Question 3\n")

a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))

res= divmod(a, b)
c=res[1]
d=res[0]

print("Remainder is: ", c)
print("Quotient is: ",d)

#Checking if function is callable
flag = callable(divmod)
print(flag, end="")
if a_part == True:
    print(", means it is callable")
else:
    print(", means it is not callable")

#Checking if the values are zero or not
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")

#Adding (4,5,6) to the result and filtering values greater than 4
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")



print("\nQuestion 4\n")

#Class named Student
class Student:

    #Initialising Constructor                                                                                          
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print("Object has been initialised\n")

    def student_info(self):
        print("Student Name : ", self.name)
        print("Roll No : ", self.roll_no)

    #Initailising Destructor
    def __del__(self):
        print("\nObject has been destroyed")

name = input("Enter name of student: ").strip()
roll_no = int(input("Enter SID of %s: " % (name)))

my_student = Student(name,roll_no)  #Creating object
my_student.student_info()           #Printing student Information
del my_student                      #Deleting the student object







print(" \n Question 5 \n")

#Creating a class named Employee
class Employee:

    # Initialising the constructor.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Employee Information
    def emp_info(self):
        print("Employee name : ", self.name)
        print("Employee salary : ", self.salary)

    # Destructor
    #def __del__(self):
    #    del self.name
    #    print("The destructor called, record of %s is deleted. " %self.name)

# Creating objects
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

#Printing Employees details using emp_info() method
employee_1.emp_info()
print()
employee_2.emp_info()
print()
employee_3.emp_info()

# Updating salary of Mehak.
employee_1.salary = 70000

# Calling the emp_info of employee_1
print("\nThe updated data of employee_1 is :")
employee_1.emp_info()
print()
# Deleting the records of employee_3( Viren).
del employee_3
print("Record of Viren is deleted.")



print("\n Question 6 \n")
George_word = input("Enter George's word: ")
Barbie_word = input("Enter Barbie's guessed word: ")

def anagrams(s):
    if s== "":
         return[s]

    ans= []
    for w in anagrams(s[1:]):
       for pos in range(len(w) +1):
          ans.append(w[:pos] + s[0] + w[pos:])
    return ans

Anagrams= anagrams(George_word)

flag= False
for i in Anagrams :
   if i== Barbie_word and flag==False:
         print("Barbie and George are true friends")
         flag= True
if flag==False :         
  print("George and Barbie's friendship is fake")



