import os
import nltk
from nltk.corpus import wordnet
from deep_translator import GoogleTranslator

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

def run(flags, args):

    if "t" in flags:
        print(GoogleTranslator(source="en", target="sv").translate(" ".join(args)))
    else: # "d" or []
        synsets = wordnet.synsets(" ".join(args)) # Synonym sets, a word can have multiple meanings
        for word in synsets:
            print("\"" + word.definition() + "\"")
