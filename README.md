# Python
Basic Programming in Python
You'll get to know the basic fundamentals of Python, Programming is done on Eclipes based on Infosys Module


## Fundamentals

### Assignment 1: Simple Print Statement

Objective:
```
print Hello World!
```

### Assignment 2: Observations from a real-world problem - Guided Activity

Objective: Given a real-world problem, be able to understand the need for programming fundamentals such as identifiers, variables, data types etc.

Problem Description: A retail store management wants to automate the process of generating the bill amount for its customers. As an initial step, they want to initialize the bill details of a customer as given below: 
Bill id should be 1001, customer id should be 101 and bill amount should be 199.99. 
After initializing, all the values must be displayed in the format given below: 
```
bill_id: 1001 
customer_id: 101 
bill_amount: Rs.199.99 
```
Analyze the above problem statement and answer the following questions: 
1.	What do you think is needed to write a program to implement the solution for the above problem statement?

Summary of this assignment: In this assignment, you have understood the need of a high-level programming language and programming fundamentals such as identifiers, variables, data types, operators etc.


### Assignment 3: Programming constructs in Python - Guided Activity

Objective: Given a real-world problem, be able to identify the data types of the variables required to solve it 

Problem Description: For the previous assignment, identify the data types that may be used to represent bill id, customer id and bill amount. 

Summary of this assignment: In this assignment, you have learnt to identify the data type for the variables based on the real-world problem 


### Assignment 4: Programming constructs in Python - Quiz

Objective: Given a real-world problem, be able to identify the variables and operators required to solve the problem and implement it using a high-level programming language like Python 
Problem Description: Predict the output of following Python Statements. 
```
print ("Value of e is %0.1f" , 2.713 ) 
print ("Value of e is %0.1f" %2.713 ) 
print ("Programming in Python: Version %d" %3.5 ) 
print ("%20s : %d" % ("Python 3.0 is also known as Python",3000.57 )) 
x=2 
print ("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x)) 
```
Summary of this assignment: In this assignment, you have learnt to make use of format specifiers for different type of data variables based on the real-world problem 


### Assignment 5: Programming constructs in Python - Demo

Objective: Given a real-world problem, be able to identify the variables and operators required to solve the problem and implement it using a high-level programming language like Python 

Problem Description: Write a Pseudocode and Python program to implement the real-world problem discussed in Programming constructs in Python Assignment 2. Compile and execute the program using Eclipse IDE. 
You may want to refer to Programming constructs in Python Assignment 1 to understand how Eclipse IDE may be used for writing and executing a Python program. 

INITIALIZE_VARIABLES_DISPLAY 
1. bill_id = 1001 
2. customer_id = 101 
3. bill_amount = 199.99 
4. display "Bill Id:", bill_id 
5. display "Customer Id:", customer_id 
6. display "Bill Amount:Rs.", bill_amount 

Summary of this assignment: In this assignment, you have understood how to implement the solution for a simple real-world problem using variables and operators 


### Assignment 6: Programming constructs in Python – Hands on practice

Objective: Given a real-world problem, be able to identify the variables and operators 
required to solve the problem and implement it using a high-level programming language like Python 

Problem Description: The finance department of a company wants to calculate the monthly pay of one of its employee. Monthly pay should be calculated as mentioned in the below formula and display all the employee details.
```
Monthly Pay = Number of hours worked in a week * Pay rate per hour * No. of weeks in a month 
```
Note: 
The number of hours worked by the employee in a week should be considered as 40, 
Pay rate per hour should be considered as Rs.400 and 
Number of weeks in a month should be considered as 4 
Write Pseudo code and Python program in Eclipse to implement the above real-world problem. 

Summary of this assignment: In this assignment, you have learnt to implement the solution for a simple real-world problem using variables and operators 


### Assignment 7: Programming constructs in Python - Hands - on - Practice

Objective: Given a real-world problem, be able to identify the variables and operators required to solve the problem and implement it using a high-level programming language like Python 

Problem Description: Write the assignment statement to swap 2 numbers x and y? (Without using temp variable) 

Summary of this assignment: In this assignment, you have learnt to implement the solution for a simple real-world problem using variables and operators


### Assignment 8: Programming constructs in Python - Guided Activity

Objective: Given a real-world problem, be able to identify the variables and operators required to solve the problem and implement it using a high-level programming language like Python 

