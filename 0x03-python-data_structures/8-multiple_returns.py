#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return(0, None)
    word = sentence.split()
    first_char = word[0]

    return (len(sentence), first_char)
