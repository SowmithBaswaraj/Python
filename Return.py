#Ask user to enter his age
#Ask user to enter his cgpa
#Write a function called eligible
#True if eligible age>18,cgpa>8

age=int(input('Enter your age: '))
cgpa=float(input('Enter your cgpa: '))
def check_eligibility(age,cgpa):
    if age > 18 and cgpa >8:
        return "true"
    else:
        return "False"
print(check_eligibility(age, cgpa))