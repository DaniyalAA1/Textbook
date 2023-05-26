# This program determines whether a bank customner
# qualifies for a loan.

min_salary = 30000.0 # the minimum annual salary
min_years = 3 # THe minimum years on the job

# Get the customer's annual salary.
salary=float(input('Enter your annual salary:'))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of' + 'years employed:'))

# Determines whether the customer qualifies.
if salary >= min_salary and years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')