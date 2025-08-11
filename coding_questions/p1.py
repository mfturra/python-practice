'''Write a Python function called word_frequency(text) that takes a string text and returns a dictionary where the keys are unique words 
in the text (case-insensitive, punctuation excluded), and the values are the number of times each word appears.

Requirements:
- Treat words as case-insensitive (e.g., "Hello" and "hello" should be counted as the same word).
- Exclude all punctuation (only count actual words).
- Return the result as a dictionary sorted by the most frequent word first. If two words have the same frequency, sort them alphabetically.'''
import re

def word_frequency(text: str) -> dict:
    # create an var to store all elements in text
    sentence = {}
    
    # extract each elements in the string of text
    text_extraction = text.lower().split()

    # store list elements into a dict
    for word in text_extraction:
        # extract special characters from elements in list entries
        cleaned_word = re.sub(r'[^a-z0-9]', '', word)
        print(cleaned_word)

        # store word as key and count as val
        sentence[cleaned_word] = text_extraction.count(cleaned_word)

    return sentence
    # print(sentence)




# input example
text = "Hello, hello! How are you? Are you learning Python? Python is great!"
print(word_frequency(text))