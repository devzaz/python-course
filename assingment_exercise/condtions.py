india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

"""user_input = input("enter city name: ", )

if user_input in india:
    print("this city belongs to india")
if user_input in pakistan:
    print("this city belongs to pakistan")
if user_input in bangladesh:
    print("This city belongs to bangladesh")"""

#question 2

"""user_input = input("Enter two city name (ex: Mumbai Chennai)", )

city_1 , city_2 = user_input.split(" ")

if city_1 in india and city_2 in india:
    print("Both cities are in India")
if city_1 in pakistan and city_2 in pakistan:
    print("Both cities are in India")
if city_1 in bangladesh and city_2 in bangladesh:
    print("Both cities are in India")
else:
    print ("They don't belong to same country")
"""

#question 3

"""Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal"""

user_sugar = int(input("Enter your sugar level: ", ))

if user_sugar <= 80:
    print("sugar is low")
elif user_sugar >= 100:
    print("your sugar is high")
