import sys
import math

annual_salary = int(input('Enter annual salary: '))
portion_saved = float(input('Enter salary saved: '))
total_cost = float(input('Enter cost of dream home: '))
raise_amount = float(input('Enter raise percentage: '))

monthly_salary = annual_salary / 12
monthly_portion_saved = (monthly_salary * portion_saved)
monthly_investment = 0
portion_down_payment = total_cost * 0.25
current_savings = 0
months_needed = 0

while current_savings <= portion_down_payment :
    if months_needed % 6 == 0 and months_needed != 0 :
        nice_raise = monthly_salary * raise_amount
        monthly_salary += nice_raise
        monthly_portion_saved = (monthly_salary * portion_saved)

    current_savings = current_savings + monthly_portion_saved
    monthly_investment = current_savings * .04 / 12
    current_savings = current_savings + monthly_investment
    months_needed += 1

#excess_saved = current_savings - total_cost
#excess_month = excess_saved / monthly_salary
#months_needed = months_needed - excess_month

print(f'You will need {months_needed} months to buy your house.')