Problem Description: Predict the output of following code snippet 
```
num = 16 
num1 = num/6 
num2 = num//6 
num3 = num//6.0 
print(num1) 
print(num2); 
print(num3) 
```
Summary of this assignment: In this assignment, you have learnt to implement the solution for a simple real-world problem using variables and operators 


### Assignment 9: id() and type() functions - Quiz

Objective: Revisit the concept and usage of id() and type() functions 

Problem Description: 
Dry run the below code snippets and predict the output. You may want to confirm the output by executing the code using Eclipse IDE. 

#### Code – 1:
```
obj_x = 10 
obj_y = obj_x 
if ( id(obj_x) == id(obj_y) ): 
print("Address of obj_x and obj_y is same") 
else: 
print("Address of obj_x and obj_y is not same") 
```
#### Code – 2: 
```
obj_x = 10 
obj_y = obj_x 
if ( obj_x is obj_y ): 
print("obj_x and obj_y have same identity") 
else: 
print("obj_x and obj_y do not have same identity") 
```
#### Code – 3: 
```
obj_x = 10 
obj_y = obj_x 
obj_y = obj_x + 1 
if ( obj_x is not obj_y ): 
print("obj_x and obj_y do not have same identity") 
else: 
print("obj_x and obj_y have same identity") 
```
#### Code – 4: 
```
int_a = 10 
raw_input = input("Enter a number") 
print("Type of int_a:", type(int_a)) 
print("Type of raw_input:", type(raw_input)) 
print(int_a + raw_input) 
```
Summary of this assignment: In this assignment, you have understood the concept and usage of id() and type() built-in functions. 


#### In Code 4 there's meant to be an error (type error), to show that int & str can't be concatenated straight away



## Control Structures

### Assignment 10: Coding Standards - Guided Activity

Objective: Given a set of source code and an identified set of best practices, be able to implement the techniques during coding 
Problem Description: Coding standards are very important for maintenance of code and for understanding of the code. Identify the sections of the given program where the coding standards are not followed and correct them. 
```
itemNo=1005 unitprice = 250 
quantity = 2 
amount=quantity*unitprice 
print("Item No:",itemNo) 
print("Bill Amount:",amount) 
```
Summary of this assignment: In this assignment, you have learnt Python coding standards 


### Assignment 11: Control Structures – Observations from a real-world problem - Guided Activity

Objective: Given a real-world problem be able to understand the need for control structures and operators to implement the logic and solve the problem 

Problem Description: The scenario discussed in Programming Fundamentals Assignment 5 is revisited here. Suppose the retail store management now wants to provide 2% discount for all bill amounts above Rs.500 and for all other bill amount, a discount of 1%. 
What do you think is needed to implement this scenario? 

Summary of this assignment: In this assignment, you have understood the need of operators and control structures using a real-world problem  


### Assignment 12: Control Structures - Demo

Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem

Problem Description: Suppose the retail store management now wants to provide 2% discount for all bill amounts above Rs.500 and for all other bill amont, a discount of 1%.

Write a Python program to implement the same?
```
bill_id = 1001 
customer_id = 101 
bill_amount = 200.0 
discounted_bill_amount = 0.0 
print("Bill Id:%d" %bill_id) 
print("Customer Id:%d" %customer_id) 
Note the use if else statement 
print("Bill Amount:Rs.%f" %bill_amount) 
if bill_amount > 500: 
  discounted_bill_amount = bill_amount - bill_amount * 2 / 100 
else: 
  discounted_bill_amount = bill_amount - bill_amount * 1 / 100 
print("Discounted Bill Amount:Rs.%f" %discounted_bill_amount) 
```

Summary of this assignment: In this assignment, you have understood the implementation of operators and control structures using a real world problem


### Assignment 13: Control Structures - Guided Activity

Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem

Problem Description: Suppose the retail store management now wants to provide discount for all bill amounts as mentioned below.
Assume bill amount will be always greater than 0.
Note Note Note Note the use if else statement the use if else statement the use if else statement the use if else statement the use if else statement the use if else statement the use if else statement the use if else statement the use if else statement
```
Bill Amount
Discount          %
>=1000            5
>=500 and <1000   2
>0 and <500       1
```
Write a Python program to implement the same?
```
bill_id = 1001 
customer_id = 101 
bill_amount = 1200.0 
discounted_bill_amount = 0.0 
discount = 0 
print("Bill Id: %d" %bill_id) 
print("Customer Id: %d" %customer_id) 
print("Bill Amount:Rs. %f" %bill_amount) 
if bill_amount >= 1000: 
  discount = 5 
elif bill_amount >= 500: 
  discount = 2 
else: 
  discount = 1 
discounted_bill_amount = bill_amount - bill_amount * discount / 100 
print("Discounted Bill Amount:Rs. %f" %discounted_bill_amount)
```

