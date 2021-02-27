# DICTIONARIES LESSON
# Dictionaries
# A dictionary in Python is a scrambled collection of objects. Unlike other data types such as a list or a set
# which has a single value field, the dictionary type stores a key along with its value.
# The keys pair with values using a colon (:) while the commas work as a separator for the elements.
# Also, the entire dictionary object uses curly braces to enclose itself.
# The empty Python dictionary object{}
# Keys inside a dictionary can’t have duplicates, but their values can repeat themselves.
# The value in a dictionary can be of any valid Python data type.
# But the keys have a constraint to be of any immutable data types such as a string, a number, or a tuple.

# Dictionary in Python

# Create Dictionaries
# If you wish to create a Python dictionary with fixed keys and values, then it’s quite easy to do so.
# Just combine all the “key1:value1, key2: value2, …” pairs and enclose with curly braces.
# The combination of a key and its value, i.e. “key: value” represents a single element of a dictionary in Python.
# Define a blank dictionary with no elements
blank_dict = {}
# Define a dictionary with numeric keys
num_dict = {1: 'soccer', 2: 'baseball'}
# Define a dictionary with keys having different types
misc_dict = {'class': 'senior secondary', 1: [1, 2, 3, 4, 5]}
# Create a dictionary with dict() method
get_dict_from_func = dict({1: 'veg', 2: 'non-veg'})
# Create a dictionary from a sequence of tuples
make_dict_from_seq = dict([(1, 'jake'), (2, 'john')])

# Python dictionary has the key as an additional parameter.We can access the elements of a dictionary with the help
# of keys by using them as Index to the array operator ([]) or passing as Argument to the get() method.
# Both methods will work the same, but the former will return a KeyError while the latter returns None if the element is not available.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("dict['Student Name']: ", dict['Student Name'])
print("dict['Roll No.']: ", dict['Roll No.'])
print("dict['Subject']: ", dict['Subject'])
# output.
# dict['Student Name']: Berry
# dict['Roll No.']: 12
# dict['Subject']: English

# Accessing an element with a non-existent key will return an error.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
#print("dict['Name']: ", dict['Name'])
# Uses the “Name” key which doesn’t exist.Produces a “KeyError.” Traceback(most recent call last): File "C:/Python/Python35/test_dict.py", line 2, in < module > print("dict['Name']: ", dict['Name']) KeyError: 'Name'

# Access the elements in a Python dictionary using the get() function.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print(dict.get('Student Name'))
print(dict.get('Roll No.'))
print(dict.get('Subject'))
# result.
# Berry
# 12
# English

# Append in a Dictionary
# You can append a new item to an existing dict object with elements in the following two ways.

# Assignment to Append Elements
dict_append = {"1": "Python", "2": "Java"}
print(dict_append)
# {'1': 'Python', '2': 'Java'}
dict_append["3"] = "CSharp"
print(dict_append)
# {'1': 'Python', '3': 'CSharp', '2': 'Java'}

# Update Method to Append Elements
# You can call the dictionary’s update method to append a new element to it.
dict_append.update({"4": "JavaScript"})
print(dict_append)
# {'1': 'Python', '3': 'CSharp', '2': 'Java', '4': 'JavaScript'}

# Update a Dictionary
# Python allowed the dictionary object to be mutable. Hence, the add or update operations are permissible.
# You can push a new item or modify any existing with the help of the assignment operator.

# Whenever you add an element whose key already exists, it’s value will get changed to the new value.
# On adding a fresh “key: value” pair, a new element will get added to the dictionary.

# Use Assignment
# In the below example, we are demonstrating both the update and the addition operations on the existing dictionary object.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("The student who left:", dict.get('Student Name'))
dict['Student Name'] = 'Larry'
print("The student who replaced: [Update]", dict.get('Student Name'))
dict['Student Name'] = 'Jarry'
print("The student who joined: [Addition]", dict.get('Student Name'))
# output.
# The student who left: Berry
# The student who replaced: [Update] Larry
# The student who joined: [Addition] Jarry

# Use the Update Method
# You can alternatively call the update method to modify the value of any existing element.

# It has a dict object which contains a key as ‘Student Name’.We’ll update its value.
sample_dict = {"python": 1, "csharp": 2, "javascript": 3}
sample_dict.update(javascript=2)
print(sample_dict)
# {'python': 1, 'javascript': 2, 'csharp': 2}
sample_dict.update(csharp=3)
print(sample_dict)
# {'python': 1, 'javascript': 2, 'csharp': 3}

# Remove Elements
# Python lends us a no.of methods to remove elements from the dictionary.
# The most common of them is the “pop()” method.
# It takes the key as the input and deletes the corresponding element from the Python dictionary.
# It returns the value associated with the input key.
# Another method is “popitem()”.It removes and returns a random element(key, value) from the dictionary.

