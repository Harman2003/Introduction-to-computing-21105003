#Question 1
print("Question 1")
words_list = input("Enter the string: ").lower().split()

if len(words_list) == 1:
   words_list = words_list[0]
occurences = {}
for i in words_list:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1

for word_or_char, value in occurences.items() :
    print("%s appeared %d times" %(word_or_char, value))


#Question 2

print("\n\n Question 2")
def leap_year(year: int) -> bool:                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    return False

while True:
    date = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    #Constraints in the given question
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print(''' Please enter the data in the given constraint:
        1<=date<=31
        1<=month<=12
        1800<=year<=2025''')
       
    elif month in (4,6,9,11) and date == 31:                                                                          
        print("This month has 30 days only. Enter a valid date")

    elif month == 2 and date >= 29:                                                                                
        if leap_year(year) and date != 29:
            print("The given month has 29 days only. Enter a valid date")
            
        elif not leap_year(year):
            print("The given month has 28 days only. Enter a valid date")
    
    else :
        break
            
    
#total days in a given month
if month == 2:                                                                                                     
    if leap_year(year):
        totaldays = 29
    else:
        totaldays = 28
elif month in (4,6,9,11):
    totaldays = 30
else:
    totaldays = 31

if date == totaldays:                                                                                                
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1

print("Next Date is: %d / %d / %d" %(date,month,year))



# Question 3 
# Python program to create a list of tuples with the first element as the
# number and Second element as the square of the number.

print("\n\nQuestion 3")
list_numbers = [int(i) for i in input("Enter the numbers in a single line separated by space : ").split()]

final_list = []

for num in list_numbers :
    my_tuple =(num,num**2)
    final_list.append(my_tuple)

print("The updated list is :\n",final_list)



# Question 4
# A program to prompt the user for a grade between 4 and 10
print("\n\nQuestion 4")
grade_system={
             10:("A+","outstanding"),
             9:("A","Excellent"),
             8:("B+","Very Good"),
             7:("B","Good"),
             6:("C+","Average"),
             5:("C","Below Average"),
             4:("D","Poor")
           }

while True :
    grade = int(input("\nEnter your grade between 4 to 10 : "))
    if(grade > 10 or grade <4):
        print("Please enter a valid grade between 4 to 10 : ")
    else:
        break

my_tuple= grade_system[grade]
print("Your Grade is %s and %s Performance." %(my_tuple[0],my_tuple[1]))



# Question 5
# Pattern Printing

print("\n\n Question 5")
string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1



#Question 6

print("\n\n Question 6")
dict1 = {}

#taking input
while True:                                                                                                         
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    
    flag= input("Do you wish to enter more details (Enter Y for yes and N for no) ? : ")
    if flag=='N' or flag=='n' :
         break

# part a
print("\n a. Student data in the order as entered by the user : ")
for student_sid , student_name in dict1.items() :
    print(student_sid," : ",student_name)

# part b
print("\n b. Sorted with respect to names") 
dict2 = {}
for sorted_key in sorted(dict1.values()):                                                                                    
    for student_sid, student_name in dict1.items():
        if student_name == sorted_key :
            dict2[student_sid] = student_name

for student_sid,student_name in dict2.items() :
    print(student_sid," : ",student_name)

# part c
print("\n c. Sorted with respect to SIDs")
sort_sids = sorted(dict1.keys())
dict3 ={}
for ordered_sid in sort_sids:
    for student_sid , student_name in dict1.items():
        if(student_sid==ordered_sid) :
            dict3[student_sid]= student_name

for student_sid,student_name in dict3.items() :
    print(student_sid," : ",student_name)

# part d
print("\n d. Searching student details")
while True:
    findSID = int(input("Enter the SID of the student: "))
    if findSID in dict1:
        print("The name of student whose SID is %d is %s" %(findSID, dict1[findSID]))
        break
    else:
        print("The details of student with SID %d isn't available. Please enter a new SID" %findSID)



#Question 7
print("\n\n Question 7")

a = 0
b = 1
sum = 0

#taking input
while True:                                                                                                       
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
    elif num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else :
        break

print("The Fibonacci sequence is as follows:")
print(a,end=" ")

for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
print("\nAverage of the fibonacci series is %f" %(sum/num))


#Question 8
print("\n\nQuestion 8 ")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

#part a.
print("a. Set of elements that are in Set1 and Set2 but not both:")
set4 = set1^set2
print(set4)

#part b.
print("b. Set of elements that are in only one of the three sets Set1, Set2 and Set3:")
set5 = set1^set2^set3
print(set5)

#part c.
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)

#part d.
print("d. Set of all integers in range 1 to 10 that are not in Set1:")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)

#part e.
print("e. Set of all integers in range 1-10 that are not in Set1, Set2 and Set3:")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