Summary of this assignment: In this assignment, you have understood the implementation of operators and control structures using a real world problem


### Assignment 14: Control Structures - Guided Activity

Objective: Given a real-world problem be able to understand the need for control structures and operators to implement the logic and solve the problem 

Problem Description: Suppose the retail store management now wants to provide discount for all bill amounts as mentioned below.

Customers can be considered to be valid, if their customer id is between 101 and 1000(both inclusive). 
For valid customers, discount must be provided as per the table given below:
```
Bill Amount	
Discount % 
>=500 	10 
```


### Assignment 15: Control Structures – Hands – on – Practice

Objective: Given a real-world problem be able to understand the need for control structures and operators to implement the logic and solve the problem 

Problem Description: Objective: Given a real-world problem be able to understand the need for control structures and operators to implement the logic and solve the problem 

Problem Description: The finance department of a company wants to calculate the monthly net pay of one of its employee by finding the income tax to be paid (in Indian Rupees) and the net salary after the income tax deduction. The employee should pay income tax if his monthly gross salary is more than Rs. 10,000 (Indian Rupees) and the percentage of income tax should be considered as 20% of the gross salary. 
Display the employee id, basic salary, allowances, gross pay, income tax and net pay. 
Note:
```
Employee Id must be considered as 1001, 
Basic salary of the employee must be considered as Rs.15000.00 and 
Allowances must be considered as Rs.6000.00 
```
Write a Pseudo code and Python program in Eclipse to solve the above real-world problem. 
Refer below for the formulae to be used. 
```
Monthly Gross Salary = Basic Salary + Allowances 
Net Salary = Gross Salary – Income Tax 
```
Summary of this assignment: In this assignment, you have understood the implementation of operators and control structures using a real-world problem 


### Assignment 16: Control Structures – Hands - on - Practice

Objective: Given a real-world problem be able to understand the need for control structures and operators to implement the logic and solve the problem 

Problem Description: Extend the program written for Assignment 15 to find the income tax to be paid (In Indian Rupees) and the total salary after the income tax deduction as per the details given in below table. 
```
Gross Salary (In Indian Rupees) 	Income Tax percentage 
Below 5,000                               Nil 
5,001 to 10,000                           10 % 
10,001 to 20,000                          20% 
More than 20,000                          30% 
```
Display the employee id, basic salary, allowances, gross pay, income tax and net pay. 

Note: 
Employee Id must be considered as 1001, 
Basic salary of the employee must be considered as Rs.15000.00 and 
Allowances must be considered as Rs.6000.00 
Write a Pseudo code and Python program in Eclipse to solve the above real-world problem. 

Summary of this assignment: In this assignment, you have understood the implementation of operators and control structures using a real-world problem 


### Assignment 17: Iteration Control Structures - Guided Activity

Objective: Given a real-world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object-oriented programming language (Python) 

Problem Description: 
Dry run the below code snippets and predict the output. You may want to confirm the output by executing the code using Eclipse IDE. 

#### Code-1: 
```
counter = 1 
while counter <= 3: 
  print(counter) 
  counter += 1 
print("End of Program") 
```
#### Code-2: 
```
print("To find the sum of first 10 integers:") 
result = 0 
for value in range(1,11): 
  result = result + value 
print("Sum:",result); 
```
#### Code-3: 
```
number = 1 
result = 0 
while number < 5: 
  result = result + number 
  number = number + 1 
print(result) 
```
#### Code-4:
```
result = 0 
for index in range(40, 10, -2): 
  if(index % 5 == 0): 
  result = result + index 
print(result) 
```
#### Code-5:
```
amount = 100.0 
interest = 0.0 
months = 1 
while months < 6: 
  interest = amount * 0.2 
  amount = amount + interest 
  months += 1 
print(amount) 
```
Summary of this assignment: In this assignment, you have understood the implementation of iteration control structures.


### Assignment 18: break statement - Demo

Objective: Given a real-world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object-oriented programming language (Python) 

Problem Description: 
Dry run the below code snippet and predict the output. You may want to confirm the output by executing the code using Eclipse IDE. 

