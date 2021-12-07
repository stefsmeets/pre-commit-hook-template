import argparse
from typing import Optional
from typing import Sequence


def check_file(filename):
    # your condition here
    if True:
        print(f'{filename}: Your condition here.')
        return 1
    else:
        return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0
    
    for filename in args.filenames:
        retv = check_file(filename)
    
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
