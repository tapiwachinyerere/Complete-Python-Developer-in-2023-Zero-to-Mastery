from ast import pattern
import re

pattern = re.compile(r'[A-Za-z0-9$%#@]{8,}')

password = 'Mdsdwr34si2@'

if pattern.fullmatch(password):
    print('Password valid')
else:
    print('Password invalid.')