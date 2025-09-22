
salary = float (input("What is your salary? "))
numDependents = float(input("How many dependents do you have? "))

statetax= 0.065
federaltax= 0.28
dependantDeduction= salary * (0.025 * numDependents)
totalwithholdings= (salary * statetax) + (salary * federaltax) + dependantDeduction
takeHomePay= salary - totalwithholdings

print("Your salary is: $" + str(salary))
print("Your take home pay after deductions is: $" + str(takeHomePay))