#input the number of employees
n = int(input())
#list to store employee with their salaries
employees = []

# Read input and parse names and salaries
data = input().split()
# Step to parse names and salaries
for i in range(n):
    name = data[2 * i]
    salary = data[2 * i + 1]
    employees.append((name, salary))

# sort the employees by their salaries
employees.sort(key=lambda x: x[1])

#print the list by minimum salaries to higher
for employee in employees:
    print(employee[0])

'''
Sample Input :
3
Karthik 23000 rohan 81734 varshini 12343
Sample Output :
varshini
Karthik
Rohan

'''