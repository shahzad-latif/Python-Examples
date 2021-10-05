def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

name = input('What is your name? ')
language = input('What is your language [es, fr, en]? ')

print(greet(language),name)



