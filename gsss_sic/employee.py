emp_name=input("Enter employee name: ")
emp_id=input("Enter employee ID: ")
basic_salary=int(input("Enter employee monthly salary: "))
emp_splary=int(input("Enter employee special allowance: "))
bonus=int(input("Enter employee bonus: "))
monthly_gross_salary=basic_salary + bonus
annual_gross_salary=(monthly_gross_salary * 12)+(bonus %100)*basic_salary
print("Employee Details:")
print("Employee Name:", emp_name)
print("Employee ID:", emp_id)
print("Monthly Gross Salary:", monthly_gross_salary)
print("Annual Gross Salary:", annual_gross_salary)