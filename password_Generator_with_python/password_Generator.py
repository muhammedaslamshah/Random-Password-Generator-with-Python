'''
This Python script generates strong, unique, and user-friendly 
passwords for enhanced security. It incorporates character sets 
of lowercase and uppercase letters, numbers, and special 
characters, making it suitable for both security and user-friendliness.

'''


import random

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@$%^&*()_-=+[]|;:/?.>,<'

total = lower_letters + upper_letters + numbers + special_characters

generated_password = ''.join(random.sample(total, 14))

print("password generated is : ", generated_password)