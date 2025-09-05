mess='python is fun'
print(mess.upper())
print(mess.lower())

#replace()
text='CE Department'
replaced_text=text.replace('CE','ICT')
#replaced_text=text.replace('ce','ict')--error will not come-text will be unreplaced
print(replaced_text)

#find()
mess='Python is a fun programming language fun'
print(mess.find('fun'))

#rstrip()
title='Python Programming g'
print(title.rstrip('g'))

#split
text='Python is fun'
print(text.split())

#startswith()
mess='Python is fun'
print(mess.startswith('python'))
print(mess.startswith('Python'))

#isnumeric()
pin="523"
print("\n",pin.isnumeric())

#index()
text='Python is fun'
print(text.index('is'))
#print(text.index('IS'))--value Error-substring not found

#f-strings
name='Cathy'
country='UK'
print(f'\n{name} is from {country}')

#raw string
str="This is a \n normal string example"
print(str)
print(r"This is a \n raw string example")