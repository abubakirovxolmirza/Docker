import os
a, b, c = (os.environ.get('first_name')), (os.environ.get('last_name')), (os.environ.get('age'))
print(f'Hello my name is {b} {a} and I am {c}')