#### Code
```
count = 0
result = 0 
for count in range (1, 10): 
  result = result + count 
```
On countering the break statement, control will move out of the loop as shown here
Note the use of break statement 
```
if result > 6: 
  break 
print("Result =", result) 
```
Summary of this assignment: In this assignment, you have understood the implementation of break statement. 


### Assignment 19: continue statement - Demo

Objective: Given a real-world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object-oriented programming language (Python) 

Problem Description: 
Dry run the below code snippet and predict the output. You may want to confirm the output by executing the code using Eclipse IDE. 

#### Code 
```
count = 0 
  for count in range(0,10): 
    if 4 == count: 
      continue 
    print(count) 
```
Summary of this assignment: In this assignment, you have understood the implementation of continue statement.


### Assignment 20: Iteration Control Structure – Debugging - Guided Activity

Objective: Given a real-world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object-
oriented programming language (Python) 

Problem Description: The code given below is written to display all the even numbers between 50 and 80 (both inclusive). Debug the program to get the correct output. 

Step 1: Type the below program in Eclipse, save the file as for_loop.py, compile and execute. 
```
for i in range (50, 80): 
  if i % 2 == 0: 
    print(i) 
  else: 
    break 
Step 2: Correct the logical error in the code, save, compile and execute the code 
Step 3: Implement the same logic using while loop 
```
Summary of this assignment: In this assignment, you have learnt the implementation of iteration control structure and break statement. 



## Strings - Assignments

### Assignment 21: Strings – Observations from Retail Application - Guided Activity

Objective: Observe the need for features in the retail application scenario to correlate the application of Strings 

Problem Description: In the retail application, along with the earlier details included for Customer, the retail shop wants to keep track of customer name. Customer name should be between 3 and 20 characters. 

Answer the following question: 
What do you think is needed to implement the solution for the above problem? 

Summary of this assignment: In this assignment, you have understood the need of strings using a retail application scenario


### Assignment 22: Strings – Demo

Objective: Observe the need for features in the retail application scenario to correlate the application of Strings 

Problem Description: In the retail application, along with the earlier details included for Customer, the retail shop wants to keep track of customer name. Customer name should be between 3 and 20 characters. 
```
bill_id = 1001 
customer_id = 1001 
bill_amount = 2000 
customer_name = Kevin 
```
#### Code
```
bill_id = input("Please enter Bill id") 
customer_id = input("Please enter Customer id") 
bill_amount = input("Please enter bill Amount") 
customer_name = input("Please enter Customer Name") 
if ((len(customer_name) >= 3) and (len(customer_name) <= 20)) is True: 
  print("Bill Id: ",bill_id) 
  print("Customer Id: ",customer_id) 
  print("Bill Amount:Rs. ",bill_amount) 
  print("Customer Name: ",customer_name) 
else: 
  print("Invalid customer name. Customer name must be between 3 and 20 characters");
```
Summary of this assignment: In this assignment, you have understood the implementation of Strings and String methods using a retail application scenario 


### Assignment 23: Strings – Quiz

Objective: Revisit String concepts through a quiz
 
Problem Description: 
Assume, 
string1 = “Infosys Limited” 
string2 = “Mysore” 
Predict the output of following statements: 
```
Q1: print(string1[:4]) 
Q2: print(string1[-1]) 
Q3: print(string1 * 2) 
Q4: print(string1[:-1] + string2 + string1[:-1]) 
Q5: print (string2[1]) 
Q6: print (string2[4]) 
Q7: print(string1 * 2 + string1[:-1] + string2) 
```
Summary of this assignment: In this assignment, you have revisited concepts of strings through code snippets


### Assignment 24: Strings – Hands - on - Practice 

Objective: Given a computational problem, be able to use the right data structures (lists and strings) and implement the solution to the problem and test using a set of values in an IDE 

Problem Description: 
```
a. Write a program to count and display the number of capital letters in a given string. 
b. Write a program to check if the given string is Palindrome or not? 
c. Write a program to count the number of each vowel in a string 
d. Write a program to remove all punctuation from the string provided by the user 
    punctuations = '''!()-[]{};:'"\,<>./?@###$%^&*_~''' 
```
Hint: Use membership operators IN, Not IN 

Summary: In this assignment, you have understood the application and implementation of Strings concept for the given computational problem.


### Assignment 25: Strings – Hands – on - Practice 

Objective: Given a computational problem, be able to use the right data structures (lists and strings) and implement the solution to the problem and test using a set of values in an IDE 

