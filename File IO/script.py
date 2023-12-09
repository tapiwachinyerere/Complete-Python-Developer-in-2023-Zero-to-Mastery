my_file = open('test.txt')

print(my_file.read())   #end of file
my_file.seek(0)         #python uses the idea of a cursor to read a file
print(my_file.read())   #without the my_file.seek(0), this will be a blank output in the terminal
my_file.seek(0)
print(my_file.read())

my_file2 = open('test2.txt')
print(my_file2.readline()) #unlike .read() that moves the cursor to the end of the file, readline only reads to the end of the line.
print(my_file2.readline())
print(my_file2.readline())
print(my_file2.readline())
print(my_file2.readline())

print(my_file2.readlines()) #this returns a list that contains the entire file

my_file.close() #closing the file
my_file2.close()