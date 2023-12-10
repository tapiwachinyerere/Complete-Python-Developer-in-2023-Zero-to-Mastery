from ast import pattern
import re

pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")

string = 'b@b.com'

a = pattern.search(string)

print(a)