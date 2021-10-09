from .argparser import argparser
from .folderikon import FolderIkon


def main():
    args = argparser.parse_args()
    FolderIkon(args).iconize()


if __name__ == "__main__":
    main()
