#Exercises: Module 6

    #Create an empty dictionary called dog
dog = {}
    
#Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Bingo",
    "color": "Black",
    "breed": "German Shepherd",
    "legs": 4,
    "age": 5
}

    #Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 25,
    "marital_status": "single",
    "skills": ["Python", "Java", "C++"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": "123 Main Street"
}

#Get the length of the student dictionary
print(len(student))

    #Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))
print(student["skills"])

    #Modify the skills values by adding one or two skills
student["skills"].append("PHP")
student["skills"].append("Ruby")    
print(student["skills"])

    #Get the dictionary keys as a list
print(student.keys())

    #Get the dictionary values as a list
print(student.values())

    #Change the dictionary to a list of tuples using items() method
print(student.items())

    #Delete one of the items in the dictionary
student.pop("address")
print(student)

    #Delete one of the dictionaries
del student
