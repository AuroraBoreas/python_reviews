"""

this module is to demonstrate Python built-in library string;

@ZL, 20210303

"""

import string
import pprint

def what_inside_of_string_mod():
    '''
    ascii_letters'
    ascii_lowercase'
    ascii_uppercase'
    capwords'
    digits'
    hexdigits'
    octdigits'
    printable'
    punctuation'
    whitespace'
    Formatter'
    Template'
    '''
    for item in string.__all__:
        pprint.pprint(item)

def what_are_details():
    # ascii_letters
    for item in string.__all__:
        print("\n{0} : ".format(item))
        pprint.pprint(getattr(string,  item))


def main():
    what_inside_of_string_mod()
    print("\n*** *** *** *** *** ***\n")
    what_are_details()

if __name__ == '__main__':
    main()
