##author: Sushant Bajracharya(sussyoung9@gmail.com)
##time taken:
##MONTHS_IN_A_YEAR = 12
##Balance = float(input("How much do you currently owe? "))
##AnnualInterestRate = float(input("What is the annual interest rate? "))
##MonthlyInterestRate = AnnualInterestRate / MONTHS_IN_A_YEAR
##InterestPaid = round(MonthlyInterestRate * Balance, 2)
##MinimumMonthlyPaymentRate = float(input("What is the minimum montly payment rate? "))
##TotalPaid = 0
##
##for i in range(0, MONTHS_IN_A_YEAR): # + 1 to account for offset
##    MinimumMonthlyPayment = round(MinimumMonthlyPaymentRate * Balance, 2)
##    PrincipalPaid = round(MinimumMonthlyPayment - InterestPaid, 2)
##    Balance = round(Balance - PrincipalPaid, 2)
##    TotalPaid += round(MinimumMonthlyPayment, 2)
##    print("Month: " + str(i + 1))
##    print("Minimum monthly payment: $" + str('%.2f' % (MinimumMonthlyPayment)))
##    print("Principle paid: $" + str('%.2f' % (PrincipalPaid)))
##    print("Remaining balance: $" + str('%.2f' % (Balance)))
##
##print("RESULT")
##print("Total amount paid: $" + str('%.2f' % (TotalPaid)))
##print("Remaining balance: $" + str('%.2f' % (Balance)))

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


