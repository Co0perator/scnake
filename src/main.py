from keyword import kwlist
from args import argparse_setup
from string import punctuation
from validity import is_valid_python

def main():
    print(list(punctuation) + kwlist)
    inparse = argparse_setup()


if __name__ == "__main__":
    main()
