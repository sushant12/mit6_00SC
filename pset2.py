##Author: sushant bajracharya(sussyoung9@gmail.com)
##time: 1hrs

MONTHS = 12
outstanding_balance = float(raw_input("Enter the outstanding balance on your credit card:" ))
annual_interest_rate =  float(raw_input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = annual_interest_rate/MONTHS

min_monthly_payment = 0

balance = outstanding_balance

def apply_min_payment(balance):
    balance = balance + (balance * monthly_interest_rate) - min_monthly_payment
    return balance

while balance > 0:
  balance = outstanding_balance
  min_monthly_payment += 10
  
  for i in range (0,MONTHS):
    balance = apply_min_payment(balance)
    if balance < 0:
      break


print "RESULT"
print "Monthly payment needed to pay off in one year: " + str(round(min_monthly_payment,2))
print "Number of months needed: " + str(i+1)
print "Balance: " + str(round(balance,2))
