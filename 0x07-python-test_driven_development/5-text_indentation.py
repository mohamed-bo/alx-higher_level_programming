#!/usr/bin/python3
"""
"5-test_indentation" module.
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for oc in ".:?":
        text = (oc + "\n\n").join([l.strip(" ") for l in text.split(oc)])
    print(text, end="")
