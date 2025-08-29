# Librarys
from translate import Translator

# Languages which we want to get the translation
languages = ['fr', 'it', 'es','de']

# Standard input for the text to be translated
text = str(input("Enter Text to Translate >> "))

# Looping between the languages to get all of them
for language in languages:
    translator = Translator(provider='mymemory', from_lang='en', to_lang=language)
    translation = translator.translate(text)
    print(f'{language}: {translation}')