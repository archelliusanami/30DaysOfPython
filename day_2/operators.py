Age = 33
Height = 5.1
# Complex numbers
Complex_number = 10 + 6j
#prompt user to enter a number
base = int(input("Enter base: "))
Height = int(input("Enter height: "))
print("The area of triangle is: ", 0.5 * base * Height)
#prompt user to get perimeter of a triangle
Length = int(input("Enter side a: "))
Width = int(input("Enter side b: "))
Height = int(input("Enter side c: "))
print("The perimeter of triangle is: ", Length + Width + Height)
#prompt for raidus of a circle
radius = int(input("Enter radius: "))
print("The area of circle is: ", 3.142 * radius ** 2)
#prompt for circumference of a circle
radius = int(input("Enter radius: "))
print("The circumference of circle is: ", 2 * 3.142 * radius)

#calculate the slope, y-intercept and x-intercept of y=2x-2
x = 2
y = 2 * x - 2
print("The y-intercept is: ", y)
slope = 2
print("The slope is: ", slope)

#slope (m) = (y2-y1)/(x2-x1),find the slope of the line (2,2) and (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("The slope of the line is: ", slope)

#find length of words
word1 = len("Python")
word2 = len('dragon')

#compare the length of the two words
print(word1 == word2)
print(word1 != word2)
print(word1 > word2)
print(word1 < word2)

print('jargon' in 'I hope this course is not full of jargon')
print('on' in 'dragon', 'on' in 'python')
print(float(word1))
print(str(word1))

#check if the number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#check floor division equal to int converted value of 2.7
num1 = 7
num2 = 3
result = num1 // num2
print(result == int(2.7))

#check if type of '10' is equal to 10
print(type('10') == type(10))

#check if int('9.8') is equal to 10
print(int('9.8') == 10)

#calculate pay using hours and rate
hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))
pay = hours * rate
print("Your weekly earning is: ", pay)

#prompt calculate numer of years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for ", seconds, "seconds")

#code that prints table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
    
