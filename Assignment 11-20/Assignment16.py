Employee_id = 1001
Basic_salary = 15000
Allowances = 6000
Income_tax = 0

print("Employee id: %d" %Employee_id)
print("Basic salary: %f" %Basic_salary)
print("Allowances : %f" %Allowances)

Gross_Salary=Basic_salary+Allowances
print("Gross salary: %f" %Gross_Salary)

if(Gross_Salary < 5000):
    print("Income tax: %f" %Income_tax)
elif(Gross_Salary > 5000 and Gross_Salary > 10000):
    Income_tax = Gross_Salary*0.1
    print("Income tax: %f" %Income_tax)
elif(Gross_Salary > 10000 and Gross_Salary > 20000):
    Income_tax = Gross_Salary*0.2
    print("Income tax: %f" %Income_tax)
elif(Gross_Salary > 20000):
    Income_tax = Gross_Salary*0.3
    print("Income tax: %f" %Income_tax)

Net_Salary=Gross_Salary-Income_tax
print("Net salary: %f" %Net_Salary)