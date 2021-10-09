"""Exception which are not actually thrown, only their docstrings are used."""

import colorama
import sys

__all__ = [
    "Error",
    "ParentIsNotAFolderError",
    "InvalidURLError",
    "ImageFormatNotSupportedError",
    "ImageNotSpecifiedError",
    "FolderIconAlreadyExistsError",
    "DesktopIniError",
    "exception_exit",
]


class Error(Exception):
    """Base class for all FolderIkon errors."""

    color = False

    def __repr__(self):
        return self.red(self.__doc__)

    @staticmethod
    def red(string):
        if Error.color:
            return colorama.Fore.RED + string
        return string


class ParentIsNotAFolderError(Error):
    """Argument passed to --parent is not a folder."""


class InvalidURLError(Error):
    """Invalid image URL"""

    def __init__(self, url):
        self.__url = url
        super().__init__()

    def __repr__(self):
        return super().__repr__() + " " + self.__url


class ImageFormatNotSupportedError(Error):
    def __init__(self, fmt):
        self.__fmt = fmt
        super().__init__()

    def __repr__(self):
        return f"Image format {self.red(self.__fmt)} is not supported. Only ICO, JPG and PNG are supported."


class ImageNotSpecifiedError(Error):
    """An image with a supported format could not be found in this directory."""


class FolderIconAlreadyExistsError(Error):
    """Folder icon already exists."""


class DesktopIniError(Error):
    """The 'desktop.ini' file could not be parsed. Delete it and try again."""

    def __init__(self, exc):
        self.__exc = exc
        super().__init__()

    def __repr__(self):
        exc_name = self.__exc.__class__.__name__
        exc_info = f"An exception of {exc_name} occured when parsing it."
        return super().__repr__() + " " + exc_info


def exception_exit(exc):
    print(repr(exc()))
    sys.exit(-1)