Problem Description: Write a Python program to accept a string and display the resultant string in reverse order. The resultant string should contain all characters at the even position of accepted string ignoring blank spaces. 
```
accepted_string: An apple a day keeps the doctor away 
resultant_string: Aapedyepteotrwy 
expected_output: ywrtoetpeydepaA 
```
Summary: In this assignment, you have understood the application and implementation of Strings concept for the given computational problem. 


### Assignment 26: Strings – Hands – on - Practice 

Objective: Given a computational problem, be able to use the right data structures (lists and strings) and implement the solution to the problem and test using a set of values in an IDE 

Problem Description: Given a string containing both upper and lower case letters. Write a Python program to count the number of repeated characters and display the maximum count of a character along with the character. 
```
Sample Input: ABaBCbGc 
```
Summary: In this assignment, you have understood the application and implementation of Strings concept for the given computational problem. 


### Assignment 27: Strings – Hands - on - Practice 

Objective: Given a computational problem, be able to use the right data structures (lists and strings) and implement the solution to the problem and test using a set of values in an IDE 

Problem Description: Consider 2 strings string1 and string2 and display the merged_string as the output. The merged_string should be capital letters from both the strings in the order they appear. 

Note: Each character should be checked if it is a capital letter and then it should be merged. 
#### Sample Input: 
```
string1: I Like C 
string2: Mary Likes Python
merged_string: ILCMLP 
```
Summary: In this assignment, you have understood the application and implementation of Strings concept for the given computational problem. 


### Assignment 28: Operations on Tuples - Demo 

Objective: To understand the operations that can be performed on Tuples through a quiz 

Problem Description: 
Assume, 
```
head = ("CEO",) 
elements = ('Air', 'Water', 'Fire', 'Light', 'Land') 
```
Predict the output of following statements: 
```
Q1: print(head) 
Q2: print(elements) 
Q2: print(elements[3]) 
Q3: elements[0]='Ice' 
Q5: print(elements[-1]) 
Q6: print(elements[4]) 
Q7: print(elements[5]) 
```
Summary of this assignment: In this assignment, you have revisited concepts of tuples through code snippets 

#### There's meant to be 2 errors in this code in line 10 & 12 , however you won't be able to see the error of 12th line for that you need to remove line 10 to see it.
```
Line 10 - IndexError: tuple index out of range
Line 12 - TypeError: 'tuple' object does not support item assignment
```


### Assignment 29: Tuples – Hands – on - Practice 

Objective: Given a List of elements representing a computational problem, be able to provide solution by performing required operations using data structures like tuple from an object oriented language (Python) using Eclipse IDE 

Problem Description: Consider the list of courses opted by a Student “John” and available electives as a part of Student Management System. 
```
courses = (“Python Programming”, “RDBMS”, “Web Technology”, “Software Engg”). 
electives = (“Business Intelligence”, “Big Data Analytics”) 
```
Write a Python Program to satisy following business requirements: 
a. List the number of courses opted by Student by “John” 
b. List all the courses opted by Student “John”. 
c. Students “John” is also interested in elective course mentioned above. Print the updated tuple including electives 
d. Check whether Student “John” is allowed to change his course from “Software Engg” to “Computer Networks”. If yes, print the updated course list else mention the reason for the same. 

Summary of this assignment: In this assignment, you have learnt the implementation of Tuple operations for given business scenario. 



## Lists - Assignments

### Assignment 30: Accessing Elements from Lists - Demo 

Objective: Given a List of elements representing a computational problem, be able to access elements in different ways using an object oriented language (Python) using an IDE 

Problem Description: 
Assume, 
```
language = ['Python'] 
languages = ['Python', 'C', 'C++', 'Java', 'Perl'] 
```
Predict the output of following statements: 
```
Q1: print(language) 
Q2: print(languages) 
Q3: print(languages[0:3]) 
Q4: print(languages[1:4]) 
Q5: print(languages[2]) 
Q6: print(languages[5]) 
Q7: print (languages[0] + " and " + languages[1] + " are quite different!") 
Q8: print ("Accessing the last element of the list: " + languages[-1]) 
```
Summary of this assignment: In this assignment, you have revisited concepts of lists through code snippets


### Assignment 31: Lists – Hands - on - Practice 

Objective: Given a computational problem, be able to use the right data structures (lists and strings) and implement the solution to the problem and test using a set of values in an IDE 

Problem Description: Write a Python program to generate first ‘n’ Fibonacci numbers. Store the generated Fibonacci numbers in a list and display it. 
#### Sample input: Enter n 5 
#### Sample Output: List: [0, 1, 1, 2, 3] 

