with open('sad.txt', mode='w') as new_file: #write creates a new file if it doesn't exist already or overwrites the existing one.
    text = new_file.write(':(')
    print(text)