# Hindi to English Text Translator
# ---------------------------------

# This code utilizes the Googletrans(translator) library to create a simple translation tool
# that converts user hindi text input into English. It uses the Google Translate API
# to perform the translation. The translation function takes a Hindi text as input and
# Response English translation.

from googletrans import Translator

def hindi_to_english(text):
    """
    Translates Hindi text to English using the Googletrans library.

    Parameters:
    - text (str): The input Hindi text to be translated.

    Returns:
    - str: The English translation of the input text.
    """
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text

# Example Usage:
# --------------

# The code enters into a loop where the user can input Hindi text for translation.
# If the user types 'exit', the loop will be break, and the script shall be end. Otherwise, it keep translates
# input Hindi text convert into English text and displays the result.

while True:   
    hindi_text = input("Enter the text to translate to Hindi (type 'exit' to quit): ")
    if hindi_text.lower() == "exit":
    
        break
    english_translation = hindi_to_english(hindi_text)
    print(f"English: {english_translation}")
