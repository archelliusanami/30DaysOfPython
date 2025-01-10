#Conditional exercise
#user input on conditional statements
age = int(input("Enter your age: "))
if age > 18:
    print("You are a old enough to drive")
else:
    print(f"You need {18 - age} more years to drive")

#Exercise 2
#user input on conditional statements to compare two ages
age = int(input("Enter your age: "))
my_age = 33
if age > my_age:
    if age - my_age == 1:
        print("You are one year older than me")
    else:
        print(f"You are {age - my_age} years older than me")

elif age < my_age:
    if my_age - age == 1:
        print("I am one year older than you")
    else:
        print(f"I am {my_age - age} years older than you")
else:
    print("we are the same age")

#Exercise 3
#user input on conditional statements to compare two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#Exercise 4
#school_grade
score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

#Exercise 5
#season
month = input("Enter month: ")
if month == "September" or month == "October" or month == "November":
    print("It is Autumn")
elif month == "December" or month == "January" or month == "February":
    print("It is Winter")
elif month == "March" or month == "April" or month == "May":
    print("It is Spring")
elif month == "June" or month == "July" or month == "August":
    print("It is Summer")
else:
    print("Invalid month")

#Exercise 6
#fruit 
fruit = ["banana", "orange", "mango", "lemon"]
user_input = input("Enter a fruit: ")
if user_input in fruit:
    print(f"{user_input} already exists in the list")
elif user_input not in fruit:
    fruit.append(user_input)
    print(fruit)
else:
    print("Invalid fruit")

#Exercise 7
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])
else:
    print("Skills key not found")

#Check if the person dictionary has the key title, if so remove the key in the dictionary, if not print out the key not found.
if "title" in person:
    person.pop("title")
    print(person)
else:
    print("Key not found")

#if skil has javascript, react, node, print out the message saying, the person is a frontend developer, if the person has node, react, python, mongodb, print out the message saying, the person is a backend developer, if the person has react, node, mongodb, print out the message saying, the person is a fullstack developer, else print out the message saying the person is a programmer.
if "skills" in person:
    if "JavaScript" in person["skills"] and "React" in person["skills"] and "Node" in person["skills"]:
        print("The person is a frontend developer")
    elif "Node" in person["skills"] and "React" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
        print("The person is a backend developer")
    elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
        print("The person is a fullstack developer")
else:
    print("The person is a programmer")    

#Check if the person is married and has a country key. If so, print out the country in which the person lives.
if "is_married" in person and "country" in person:
    print('Asabeneh Yetayeh lives in Finland. He is married.')
else:
    print("Country not found")
    
