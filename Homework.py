num=int(input("Enter the amount of days you attended school"))
num2=int(input("Enter the amount of days you were absent"))

if num>num2%75:
    print("You are eligible to the attend the exams.")
else:
    print("You are not eligible to attend the exam.")