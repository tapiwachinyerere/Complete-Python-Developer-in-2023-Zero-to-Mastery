from ast import pattern
import re

string = 'search this inside of this text'

a = re.search('this', string)

print(a.span())

print(a.group()) #useful when we want to do multiple searches

# b = re.search('that', string)

# print(b.span()) #when a value that does not exist in the string, the re returns None .

pattern = re.compile('this')

c = pattern.search(string)
d = pattern.findall(string) #finds all instances of the pattern
e = pattern.fullmatch(string) #returns an object if there is an exact match or None

print(e)