"""
Miscellaneous string functions

More detailed description here
"""

# imports go here


def title_string(s):
    """
    Convert a string to title case

    Title case means that the first character of
    every word is capitalized, otherwise lowercase.

    Parameters
    -----------
    s : str
        The string to convet to title case

    Returns
    -----------
    str
        The input string in title case

    Examples
    ------------
    >>> title_string("this iS a StrINg to be ConverTed")
    'This Is A String To Be Converted'
    """
    # Check that input is string
    if not isinstance(s, str):
        raise TypeError('Input must be string')

    # Empty string
    if len(s) == 0:
        raise IndexError('Cannot apply title function to empty string')

    ret = s[0].upper()

    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            ret += s[i].upper()
        else:
            ret += s[i].lower()

    return ret
