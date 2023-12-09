'''Reading, Writing and Appending a file in Python'''
with open('test.txt', mode='a') as my_file:    #mode='r' specifies that we ONLY want to read the file.
                                                #In order to read and write, we use mode = (r+), but this reads to the end, resets the curser to zero, and overwrites existing (if any)
    text = my_file.write('My name is Tapiwa.')
    #print(my_file.read()) #if we read a file this way there is no need to close it after
    print(text) #but we broke what we had originally

#in order to add to the end of the file we use mode = 'a'
