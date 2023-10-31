#!/usr/bin/python3
"""define a text-indentation function."""


def text_indentation(text):
    """print indentated text.

    Args:
        text (string): Text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ctr = 0
    while ctr < len(text) and text[ctr] == ' ':
        ctr += 1

    while ctr < len(text):
        print(text[ctr], end="")
        if text[ctr] == "\n" or text[ctr] in ".?:":
            if text[ctr] in ".?:":
                print("\n")
            ctr += 1
            while ctr < len(text) and text[ctr] == ' ':
                ctr += 1
            continue
        ctr += 1

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
