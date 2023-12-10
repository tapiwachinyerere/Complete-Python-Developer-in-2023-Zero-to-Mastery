#Created a translate file in the terminal

#Write into the file.
with open('translate.txt', mode='w') as my_file:
    text = my_file.write('I love my wife so much.')
    #print(text)

from translate import Translator
translator = Translator(to_lang='sn')
try:
    with open('translate.txt', mode='r') as my_file:
        translation = translator.translate(my_file.read())
        with open('translation-sn.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('File not found.')
    raise err