Summary: In this assignment, you have understood the application and implementation of Lists concept for the given computational problem. 


### Assignment 32: Lists – Hands - on - Practice 

Objective: Given a List of elements representing a computational problem, be able to sort the elements in ascending/descending order using an object oriented language (Python) using an IDE

Problem Description: You have a bundle of currency of varied denominations. You want to arrange them in descending order. 
Given below is one approach to perform the above operation.
```
Algorithm: Bubble Sort (List of N element) 
Input: A List of N elements to be sorted 
```
Summary: In this assignment, you have understood the application and implementation of Lists concept for the given computational problem


### Assignment 33: Lists - Hands - on - Practice 

Objective: Given a computational problem, Implement the solution for the problem using suitable data structures from an object oriented language (Python) using an IDE 

Problem Description: ABC Retail Store sells different varieties of Furniture to the customers. The list of furnitures available and its cost list are given below:
```
Furniture     Sofa set  Dining table  T.V. Stand  Cupboard 
Cost in Rs.   20,000    8,500         4,599 	    13,920 
```


### Assignment 34: Sets - Demo

Objective: Given a Set of elements representing a computational problem, be able to perform different operations using an object oriented language (Python) using an IDE

Problem Description:
Consider the sets,
```
fruits = {"apple", "orange", "banana", "apple", "pear", "papaya", "papaya"}
fruit_basket = {"apple", "banana", "grapes", "mango", "kiwi"}
```
Predict the output of following statements:
```
Q1: print(fruits) 
Q2: print(fruits & fruit_basket) 
Q3: print(fruits | fruit_basket) 
Q4: print(fruits - fruit_basket) 
Q5: print(fruits ^ fruit_basket)
Q6: print(len(fruit_basket)) 
Q7: print("pear" in fruits) 
Q8: print("pear" not in fruit_basket) 
Q9: print(fruits.issubset(fruit_basket)) 
Q10: print(fruits.issuperset(fruit_basket)) 
Q11: print(fruit_basket.copy())
```
Summary of this assignment: In this assignment, you have revisited concepts of Sets through code snippets


### Assignment 35: Sets – Hands - on - Practice

Objective: Given a Set of elements representing a computational problem, be able to provide solution by performing required operations on sets from an object oriented language (Python) using an IDE

Problem Description: Consider the scenario from course in student management system. Given below are 2 Sets representing the names of students enrolled for a particular course.
```
java_course = {“John”, “Jack”, “Jill”, “Joe”}
python_course = {“Jake”, “John”, “Eric”, “Jill”}
```
Write a Python program to satisy below mentioned business requirements:
a. List the number of Students enrolled for Python course
b. List the names of Students enrolled for Java course only
c. List the names of Students enrolled for Python course only
d. List the number and names of Students enrolled for both Java and Python courses
e. List the number and names of Students enrolled for either Java or Python courses but not both
f. List names and number of Students enrolled for either Java or Python courses

Summary of this assignment: In this assignment, you have learnt the implementation of Set operations for given business scenario.


### Assignment 36: Dictionary - Demo

Objective: Given a Dictionary of elements representing a computational problem, be able to perform different operations using an object oriented language (Python) on Eclipse IDE

Problem Description: Given below is a Dictionary customer_details representing customer Details from Retail Application - Customer Id is key and Customer Name is value.
```
customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
```
Write Python code to perform below mentioned operations:
a. Print details of Customers
b. Print number of Customers
c. Print Customer names in ascending order
d. Delete the details of customer with customer id = 1005 and print updated dictionary
e. Update the name of customer with customer id = 1003 to “Mary” and print updated dictionary
f. Check whether details of customer with customer id 1002 exists in the dictionary.

Summary of this assignment: In this assignment, you have learnt the implementation of Dictionary operations for given business scenario.


### Assignment 37: Dictionary – Hands - on - Practice

Objective: Given a computational problem, select the right set of data structures (lists and dictionary) and implement the solution to problem and test using a set of values in an IDE

Problem Description: Consider the scenario of processing marks of students for a course in student management system. Given below is the list of marks scored by students. Find top three scorers for the course and also display average marks.
Implement the solution for given business scenario.
```
Student Name  Marks Scored
John          86.5
Jack          91.2
Jill          84.5
Harry         72.1
Joe           80.5
```
Summary: In this assignment, you have understood the application and implementation of Dictionary concept for the given computational problem.
