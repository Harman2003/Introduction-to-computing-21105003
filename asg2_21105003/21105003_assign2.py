#ASSIGNMENT 2

#QUESTION 1:

print("\nQUESTION 1 ")

#Given string
str="Python is a case sensitive language"  

print("\n Given string :  ", str)

# part (a)
print("\n (a) Length of the string is :  " ,len(str))

# part (b)
rev_str= str[::-1]
print("\n (b) Reversed string is : ", rev_str)

# part (c)
new_str = str[10:26]
print("\n (c) New string created stores '%s' in it" %new_str)

# part (d)
changed_str = str.replace(new_str, "object oriented")
print("\n (d) Replacing '%s' with '%s' gives : " %(new_str,"object oriented"), changed_str)

# part (e)

print("\n (e) Index of 'a' in the given string :", str.index("a"))

# part (f)

without_spc = str.replace(" ","")
print("\n (f) After removing white spaces from the input string : ",without_spc)


#QUESTION 2

# Store your name, SID, department name and CGPA into different variables

print("\nQUESTION 2")

name ="Harman Singh"
SID = 21105003
department_name = "Electronics and Communication Engineering "
CGPA = 9.9

print("""\n Hey, %s Here!
 My SID is %d
 I am from %s department and my CGPA is %.1f """ %(name,SID,department_name,CGPA))


#QUESTION 3. 
#Bitwise Calculations

print("\nQUESTION 3")
#given data
a=56
b=10

#(a) bitwise And (&)

print("\n (a)  a&b : ",(a&b))

#(b) bitwise Or (|)

print("\n (b)  a|b : ",(a|b))

#(c) bitwise Xor (^)

print("\n (c)  a^b : ",(a^b))

#(d)  bitwise left shift (<<)

print(''' (d) Left shift:-
             a<<2: %d
             b<<2: %d''' %(a<<2, b<<2))

#(e)  bitwise right shift (>>) 

print(''' (d) Right shift:-
             a>>2: %d
             b>>2: %d''' %(a>>2, b>>2))


# QUESTION 4

print("\nQUESTION 4")

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))

if (num1 >= num2) and (num1 >= num3):
   greatest = num1
elif (num2 >= num1) and (num2 >= num3):
   greatest = num2
else:
   greatest = num3

print("The largest number is: ", greatest)


#QUESTION 5
print("\nQUESTION 5")

name_str = input("\nEnter a string to check if it contains 'name' :  " ).split()
word = "name"
if word in name_str :
    print("Yes")
else:
    print("No")


#QUESTION 6

print("\nQUESTION 6")
sides = [int(x) for x in input("\nEnter three numbers space separated to check triangle property").split()]

sides.sort()
if (sides[0]+sides[1])>sides[2]:
    print("Yes")
else:
    print("No")
