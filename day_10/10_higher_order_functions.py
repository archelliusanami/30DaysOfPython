'''  map is used for element-wise operations. It takes a function and an iterable and applies the function to each element in the iterable. It returns a new iterable with the transformed elements. Filter i used for conditional 
filtering, while reduce is used for aggregating elements. '''

''' diffrence between higher order function , closure and decorator is that higher order function is a function that takes a function as an argument or returns a function. A closure is a function that captures the
'''

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers)) 

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) 

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product)  


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print each country in the countries list
print("Countries:")
for country in countries:
    print(country)

# Print each name in the names list
print("\nNames:")
for name in names:
    print(name)

# Print each number in the numbers list
print("\nNumbers:")
for number in numbers:
    print(number)

#Exercise level 2

# Change each country to uppercase
uppercase_countries = list(map(lambda country: country.upper(), countries))
print("Uppercase countries:", uppercase_countries)

# Change each number to its square
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Change each name to uppercase
uppercase_names = list(map(lambda name: name.upper(), names))
print("Uppercase names:", uppercase_names)

# Filter out countries containing 'land'
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))
print("Countries containing 'land':", countries_with_land)

# Filter out countries having exactly six characters
countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))
print("Countries with exactly six characters:", countries_with_six_chars)

# Filter out countries containing six letters and more
countries_with_six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print("Countries with six or more letters:", countries_with_six_or_more)

# Filter out countries starting with 'E'
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
print("Countries starting with 'E':", countries_starting_with_e)


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chain map, filter, and reduce
result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 2 == 0,  # Keep only even numbers
        map(
            lambda x: x ** 2,  # Square the numbers
            numbers
        )
    )
)
print("Sum of squared even numbers:", result)  # Output: 220

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

# Example usage
mixed_list = [1, 'hello', True, 'world', 3.14, 'Python']
string_items = get_string_lists(mixed_list)
print("String items:", string_items)  # Output: ['hello', 'world', 'Python']

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sum all numbers
total_sum = reduce(lambda x, y: x + y, numbers)
print("Sum of all numbers:", total_sum)  # Output: 55

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Concatenate countries into a sentence
sentence = reduce(
    lambda x, y: x + ', ' + y,
    countries[:-1]
) + f", and {countries[-1]} are north European countries."
print(sentence)


def categorize_countries(pattern, countries_list):
    return list(filter(lambda country: pattern in country.lower(), countries_list))

# Example usage
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
pattern = 'land'
land_countries = categorize_countries(pattern, countries)
print("Countries containing 'land':", land_countries)  # Output: ['Finland', 'Iceland']

def countries_by_starting_letter(countries_list):
    from collections import defaultdict

    letter_count = defaultdict(int)
    for country in countries_list:
        letter_count[country[0]] += 1
    return dict(letter_count)

# Example usage
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
starting_letter_dict = countries_by_starting_letter(countries)
print("Countries by starting letters:", starting_letter_dict)


def get_first_ten_countries(countries_list):
    return countries_list[:10]

# Example usage
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Germany', 'Poland', 'Latvia', 'Lithuania', 'Russia']
first_ten = get_first_ten_countries(countries)
print("First ten countries:", first_ten)


def get_last_ten_countries(countries_list):
    return countries_list[-10:]

# Example usage
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Germany', 'Poland', 'Latvia', 'Lithuania', 'Russia']
last_ten = get_last_ten_countries(countries)
print("Last ten countries:", last_ten)

#Exercise level 3
# Load the data from the file
import json

# The countries data should be assigned to a variable
countries = [
    # Paste the full list of dictionaries from the file here or load dynamically
]

# Sort by name
countries_sorted_by_name = sorted(countries, key=lambda x: x["name"])

# Sort by capital
countries_sorted_by_capital = sorted(countries, key=lambda x: x["capital"])

# Sort by population
countries_sorted_by_population = sorted(countries, key=lambda x: x["population"])

print("Countries sorted by name:", [country["name"] for country in countries_sorted_by_name])
print("Countries sorted by capital:", [country["capital"] for country in countries_sorted_by_capital])
print("Countries sorted by population:", [country["name"] for country in countries_sorted_by_population])
   
from collections import Counter

# Flatten the list of all languages
all_languages = [lang for country in countries for lang in country["languages"]]

# Count occurrences of each language
language_counts = Counter(all_languages)

# Get the 10 most spoken languages
top_10_languages = language_counts.most_common(10)

print("Top 10 most spoken languages by location:", top_10_languages)


# Sort by population in descending order and get the top 10
most_populated_countries = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]

print("Top 10 most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

