import datetime

from datetime import date

salary = input("Insert you salary: ")
loan = input("Insert the loan value: ")
payment_date = input("When you will finish your payment: ")

today_year = date.today().year

try:

    if int(payment_date) <= int(today_year):
        print("Insert a valid date.")

    month_bill = (int(loan) / ((today_year - int(payment_date)) * 12) * -1)
    salary_limit = (int(salary) * 0.30)

    if  int(month_bill) < salary_limit:
        print(f"Your loan has been approved and the tuition is {month_bill:.2f}, have a nice day")
    else:
        print("The loan has been rejected, because the tuition is greather than 30% \of your salary")

except ValueError:
    print("\n\nInsert valid values, please")



