##author: Sushant Bajracharya(sussyoung9@gmail.com)
##time taken:3hrs

MONTHS = 12
outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
monthly_interest_rate = annual_interest_rate/MONTHS
interest_paid = round(monthly_interest_rate * outstanding_balance, 2)
monthly_payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))
total_paid = 0

for i in range(0, MONTHS):
    monthly_payment = round(monthly_payment_rate * outstanding_balance, 2)
    principal_paid = round(monthly_payment - interest_paid, 2)
    outstanding_balance = round(outstanding_balance - principal_paid, 2)
    total_paid += round(monthly_payment, 2)
    print("Month: " + str(i + 1))
    print("Minimum monthly payment: $" + str('%.2f' % (monthly_payment)))
    print("Principle paid: $" + str('%.2f' % (principal_paid)))
    print("Remaining balance: $" + str('%.2f' % (outstanding_balance)))


print("RESULT")
print("Total amount paid: $" + str('%.2f' % (total_paid)))
print("Remaining balance: $" + str('%.2f' % (outstanding_balance)))


