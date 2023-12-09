try:
    with open('../sad.txt', mode='r') as new_file:
        print(new_file.read())
except FileNotFoundError as err:
    print('File does not exist.')
    raise err
except IOError as err: #computer has some issues reading, writing or doing any IO related operation
    print('IO Error.')
    raise err