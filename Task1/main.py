import os
first_name = os.environ.get('first_name')
last_name = os.environ.get('last_name')
age = os.environ.get('age')
print(f'Hello my name is {last_name} {first_name} and I am {age}')
