#Python Datetime Exercises
from datetime import datetime

# Get current date and time
now = datetime.now()

# Extract individual components
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print("Day:", current_day)
print("Month:", current_month)
print("Year:", current_year)
print("Hour:", current_hour)
print("Minute:", current_minute)
print("Timestamp:", current_timestamp)

#formatting date and time using the format "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

#Change the string "5 December, 2019" to a datetime object
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Datetime object:", date_object)

#Calculate the time difference between now and New Year
# Next New Year
new_year = datetime(current_year + 1, 1, 1)
time_difference = new_year - now

print("Time until New Year:", time_difference)

#Calculate the time difference between 1 January 1970 and now

epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch

print("Time since 1 January 1970:", time_since_epoch)

#Use Cases of the datetime Module
'''
The datetime module can be used for many purposes, such as:

    Time series analysis: Useful for working with time-based data in applications like finance or weather forecasting.
    Logging and auditing: Automatically generate timestamps for events in applications (e.g., logging user activities or errors).
    Post scheduling: Add timestamps to posts, emails, or notifications in a blog, CMS, or messaging application.
    Deadline calculation: Determine remaining time until a deadline (e.g., days left to submit an assignment).
    Date formatting: Convert date and time to readable formats or compare dates.
'''

#File Handling Exercises:
def count_lines_and_words(file_path):
    """
    Counts the number of lines and words in a text file.

    Parameters:
        file_path (str): Path to the file.

    Returns:
        tuple: (number of lines, number of words)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            return num_lines, num_words
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {e}"

# File paths
files = {
    "Obama's Speech": "/home/archellius-anami/Downloads/obama_speech.txt",
    "Michelle Obama's Speech": "/home/archellius-anami/Downloads/michelle_obama_speech.txt",
    "Melina Trump's Speech": "/home/archellius-anami/Downloads/melina_trump_speech.txt",
    "Donald Trump's Speech": "/home/archellius-anami/Downloads/donald_speech.txt"
}

# Process each file
for title, path in files.items():
    result = count_lines_and_words(path)
    if isinstance(result, tuple):
        print(f"{title}:")
        print(f"  Number of Lines: {result[0]}")
        print(f"  Number of Words: {result[1]}\n")
    else:
        print(f"{title} - {result}")

#countries most spoken languages
import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    """
    Finds the most spoken languages from a JSON file.

    Parameters:
        filename (str): Path to the JSON file.
        top_n (int): Number of top languages to return.

    Returns:
        list: A list of tuples containing the count and language, sorted by count.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
        
        # Extract all languages into a single list
        all_languages = []
        for country in countries_data:
            all_languages.extend(country.get("languages", []))
        
        # Count occurrences of each language
        language_counts = Counter(all_languages)
        
        # Get the top_n most common languages
        most_common_languages = language_counts.most_common(top_n)
        
        return most_common_languages
    
    except FileNotFoundError:
        return f"File not found: {filename}"
    except Exception as e:
        return f"An error occurred: {e}"

# File path to the countries_data.json file
filename = '/home/archellius-anami/Downloads/countries_data.json'

# Get the 10 most spoken languages
top_10_languages = most_spoken_languages(filename, 10)
print(top_10_languages)

# Get the 3 most spoken languages
top_3_languages = most_spoken_languages(filename, 3)
print(top_3_languages)

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json

def get_top_ten_populated_countries(file_path):
    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Sort the countries by population in descending order
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    
    # Get the top 10 populated countries
    top_ten = sorted_countries[:10]
    
    # Return a list of country names and their populations
    return [(country['name'], country['population']) for country in top_ten]


file_path = filename
top_ten_countries = get_top_ten_populated_countries(file_path)

# Print the result
for country, population in top_ten_countries:
    print(f"{country}: {population}")

#difference between melina  and michelle obama speech
import re
import string
from collections import Counter
from math import sqrt

# Function to load the stop words from the file
def load_stop_words(file_path):
    with open(file_path, 'r') as file:
        stop_words = set(file.read().splitlines())
    return stop_words

# Function to clean the text by removing punctuation and converting it to lowercase
def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text

# Function to remove stop words from the text
def remove_support_words(text, stop_words):
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

# Function to compute cosine similarity between two texts
def check_text_similarity(text1, text2):
    # Convert texts to word counts
    counter1 = Counter(text1.split())
    counter2 = Counter(text2.split())
    
    # Compute the dot product of the two vectors
    dot_product = sum(counter1[word] * counter2.get(word, 0) for word in counter1)
    
    # Compute the magnitude of each vector
    magnitude1 = sqrt(sum(count ** 2 for count in counter1.values()))
    magnitude2 = sqrt(sum(count ** 2 for count in counter2.values()))
    
    # Compute cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    else:
        return dot_product / (magnitude1 * magnitude2)

# Main function to compare two text files or strings
def compare_texts(file1, file2, stop_words_file = '/home/archellius-anami/Downloads/stop_words.py'):
    # Load the stop words
    stop_words = load_stop_words(stop_words_file)
    
    # Clean and preprocess both texts
    text1 = clean_text(file1)
    text2 = clean_text(file2)
    
    # Remove stop words
    text1_cleaned = remove_support_words(text1, stop_words)
    text2_cleaned = remove_support_words(text2, stop_words)
    
    # Check similarity
    similarity_score = check_text_similarity(text1_cleaned, text2_cleaned)
    
    return similarity_score

file1 =  "/home/archellius-anami/Downloads/michelle_obama_speech.txt"
file2 =  "/home/archellius-anami/Downloads/melina_trump_speech.txt"

similarity = compare_texts(file1, file2)
print(f"Similarity between the two texts: {similarity:.4f}")




#most repeated words in romeo_and_juliet.txt
import re
from collections import Counter
file = '/home/archellius-anami/Downloads/romeo_and_juliet.txt'

def get_most_repeated_words(file_path, top_n=10):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top N most common words
    most_common_words = word_counts.most_common(top_n)
    
    return most_common_words


file_path = file
most_common_words = get_most_repeated_words(file_path)


#hacker_news file read

import csv

def count_language_mentions(file_path):
    # Initialize counters for each language
    python_count = 0
    javascript_count = 0
    java_and_not_javascript_count = 0
    
    # Open the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        # Skip header if there is one
        header = next(reader, None)
        
        # Iterate through each row in the CSV
        for row in reader:
            # Assuming the relevant text is in the last column, adjust the index if necessary
            text = row[-1].lower()  # Convert to lowercase for case-insensitive matching
            
            # Check for Python or python
            if 'python' in text:
                python_count += 1
                
            # Check for JavaScript, javascript, or Javascript
            if 'javascript' in text:
                javascript_count += 1
                
            # Check for Java but not JavaScript
            if 'java' in text and 'javascript' not in text:
                java_and_not_javascript_count += 1
    
    return python_count, javascript_count, java_and_not_javascript_count


file_path = '/home/archellius-anami/Downloads/hacker_news.csv'
python_count, javascript_count, java_and_not_javascript_count = count_language_mentions(file_path)

# Print the results
print(f"Lines containing 'python' or 'Python': {python_count}")
print(f"Lines containing 'JavaScript', 'javascript', or 'Javascript': {javascript_count}")
print(f"Lines containing 'Java' but not 'JavaScript': {java_and_not_javascript_count}")
