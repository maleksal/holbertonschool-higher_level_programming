#!/usr/bin/python3


def split_text(text, delim):
    """
    splits a text with a given delimiters

    Args:
        text: a given string
        delim (tuple): tuple of 3 delemiters

    Returns:
        finaltext: the final splited text

    """
    a, b, c = delim
    newline = "\n\n"

    part_1 = text.split(a)
    part_2 = "{}{}".format(
        a, newline).join(i.lstrip() for i in part_1).split(b)

    part_3 = "{}{}".format(
        b, newline).join(i.lstrip() for i in part_2).split(c)
    finaltext = "{}{}".format(c, newline).join(i.lstrip() for i in part_3)

    return finaltext


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: [.,?,:]

    Args:
        text (string): must be a string

    Returns:
        TypeError: if text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    textholder = split_text(text, ('.', '?', ':'))

    for i in textholder:
        print(i, end="")
