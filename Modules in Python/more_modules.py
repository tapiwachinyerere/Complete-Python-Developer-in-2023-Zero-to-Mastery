from collections import Counter, defaultdict

my_list = [1,2,3,2,2,4,5]

print(Counter(my_list))

sentence = 'Hello, good morning guys. My name is Tapiwa and I will be your tutor for today.'

print(Counter(sentence))

my_dict = defaultdict(lambda: 'Key doesn\'t exist', {
    'a': 12,
    'b': 55,
    'c': 1
})

print(my_dict['d'])

import datetime

print(datetime.date.today())

