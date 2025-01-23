#list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [i for i in numbers if i <= 0]
print(neg_and_zero)

#flatten list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row in list_of_lists for inner_row in row for number in inner_row]
print(flattened_list)

#creating list comprehension
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
#list comprehension
# Generate the list using list comprehension
result = [(i,) + tuple(i ** j for j in range(1, 7)) for i in range(11)]

# Print the result
for row in result:
    print(row)
#flatten countires
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(output)
#dict comprehension
dict = [{'country':country.upper(), 'capital':capital.upper()} for [(country, capital)] in countries]
print(dict)

#concatenate list
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [name for [(first_name, last_name)] in names for name in [f'{first_name} {last_name}']]
print(output)

#lambda function
# Lambda function for slope and y-intercept
linear_solver = lambda mode, x1, y1, x2=None, y2=None: (y2 - y1) / (x2 - x1) if mode == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1 if mode == 'y-intercept' else None

# Examples of usage:

# Find slope
slope = linear_solver('slope', 2, 3, 5, 11)  # Points: (2, 3) and (5, 11)
print(f"Slope: {slope}")

# Find y-intercept
y_intercept = linear_solver('y-intercept', 2, 3, 5, 11)  # Points: (2, 3) and (5, 11)
print(f"Y-Intercept: {y_intercept}")
