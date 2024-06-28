# Creating a HashMap
my_dict = {}

# Adding key-value pairs
my_dict['apple'] = 10
my_dict['banana'] = 20
my_dict['orange'] = 15

# Accessing values
print("Value for 'apple':", my_dict['apple'])  # Output: 10

# Updating value
my_dict['apple'] = 12

# Removing a key-value pair
del my_dict['orange']

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, ':', value)
