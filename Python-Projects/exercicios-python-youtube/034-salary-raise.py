def salary_raise(salary):
    if salary > 1250:
        salary_r = salary * 0.10
        salary += salary_r
    
    if salary <= 1250:
        salary_r = salary * 0.15
        salary += salary_r
    
    return salary

print(salary_raise(1000))