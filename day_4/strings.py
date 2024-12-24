t = 'Thirty'
d = 'Days'
o = 'Of'
p = 'Python'
print(t + ' ' + d + ' ' + o + ' ' + p)

c = 'Coding'
f = 'For'
a = 'All'
print(c + ' ' + f + ' ' + a)

# Exercise 2    
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company[7:10])
print(company[11:14])
print(company.replace('Coding', 'Python'))
name = 'Python for Everyone'
print(name.replace('Everyone', 'All'))
print(company.split(' '))
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))
#
print(company[0])
print(company.rindex('All'))
print(company[10])
#acroynm for python for everyone
name = 'Coding For All People'
cd = 'Co'
fe = 'Fo'
print(company.index(cd))
print(company.index(fe))
print(name.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

sentence1 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence1.rfind('because'))
#sclicing the word because in sentence
print(sentence[31:54])
print(sentence1.index('because'))

#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#use the method isidentifier()
py = '30DaysOfPython'
py2 = 'thirty_days_of_python'
print(py.isidentifier())
print(py2.isidentifier())

#use .join() method to join the words of the list
words = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(words))
#use escape character to write the following sentence
sentence = 'I am enjoying this challenge. I just wonder what is next.'
print('I am enjoying this challenge. \nI just wonder what is next.')
#use tab  escape sequence
bd = 'Name\tAge\tCountry\tCity'
ns = 'Asabeneh\t250\tFinland\tHelsinki'
print(bd)
print(ns)
#string formatting
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f meters square' % (radius, area))

#strng formatting using f-string
print(f'The area of a circle with radius {radius} is {area} meters square')


print('{} + {} = {}'.format(8, 6, 8 + 6))
print('{} - {} = {}'.format(8, 6, 8 - 6))
print('{} * {} = {}'.format(8, 6, 8 * 6))
print('{} / {} = {:.2f}'.format(8, 6, 8 / 6))
print('{} % {} = {}'.format(8, 6, 8 % 6))
print('{} // {} = {}'.format(8, 6, 8 // 6))
print('{} ** {} = {}'.format(8, 6, 8 ** 6))




