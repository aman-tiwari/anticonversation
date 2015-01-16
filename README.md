Anti-Conversation
=================

Anti aims to disrupt human communication by inverting the meaning of any sentence it hears and talking over the conversation.

## Libraries
* NLTK
    * Wordnet
* Google Speech Recognition API, with Python wrapper by Uberi (https://github.com/Uberi/speech_recognition)

# How does it work?

Anti uses the google speech recognition api to process human speech. It processes the recognized words using WordNet and finds their antonyms. On capable hardware, this happens fast enough for it to be able to talk over the conversation, ignoring the words it can't invert and speaking just the ones it can.

# Gallery Plan

Although it is unlikely that Anti will be featured in a gallery (at least, in its current state), I have drawn up a gallery plan for it: [gallery-plan](../gallery-plan.pdf)

## Future Goals

* Use better text-to-speech (currently uses OS X's terrible `say` command)
* Cache results for antonyms so it gets results faster
