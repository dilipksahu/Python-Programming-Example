# Reverse words in a given String in Python

def reverseWords(sentence):
    words = sentence.split(" ")
    rev_sentence = reversed(words)
    print(" ".join(rev_sentence))

s = "geeks quiz practice code"
reverseWords(s)