# drop all the elements from the dictionary, then use the “clear()” method to flush everything.
# One more way to remove an element from a dictionary is to use the del keyword.
# It can help you delete individual items and consequently the whole dictionary object.

# Create a Python dictionary
sixMonths = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30}

# Delete a specific element
print(sixMonths.pop(6))
print(sixMonths)

# Delete an random element
print(sixMonths.popitem())
print(sixMonths)

# Remove a specific element
#del sixMonths[5]
#print(sixMonths)

# Delete all elements from the dictionary
sixMonths.clear()
print(sixMonths)

# Finally, eliminate the dictionary object
#del sixMonths
#print(sixMonths)
# 30
# {1: 31, 2: 28, 3: 31, 4: 30, 5: 31}
# (1, 31)
# {2: 28, 3: 31, 4: 30, 5: 31}
# {2: 28, 3: 31, 4: 30}
# {}
# Traceback(most recent call last):
# File "C:/Python/Python35/test_dict.py", line 22, in < module > print(sixMonths) NameError: name 'sixMonths' is not defined
# In the above example, the second last statement removes all the elements from the Python dictionary, leaving it empty.

# And the subsequent call to the “del” operator on the dictionary object removes it altogether.Hence, the last
# print statement fails with the “NameError.”

# Dictionary Attributes
# Python doesn’t impose any constraints on the “Values” of a dictionary object.You can form them using the standard Python or any
# custom data types.But, as we said earlier, the “Keys” aren’t the same as “Values” and have altogether different handling.

# Hence, it is vital for you to memorize the following two facts about the dictionary “Keys.”
# The same key can’t have another value in the dictionary.It confirms that a duplicate key can’t exist.
# However, even if you try to supply a duplicate key, it’ll only modify the existing key with the value provided in the last assignment.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English', 'Student Name': 'Kerry'}
print("dict['Student Name']: ", dict['Student Name'])
# the key “Student Name” will keep the last assigned value, i.e., “Kerry.”
# dict['Student Name']: Kerry

# Python says that the dictionary Keys should derive from the immutable data types.
# You can infer that only allowed types are strings, numbers or tuples.Check out a standard example below.
dict = {['Student Name']: 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("dict['Student Name']: ", dict['Student Name'])
# In the above example, the key is using a list type.Since Python doesn’t support this, hence the statement will generate a “TypeError.”
# Traceback(most recent call last): File "C:/Python/Python35/test_dict.py", line 1, in < module > dict = {['Student Name']: 'Berry', 'Roll No.': 12, 'Subject': 'English'} TypeError: unhashable type: 'list'

# Iterate Dictionary
# Similar to the lists, you can use a “for in ” loop to traverse through a dictionary.In general, it’s the keys which enable iteration.
# Let’s understand the concept with a simple example.It prints all the keys of a dictionary in a loop.
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("Keys are:")
for key in dict:
    print(key)
# Output
# Keys are: Student Name Roll No. Subject
dict = {'Student Name': 'Berry', 'Roll No.': 12, 'Subject': 'English'}
print("{Keys}:{Values}")
for key, value in dict.items():
    print({key}, ":", {value})
# Output
# {Keys}: {Values}
# {'Student Name'}: {'Berry'}
# {'Roll No.'}: {12}
# {'Subject'}: {'English'}

# Dictionary Comprehension
# Just like a Python list, the dictionary also allows comprehension to create new objects from an iterable in a loop.
# You can specify a dictionary comprehension by using an expression including a “key: value” pair followed by for loop and enclosed with curly braces {}.

# Make a dictionary object with the string type for keys and the number format for values.
{str(iter): iter for iter in [11, 22, 33, 44, 55]}
# {'44': 44, '33': 33, '55': 55, '11': 11, '22': 22}
# Creating a dictionary from the list of weekdays as keys and the length of each week as the values.
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
{w: len(w) for w in weekdays}
# {'fri': 3, 'tue': 3, 'wed': 3, 'sat': 3, 'thu': 3, 'mon': 3, 'sun': 3}
# We can use the “enumerate()” function in a dictionary comprehension.
# It helps us save the index of a specific element that we could use later.
# Also, in afor loop, the position of a list element isn’t visible without “enumerate().”
# Such Python dictionaries which have element index can be useful in many situations.
{w: i for i, w in enumerate(weekdays)}
# {'fri': 5, 'tue': 2, 'wed': 3, 'sat': 6, 'thu': 4, 'mon': 1, 'sun': 0}

# Membership Test
# We can quickly confirm whether a Key is present in a dictionary or not using the keyword “ in.”
# Also, please note that the membership test is only applicable to Keys, not for Values.
weekdays = {'fri': 5, 'tue': 2, 'wed': 3, 'sat': 6, 'thu': 4, 'mon': 1, 'sun': 0}
# Output: True
print('fri' in weekdays)
# Output: False
print('thu' not in weekdays)
# Output: True
print('mon' in weekdays)
# Output
True
False
True