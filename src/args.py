import argparse

def argparse_setup() -> argparse.ArgumentParser:
    out = argparse.ArgumentParser(
        prog="Scnake",
        description="Transpiles Python to C",
        epilog="Sclither at a faster rate with Scnake!")
    
    out.add_argument('-v, --verbose')
    out.add_argument('-h, --help')

    return out