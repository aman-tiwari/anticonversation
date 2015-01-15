import nltk
from nltk.corpus import wordnet as wn
from itertools import chain
from random import choice
import speech_recognition as speech
import os

#Fixes some holes in the WordNet mapping
custom_map = {'am':'am', 'create':'destroy', 'kill':'make_life', 'worship':'deface',
                'are':'are', 'be':'be', 'is':'is', 'i am':'i am not'}
custom_map.update(reversed(i) for i in custom_map.items())
print custom_map
print custom_map['is']
def anti_words(word):
    """Returns a list of antonym for the word"""
    if word in custom_map:
        return [custom_map[word], custom_map[word]]
    ant_bag = set([word])
    for syn in wn.synsets(word):
        try:
            #print syn.lemmas()
            ant_bag.add(syn.lemmas()[0].antonyms()[0].name())
        except:
            ant_bag.add(word)

    if len(ant_bag) > 1:
        try:
            ant_bag.remove(word)
        except KeyError:
            pass
    return ant_bag

def anti_sentence(sentence):
    """A generator that chooses a random antonym for each word in the sentence and yields it"""
    words = sentence.split()
    for word in words:
        yield choice(tuple(anti_words(word)))
print list(anti_sentence('is'))

if __name__ == '__main__':
    recognizer = speech.Recognizer()
    recognizer.quiet_duration = 0.01
    recognizer.energy_threshold = 50
    recognizer.pause_threshold = 0.02

    while True:
        with speech.Microphone() as source:
            audio = recognizer.listen(source)
        print 'recognizing'
        try:
            recognized = recognizer.recognize(audio)
            anti = ''.join(anti_sentence( recognized ))
            print recognized
            if recognized != anti:
                os.system('say -v "Victoria" "' + anti + '"')
        except KeyError:
            print 'API key overused :('
        except LookupError: #can't recognize
            print 'what?'
